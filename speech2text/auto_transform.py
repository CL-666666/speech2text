import os

g726_file = '../speech/SH-20210409-180639-013842937141-6961-8871.wav'
wav_file = '../speech/Out_SH-20210409-180639-013842937141-6961-887101.wav'
pcm_file = '../speech/Out_SH-20210409-180639-013842937141-6961-887101.pcm'


def fun(root_file_path):
    """
    提取音频文件名(不带后缀)
    :param root_file_path:
    :return:
    """

    file_path = '/'.join(root_file_path.split('/')[:-1]) + '/'
    file_name = root_file_path.split('/')[-1].split('.')[0]
    return file_path + file_name


def g7262wav(g726_file, wav_file):
    """
    g726转wav
    :param g726_file:
    :param wav_file:
    :return:
    """
    try:
        os.system('ffmpeg -f g726 -ar 8000 -code_size 2 -i {} -acodec pcm_s16le -ar 8000 -ac 1 {}'.format(g726_file,
                                                                                                          wav_file))
    except:
        print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


def wav2pcm(wav_file, pcm_file):
    """
    wav转16k 16bit 单声道 pcm
    :param wav_file:
    :param pcm_file:
    :return:
    """
    try:
        os.system('ffmpeg -y -i {} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {}'.format(wav_file,
                                                                                         pcm_file))
        os.system(r'rm F:\speech2text\speech\Out*.wav')
    except:
        print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# def audio_split(file):
#     try:
#         os.system(
#             'ffmpeg  -i {} -segment_time 60 -c -f '
#             's16le -ar 16000 -ac 1 {}%02d.pcm'.format(file, file))
#     except:
#         print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
def audio_split(file):
    """
    切割wav音频,每段60s
    :param file:
    :return:
    """
    try:
        os.system('ffmpeg -i {} -f segment -segment_time 60 -c copy {}%02d.wav'.format(file,
                                                                                       fun(file)))
    except:
        print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


def is_g726(document_path):
    """
    对音频文件ftp路径做切分，判断是否为g726格式加密文件
    :param document_path: 音频文件ftp路径
    :return: bool(True or False)
    """
    path_list = document_path.split('/')
    special_string = path_list[2].split('.')[-1]
    if special_string in ['67', '42']:
        return True
    else:
        return False


def audio_test(audio_path):
    # os.system('./no_g726_transform.sh ../speech/Out_SH-20210409-180639-013842937141-6961-887101.wav')
    os.system('./no_g726_transform.sh {}'.format(audio_path))


# g7262wav(g726_file, wav_file)
# audio_split(wav_file)
# wav2pcm(wav_file, pcm_file)

# print(fun(pcm_file))

# print(is_g726('ftp://192.168.1.67/2021_04_09/SH-20210409-184543-013940506245-6985-8893.wav'))
# print(is_g726('ftp://192.168.1.42/2021_04_09/SH-20210409-194222-13911591732-6762-8686.wav'))

# audio_test()
# for each in os.listdir('out'):
#     print(os.path.abspath(each))
#     # print(each)
def get_file_name():
    for each in os.listdir('out'):
        yield os.path.realpath(each)
        # yield os.path.abspath(each)

# for i in get_file_name():
#     print(i)
