# coding: UTF-8
# Python2向けのencoding wrapper (『Pythonチュートリアル第2版』p204)
import codecs
import sys
import re
sys.stdout = codecs.lookup('utf_8')[-1](sys.stdout)
f = open('jawiki-country-20.json')
p_template = re.compile("^\|(.*?) = (.*)")
p_remove_strong = re.compile('\'{2,5}')
p_remove_link1 = re.compile('(.*)\[\[(.+?\|)(.+?)\]\]')
p_remove_link2 = re.compile('\[\[(.+?)\]\]')
p_remove_weblink = re.compile('\[.*?\]')
p_remove_ref = re.compile('<.*?>')
p_remove_tmp = re.compile('{{(.*?)}}')
template_dic = dict()
for line in f:
    result_template = p_template.search(line)
    if result_template:
        rm_template = p_remove_strong.sub('', result_template.group(2).decode('utf-8'))
        rm_link = p_remove_link1.sub('\\1[[\\3]]', rm_template)
        rm_link = p_remove_link2.sub('\\1', rm_link)
        rm_weblink = p_remove_weblink.sub('', rm_link)
        rm_ref = p_remove_ref.sub('', rm_weblink)
        rm_tmp = p_remove_tmp.sub('\\1', rm_ref).split('|')[-1]
        template_dic[result_template.group(1).decode('utf-8')] = rm_tmp
