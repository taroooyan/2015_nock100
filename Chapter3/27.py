# coding: UTF-8
# Python2向けのencoding wrapper (『Pythonチュートリアル第2版』p204)
import codecs
import sys
import re
sys.stdout = codecs.lookup('utf_8')[-1](sys.stdout)
f = open('jawiki-country-20.json')
p_template = re.compile("^\|(.*?) = (.*)")
p_remove_strong = re.compile('\'{2,5}')
p_remove_link = re.compile('\[\[(.+\|)*?(.*?)\]\]')
template_dic = dict()
for line in f:
    result_template = p_template.search(line)
    if result_template:
        template_dic[result_template.group(1).decode('utf-8')] =\
        p_remove_link.sub('\\2', p_remove_strong.sub('', result_template.group(2).decode('utf-8')))
for key, value in template_dic.items():
    print key, " => ", value
