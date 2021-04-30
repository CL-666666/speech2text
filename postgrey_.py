# 导入依赖包
# !/usr/bin/python3
# psycopg2用于在python中连接postgrey数据库
import psycopg2
# 导入音频下载模块
from auto_download import audio_download


# 取record_guid和documentpath
def get_record_guid_documentpath():
    """
    取到record_guid和documentpath
    :return: 返回由record_guid和documentpath组成的列表
    """
    # 创建连接对象
    conn = psycopg2.connect(database="elite", user="audio", password="audio@2021", host="111.198.134.218", port="18432")
    cur = conn.cursor()  # 创建指针对象
    cur.execute("select r.record_guid,r.documentpath from ext_elite6_business_result b "
                "inner join ext_elite6_record r on b.mobile=r.dnis "
                "and r.starttime > to_char(b.businsessdate::timestamp - interval '1 month','YYYY-MM-DD HH24:MI:SS')"
                " and r.starttime < b.businsessdate "
                "left join record_parse p on p.record_guid=r.record_guid "
                "and p.datasource='elite6' where p.record_guid is null limit 10")
    results = cur.fetchall()

    # 关闭连接
    conn.commit()
    cur.close()
    conn.close()
    return results


# 判断record_guid是否已在数据库中存在
def record_guid_is_repeat(record_guid):
    """
    判断record_guid是否已在数据库中存在
    :param record_guid:
    :return: bool(True or False)
    """
    # 创建连接对象
    conn = psycopg2.connect(database="test", user="postgres", password="123456", host="localhost", port="5432")
    cur = conn.cursor()  # 创建指针对象
    # 获取结果
    cur.execute('SELECT record_guid FROM record_parse')
    results = cur.fetchall()
    # 关闭连接
    conn.commit()
    cur.close()
    conn.close()
    for single_record_guid in results:
        if record_guid == single_record_guid[0]:
            return True
        else:
            return False


# 将record_guid, documentpath, datasource, parsetext插入数据库
def insert_into_record_parse(record_guid, documentpath, datasource, parsetext):
    """
    将record_guid, documentpath, datasource, parsetext插入数据库
    :param record_guid:
    :param documentpath:
    :param datasource:
    :param parsetext:
    :return:
    """
    # 创建连接对象
    conn = psycopg2.connect(database="test", user="postgres", password="123456", host="localhost", port="5432")
    cur = conn.cursor()  # 创建指针对象
    if not record_guid_is_repeat(record_guid):
        # 创建表
        # cur.execute("CREATE TABLE record_parse(record_guid varchar,documentpath varchar,datasource varchar,parsetext text);")
        # cur.execute("CREATE TABLE ftp(id integer,path varchar);")
        # cur.execute("ALTER  table ftp ADD COLUMN text varchar(255) DEFAULT null;")

        # 插入数据
        # cur.execute("alter table ftp alter  COLUMN  audio_text type text ;")
        # cur.execute("ALTER TABLE ftp RENAME text to audio_text;")
        # cur.execute("INSERT INTO ftp(id,path)VALUES(%s,%s)", (2,'ftp://127.0.0.1/speech2text/test.py'))
        # cur.execute("INSERT INTO ftp(id,path)VALUES(%s,%s)", (2,'ftp://192.168.1.67/2017_05_22/SH-20170522-192801-015595309568-6939-8886.wav'))
        # cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (2, 'Taxol', 'F'))
        cur.execute("INSERT INTO record_parse(record_guid,documentpath,datasource,parsetext)VALUES(%s,%s,%s,%s)",
                    (record_guid, documentpath, datasource, parsetext))

        # 获取结果
        cur.execute('SELECT * FROM record_parse')
        results = cur.fetchall()

        # 关闭连接
        conn.commit()
        cur.close()
        conn.close()
        return results
    else:
        print('数据已存在!')


# 读取音频转化之后的文本
def read_audio_text(file_path):
    """
    读取音频转化之后的文本
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as f:
        result = f.read()
    return result


# aa50cb68-81c2-4743-b533-0689342b5922	ftp://192.168.1.67/2021_04_09/SH-20210409-180036-013830406589-6978-8849.wav
# fun()


# print(get_record_guid_documentpath())

record_guid_documentpath_list = [('b77f7a40-3b12-4c0d-8eb7-9bd040006bc6',
                                  'ftp://192.168.1.67/2020_11_16/SH-20201116-161100-05588816627-6928-8890.wav'),
                                 ('36e4e1ff-c43c-4b9d-ba53-c36d51151b44',
                                  'ftp://192.168.1.67/2020_11_16/SH-20201116-193038-05588816627-6927-8899.wav'),
                                 ('4822e5dc-75cb-4a45-9641-40a4bd8e248d',
                                  'ftp://192.168.1.67/2020_11_17/SH-20201117-113259-015904525775-6919-8865.wav'),
                                 ('9ffc2e10-e558-4dc8-b525-7603c0c6936c',
                                  'ftp://192.168.1.67/2020_11_17/SH-20201117-115539-018942982799-6941-8867.wav'),
                                 ('e60d120b-3135-4e67-8f57-913fb2477abb',
                                  'ftp://192.168.1.67/2020_11_18/SH-20201118-102418-013995140180-6917-8853.wav'),
                                 ('d0e2c577-aa9d-4322-b912-4bd2a0c414f3',
                                  'ftp://192.168.1.67/2020_11_18/SH-20201118-110740-013899591835-6928-8890.wav'),
                                 ('1ff87276-2c71-4297-a64d-0a13f36ae377',
                                  'ftp://192.168.1.67/2020_11_18/SH-20201118-110635-013826384826-6927-8899.wav'),
                                 ('fd502742-0eb4-45a2-b8f1-503425d612e1',
                                  'ftp://192.168.1.67/2020_11_18/SH-20201118-111826-09918810288-6939-8893.wav'),
                                 ('9b12da60-2b69-42e8-af65-cacb21df394f',
                                  'ftp://192.168.1.67/2020_11_18/SH-20201118-112945-09918810288-6939-8893.wav'),
                                 ('18e8644c-8b9f-4f35-893e-b75b88347d84',
                                  'ftp://192.168.1.67/2020_11_13/SH-20201113-195855-013999967670-6939-8893.wav')]
# print(insert_into_record_parse('b77f7a40-3b12-4c0d-8eb7-9bd040006bc6',
#                                'ftp://192.168.1.67/2020_11_16/SH-20201116-161100-05588816627-6928-8890.wav',
#                                'elite6', """
# 谢谢
# 喂你好
# ，艾先生，您好，我这边呢是集邮客服中心的，今天冒昧给您致电，主要是将最新的油品发新消息通知到您
# ，就是在今年这个特殊的历史背景下吗，推出一款特殊版式的毛主席大邮票
# ，这个是选用各个历史时期毛主席的一些标准上和经典
# ，就像现在我们比较熟悉的就是第5套人民币上的主席标准像
# ，和目前天安门城楼悬挂的主席画像，以及像开国大典上毛主席的经典像这些
# ，而且都是配有主席最具有代表性的题词手迹
# ，也是全面的展现了伟人领袖这一生的光辉历程和不同时期的一个卓越风采，用这种画框的形式去呈现，也是打破了常规邮票的一个收藏形式
# ，整体呢非常的精美大气
# ，所以像它这个不仅仅是一款高价的
# 。
# 使得一个收藏品也是一款高端的装饰画
# ，因为现在全国总共是发行了1万套吗，现在呢，针对通知到的一部分用户可以提前了解和征订的
# ，不知道这个发消息就最近您那边有关注到了吗
# ？还没有注意到这个消息是吧
# ？没有
# ，那这次呢就是建议您一定要重点注意一下，因为这次因为今年赶上这种特殊的历史时期吗，用这种特别的一个形式来致敬伟人缅怀伟人
# ，这次呢产品就是融入了一个伟人风采邮票价值和书法艺术在里面
# ，发行是要区别于普通的版张邮票是连那个大半年册语都没有的
# ，所以像这次呢也是给您去通，知道这个消息就见您呢，一定要重点去关注与了解一下吧
# ，那行那
# 。
# 说呢，就是把这个消息给您重点说一下，您可以再去了解关注一下
# ，那行那这边呢，就给您说这么多，就先不打扰您了
# ，嗯，嗯嗯，好您先忙
# ，嗯嗯，好再见
# 嗯
# 。"""))
# print(record_guid_is_repeat('b77f7a40-3b12-4c0d-8eb7-9bd040006bc6'))
# s = [('b77f7a40-3b12-4c0d-8eb7-9bd040006bc6',)]
# for i in s:
#     print(('b77f7a40-3b12-4c0d-8eb7-9bd040006bc6' == i[0]))
# for documentpath in record_guid_documentpath_list:
#     audio_download(documentpath[1])
test_audio_pcm_list = [(1, r'ftp://127.0.0.1/speech2text/speech2text/out/audio00.pcm'),
                       (2, r'ftp://127.0.0.1/speech2text/speech2text/out/audio01.pcm'),
                       (3, r'ftp://127.0.0.1/speech2text/speech2text/out/audio02.pcm'),
                       ]

# for documentpath in test_audio_pcm_list:
#     audio_download(documentpath[1])
# print(get_record_guid_documentpath())
