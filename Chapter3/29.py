# coding: UTF-8
# Python2向けのencoding wrapper (『Pythonチュートリアル第2版』p204)
import codecs
import sys
import re
import urllib2
import json
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
baseurl = 'https://commons.wikimedia.org/w/api.php'
parameta = '?action=query&prop=imageinfo&iiprop=url&format=json'
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
filename =\
        "&titles=File:"+template_dic[u'国旗画像'].replace(' ', '%20')
url = "%s%s%s" % (baseurl, parameta, filename)
response = urllib2.urlopen(url)
response = json.loads(response.read())['query']['pages']['347935']['imageinfo']
imageurl = response[0]['url']
print imageurl
