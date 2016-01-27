# coding: UTF-8
# Python2向けのencoding wrapper (『Pythonチュートリアル第2版』p204)
import codecs
import sys
import re
sys.stdout = codecs.lookup('utf_8')[-1](sys.stdout)
f = open('jawiki-country-20.json')
p = re.compile("^\|(.*?) = (.*)")
template_dic = dict()
for line in f:
    result = p.search(line)
    if result:
        template_dic[result.group(1).decode('utf-8')] =\
                result.group(2).decode('utf-8')
for key, value in template_dic.items():
    print key, " => ", value
