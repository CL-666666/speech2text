# _*_ coding:utf-8 _*_
# name gefile.py
import os
import stat
import socket
import paramiko

# FILES = ["filenameA", "filenameB", "filenameC", "filenameD", "filenameE"]
FILES = ["filenameA", "filenameB", "filenameC", "filenameD", "filenameE"]
USERNAME = "cl"
PASSWORD = "12345678"
HOST = "127.0.0.1"
PORT = 21
remotefile = "/speech2text/"
localpath = r'F:\speech2text\test'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
t = paramiko.Transport(sock)
t.start_client()
t.auth_password(USERNAME, PASSWORD)
sftptest = paramiko.SFTPClient.from_transport(t)
sftptest.get(remotefile, localpath)
sftptest.close()
t.close()
sock.close()
