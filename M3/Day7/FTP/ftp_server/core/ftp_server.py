#_*_coding:utf-8_*_
#__author__: Zhang Qing

import socketserver
import json
import configparser
from conf import settings

STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",
}

class FTPHandler(socketserver.BaseRequestHandler):
    def handler(self):
        while True:
            self.data=self.request.recv(1024).strip()
            print(data)
            data=json.loads(self.data.decode())
            if self.data is None:
                print("client is closed.")
                break
            if data.get("action"):
                if hasattr(self,data.get("action")):
                    func=getattr(self,data.get("action"))
                    print(func)
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

    def auth(self,data):
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        username = data.get("username")
        password = data.get("password")
        if username:
            if username in config.sections():
                if password == config[username]["password"]:
                    print(STATUS_CODE[254])
                    self.send_response(254)
                else:
                    print(STATUS_CODE[253])
                    self.send_response(253)
            else:
                print(STATUS_CODE[253])
                self.send_response(253)
        else:
            print(STATUS_CODE[252])
            self.send_response(252)
