from flask import send_file, send_from_directory, Flask
import os

app = Flask(__name__)

current_path = os.getcwd()
print(current_path)


@app.route('/download/<filename>')
def copy(filename):
    fr = open(filename, 'rb')  # 要拷贝的文件
    # local_path = 'f:/speech2text/kafka_simulate/'
    local_path = os.path.abspath(filename)
    # print(local_path)
    # new_file = 'f:/speech2text/kafka_simulate/' + filename.split('/')[-1]
    new_file = current_path + '/' + filename.split('/')[-1]
    # print(new_file)
    fw = open(new_file, 'wb')  # 新文件
    # 循环读取 写入
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()
    # send_from_directory(local_path, filename=new_file, as_attachment=True)


app.run()
