import os
from flask import Response, Flask

app = Flask(__name__)


@app.route('/download/<filename>')
def uploaded_file(filename):
    def send_file():
        store_path = os.path.join('f:/speech2text', filename)
        with open(store_path, 'rb') as targetfile:
            while True:
                data = targetfile.read(1 * 1024 * 1024)  # 每次读取1MB (可用限速)
                if not data:
                    break
                yield data

    response = Response(send_file(), content_type='application/octet-stream')
    response.headers["Content-disposition"] = 'attachment; filename=%s' % filename  # 如果不加上这行代码，导致下图的问题
    return response


app.run('0.0.0.0','5000')
