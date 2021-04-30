import os


def audio_download(documentpath):
    # os.system('wget http://192.168.8.46:5000/download/{}'.format(documentpath))
    os.system('wget http://192.168.5.204:5000/download/{}'.format(documentpath))

