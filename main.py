from ftp_download1 import MyFtp

from test import uploaded_file
from flask import Flask

app = Flask(__name__)


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


@app.route('/')
def run():
    local_path = 'f:/speech2text/test/'
    ftp.download_file(local_path, path, filename)
    # copy(local_path + filename)
    uploaded_file(filename)


if __name__ == '__main__':
    ftp_path = 'ftp://127.0.0.1/speech2text/requirements.txt'
    ip, path, filename = handle(ftp_path)
    print(ip, path, filename)
    ftp = MyFtp(ip)
    ftp.login('cl', '12345678')
    # run()
    app.run(host='0.0.0.0', port=5000)
    # app.run()
    ftp.close()
