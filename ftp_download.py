#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
FTP常用操作
"""
from ftplib import FTP
import os
from flask import Flask

# 实例化，可视为固定格式
app = Flask(__name__)


class FTP_OP(object):
    def __init__(self, host, username, password, port):
        """
        初始化ftp
      :param host: ftp主机ip
      :param username: ftp用户名
      :param password: ftp密码
      :param port: ftp端口 （默认21）
      """
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def ftp_connect(self):
        """
        连接ftp
        :return:
        """
        ftp = FTP()
        ftp.set_debuglevel(1)  # 不开启调试模式
        ftp.connect(host=self.host, port=self.port)  # 连接ftp
        ftp.login(self.username, self.password)  # 登录ftp
        ftp.set_pasv(False)  ##ftp有主动 被动模式 需要调整
        return ftp

    def download_file(self, ftp_file_path, dst_file_path):
        """
        从ftp下载文件到本地
        :param ftp_file_path: ftp下载文件路径
        :param dst_file_path: 本地存放路径
        :return:
        """
        buffer_size = 102400  # 默认是8192
        ftp = self.ftp_connect()
        print(ftp.getwelcome())  # 显示登录ftp信息
        file_list = ftp.nlst(ftp_file_path)
        for file_name in file_list:
            print('file_name' + file_name)
            ftp_file = os.path.join(ftp_file_path, file_name)
            print('ftp_file:' + ftp_file)
            # write_file = os.path.join(dst_file_path, file_name)
            write_file = dst_file_path + file_name  ##在这里如果使用os.path.join 进行拼接的话 会丢失dst_file_path路径,与上面的拼接路径不一样
            print('write_file' + write_file)
            if file_name.find('.txt') > -1 and not os.path.exists(write_file):
                print('file_name:' + file_name)
                # ftp_file = os.path.join(ftp_file_path, file_name)
                # write_file = os.path.join(dst_file_path, file_name)
                with open(write_file, 'wb') as f:
                    ftp.retrbinary('RETR %s' % ftp_file, f.write, buffer_size)
                    # f.close()
        ftp.quit()
        return '下载成功!'


@app.route('/d')
def run():
    return ftp.download_file(ftp_file_path=ftp_file_path, dst_file_path=dst_file_path)


if __name__ == '__main__':
    host = "127.0.0.1"
    username = "cl"
    password = "12345678"
    port = 21
    ftp_file_path = "/speech2text/"  # FTP目录
    dst_file_path = "/test/"  # 本地目录

    ftp = FTP_OP(host=host, username=username, password=password, port=port)
    # ftp.download_file(ftp_file_path=ftp_file_path, dst_file_path=dst_file_path)
    app.run(host='0.0.0.0', port=5000)

# ftp://bigrecord:bigrecord123@192.168.1.67/2017_05_22/SH-20170522-192801-015595309568-6939-8886.wav
