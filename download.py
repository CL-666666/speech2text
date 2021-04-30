from flask import send_file, send_from_directory, Flask
import os

app = Flask(__name__)


@app.route("/download/<filename>")
def download(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名
    local_path = 'f:/speech2text/test'
    # filename = filename.split('/')[-1]
    return send_from_directory(app.config[local_path], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
