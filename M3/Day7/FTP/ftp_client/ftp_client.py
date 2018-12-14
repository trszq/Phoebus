#_*_coding:utf-8_*_
#__author__: Zhang Qing

import socket
import optparse
import json

STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
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
        # print(self.options,self.args)
        # print(type(self.options),type(self.args))
        # print(self.options.server)

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
        self.client=socket.socket()
        self.client.connect((self.options.server,self.options.port))

    def auth(self):
        print("Be in authentication...")
        if self.get_auth_result(self.options.username,self.options.password):
            return True
        else:
            retry_count = 0
            while retry_count <3:
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
        self.client.send(json.dumps(data).encode())
        response=self.get_response()
        if response.get("status_code") == 254:
            print(STATUS_CODE[254])
            self.user=username
            return True
        else:
            print(response.get("status_msg"))
            return False

    def get_response(self):
        data=self.client.recv(1024)
        print("Get response:",data)
        data=json.loads(data.decode())
        return data

    def interact(self):
        if self.auth():
            pass

if __name__ == "__main__":
    ftp = FTPClient()
    ftp.interact()
