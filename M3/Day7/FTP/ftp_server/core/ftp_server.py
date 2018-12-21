#_*_coding:utf-8_*_
#__author__: Zhang Qing

import socketserver
import json
import configparser
import os
from conf import settings

STATUS_CODE = {
    250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251: "Invalid cmd ",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
    255: "Filename is not provided",
    256: "File doesn't exist on server",
    257: "ready to send file",
    258: "ready to receive file",
    259: "ready to show the files",
    260: "No file is found",
}

class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data=self.request.recv(1024).strip()
            print("Connected client: ",self.client_address[0])
            print(self.data)
            if self.data == b'':
                print("client is closed.")
                break
            else:
                data=json.loads(self.data.decode())
            if data.get("action"):
                if hasattr(self, "_%s"%data.get("action")):
                    func=getattr(self, "_%s"%data.get("action"))
                    func(data)
                else:
                    print(STATUS_CODE[251])
                    self.send_response(251)
            else:
                print(STATUS_CODE[250])
                self.send_response(250)

    def send_response(self,status_code,data=None):
        response_msg = {"status_code": status_code, "status_msg": STATUS_CODE[status_code]}
        if data:
            response_msg.update(data)
        self.request.send(json.dumps(response_msg).encode())

    def _auth(self,data):
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        username = data.get("username")
        password = data.get("password")
        if username:
            if username in config.sections():
                if password == config[username]["password"]:
                    print(STATUS_CODE[254])
                    self.send_response(254)
                    config[username]["username"]=username
                    self.user=config[username]
                    self.user_home="%s/%s"%(settings.HOME_BASE,self.user["username"])
                else:
                    print(STATUS_CODE[253])
                    self.send_response(253)
            else:
                print(STATUS_CODE[253])
                self.send_response(253)
        else:
            print(STATUS_CODE[252])
            self.send_response(252)

    def _get(self,data):
        if data.get("file_name"):
            file_name = data["file_name"]
        else:
            print(STATUS_CODE[255])
            self.send_response(255)
            return
        file_abs_path = "%s/%s"%(self.user_home, file_name)
        if os.path.isfile(file_abs_path):
            file_size = os.path.getsize(file_abs_path)
            print(STATUS_CODE[257])
            self.send_response(257,data={"file_size":file_size})
            self.request.recv(1)
            file_hd = open(file_abs_path,'rb')
            for line in file_hd:
                self.request.send(line)
            else:
                file_hd.close()
                print("File sending is done.")
        else:
            print(STATUS_CODE[256])
            self.send_response(256)

    def _put(self,data):
        if data.get("file_name"):
            file_name = data.get("file_name")
            self.send_response(258)
        else:
            print(STATUS_CODE[255])
            self.send_response(255)
            return
        print(file_name)
        file_abs_path = "%s/%s" % (self.user_home, os.path.basename(file_name))
        received_size = 0
        file_size = data["file_size"]
        file_hd = open(file_abs_path,'wb')
        while received_size < file_size:
            data = self.request.recv(4096)
            file_hd.write(data)
            received_size += len(data)
        else:
            file_hd.close()
            print("File is all received.")

    def _ls(self,data):  # 只支持linux
        cmd = data["action"]+" "+data.get("args")
        cmd_res = os.popen("cd "+self.user_home+" && "+cmd).read()
        if len(cmd_res) == 0:
            self.send_response(260)
        else:
            msg_size = len(cmd_res)
            self.send_response(259,data={"msg_size":msg_size})
            self.request.recv(1)
            self.request.sendall(cmd_res.encode())
