#_*_coding:utf-8_*_
#__author__: Zhang Qing

import socket
import optparse
import json
import os

STATUS_CODE = {
    250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251: "Invalid cmd ",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
    255: "Filename is not provided",
    256: "File doesn't exist"
}

class FTPClient(object):
    def __init__(self):
        parser=optparse.OptionParser()
        parser.add_option("-s","--server",dest="server",help="ftp server IP")
        parser.add_option("-P","--port",type="int",dest="port",help="ftp server port")
        parser.add_option("-u","--user",dest="username",help="username")
        parser.add_option("-p","--password",dest="password",help="password")
        self.options, self.args = parser.parse_args()
        self.verify_args()
        self.make_connection()


    def verify_args(self):
        if not (self.options.username and self.options.password):
            exit("ERROR: Please provide the username and password together.")

        if self.options.server and self.options.port:
            if self.options.port > 0 and self.options.port < 65535:
                return True
            else:
                exit("ERROR: Host port must be in 0-65535.")
        else:
            exit("ERROR: Please provide the server IP address and service port.")

    def make_connection(self):
        self.sock=socket.socket()
        self.sock.connect((self.options.server,self.options.port))

    def auth(self):
        print("Be in authentication...")
        if self.get_auth_result(self.options.username,self.options.password):
            return True
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username:").strip()
                password = input("password:").strip()
                if self.get_auth_result(username,password):
                    return True
                else:
                    retry_count += 1
            else:
                exit("Authentication is failed.")

    def get_auth_result(self,username,password):
        data={
            "action": "auth",
            "username": username,
            "password": password
        }
        self.sock.send(json.dumps(data).encode())
        response=self.get_response()
        if response.get("status_code") == 254:
            print(STATUS_CODE[254])
            self.user=username
            return True
        else:
            print(response.get("status_msg"))
            return False

    def get_response(self):
        data=self.sock.recv(1024)
        print("Get response:",data)
        data=json.loads(data.decode())
        return data

    def _get(self,cmd):
        if len(cmd) == 1:
            print(STATUS_CODE[255])
            return
        req={
            "action": cmd[0],
            "file_name": cmd[1]
        }
        self.sock.send(json.dumps(req).encode())
        response=self.get_response()
        if response["status_code"] == 257:
            print(response["status_msg"])
            self.sock.send(b'1')
            file_size = response["file_size"]
            received_size=0
            # base_filename=cmd[1].split('/')[-1]
            base_filename=os.path.basename(cmd[1])
            print(base_filename)
            file_hd=open(base_filename,'wb')
            while received_size < file_size:
                data=self.sock.recv(4096)
                file_hd.write(data)
                received_size += len(data)
            else:
                file_hd.close()
                print("File is all received.")
        else:
            print("%s: %s"%(response["status_code"],response["status_msg"]))

    def _put(self,cmd):
        if len(cmd) == 1:
            print(STATUS_CODE[255])
            return

        if os.path.isfile(cmd[1]):
            file_size = os.path.getsize(cmd[1])
            req = {
                "action": cmd[0],
                "file_name": cmd[1],
                "file_size": file_size
            }
            self.sock.send(json.dumps(req).encode())
            response = self.get_response()
            if response["status_code"] == 258:
                print(response["status_msg"])
                file_hd = open(req["file_name"],'rb')
                for line in file_hd:
                    self.sock.send(line)
                else:
                    file_hd.close()
                    print("File sending is done.")
            else:
                print("%s: %s"%(response["status_code"],response["status_msg"]))
        else:
            print(STATUS_CODE[256])

    def _ls(self,cmd):  # 只支持linux
        req = {
            "action": cmd[0],
            "args": " ".join(cmd[1:])
        }
        self.sock.send(json.dumps(req).encode())
        response=self.get_response()
        if response["status_code"] == 259:
            self.sock.send(b'1')
            msg_size = response["msg_size"]
            received_size = 0
            received_data = b''
            while received_size < msg_size:
                data = self.sock.recv(1024)
                received_data += data
                received_size += len(data)
            else:
                print(received_data.decode())
        else:
            print("%s: %s" % (response["status_code"], response["status_msg"]))

    def interact(self):
        if self.auth():
            while True:
                cmd = input(">>:").strip()
                if len(cmd) == 0:
                    continue
                cmd_list = cmd.split()
                if cmd_list[0] == "exit":
                    break
                elif hasattr(self, "_%s"%cmd_list[0]):
                    func = getattr(self, "_%s"%cmd_list[0])
                    func(cmd_list)
                else:
                    print(STATUS_CODE[251])
        self.sock.close()


if __name__ == "__main__":
    ftp = FTPClient()
    ftp.interact()
