# coding: UTF-8
import sys
import codecs
import json
sys.stdout = codecs.lookup('utf-8')[-1](sys.stdout)

f_r = open('jawiki-country.json', 'r')
f_w = open('jawiki-country-20.json', 'w')
f_w = codecs.lookup('utf-8')[-1](f_w)
for line in f_r:
    jsonData = json.loads(line)
    if jsonData['title'] == u'イギリス':
        f_w.write(jsonData['text'])
