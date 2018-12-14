#_*_coding:utf-8_*_
#__author__: Zhang Qing

import sys,os
import socketserver

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.ftp_server import FTPHandler
from conf import settings

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler)
    server.serve_forever()