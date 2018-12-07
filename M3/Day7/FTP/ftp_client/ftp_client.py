#_*_coding:utf-8_*_
#__author__: Zhang Qing

import socket
import optparse

class FTPClient(object):
    def __init__(self):
        parser=optparse.OptionParser()
        parser.add_option("-s","--server",dest="server",help="ftp server IP")
        parser.add_option("-P","--port",type="int",dest="port",help="ftp server port")
        parser.add_option("-u","--user",dest="username",help="username")
        parser.add_option("-p","--password",dest="password",help="password")
        self.options, self.args = parser.parse_args()

if __name__ == "__main__":
    ftp = FTPClient()