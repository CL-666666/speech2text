import os

from flask import Flask, send_file
from ftp_download1 import MyFtp
from werkzeug.routing import BaseConverter
# from file_copy import copy
# from test import uploaded_file

app = Flask(__name__)

current_path = os.getcwd()


# 自定义类型转换器
class FTPPathConverter(BaseConverter):
    regex = "ftp.*"  # 匹配规则，不要以^开头


app.url_map.converters["ftp_path"] = FTPPathConverter  # 添加到转换器列表

def handle(root_path):
    """
    处理原始ftp路径 例：'ftp://192.168.1.67/2017_05_22/SH-20170522-192801-015595309568-6939-8886.wav'
    :param root_path: 原始ftp路径
    :return: 返回ip,ftp下载路径,文件名
    """
    path_list = root_path.split('/')  # 将原始ftp路径用'/'分割
    ip = path_list[2]
    path = '/' + '/'.join(path_list[3:-1]) + '/'
    filename = path_list[-1]
    return ip, path, filename


@app.route(rule="/download/<ftp_path:ftp_path>")  # 将参数转换成ftp_path类型
def run(ftp_path):
    print(ftp_path)
    # local_path = 'f:/speech2text/test'
    local_path = current_path
    ip, path, filename = handle(ftp_path)
    print(ip, path, filename)
    # if os.path.exists(local_path + filename):
    #     pass
    ftp = MyFtp(ip)
    ftp.login('cl', '12345678')
    ftp.download_file(local_path, path, filename)
    return send_file(local_path + '/' + filename, as_attachment=True)
    # copy(local_path + filename)
    # return uploaded_file(filename)


if __name__ == '__main__':
    #     ftp_path = 'ftp://127.0.0.1/speech2text/requirements.txt'
    #     ip, path, filename = handle(ftp_path)
    #     print(ip, path, filename)
    #     ftp = MyFtp(ip)
    #     ftp.login('cl', '12345678')
    app.run(host='0.0.0.0', port=5000, debug=True)
    #     # app.run()
    #     # run()
    #     ftp.close()
