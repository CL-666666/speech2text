# coding=gbk
import json

li = [{'N': '������'}]
# print(li[0]['N'])
print(json.dumps(li, ensure_ascii=False))
