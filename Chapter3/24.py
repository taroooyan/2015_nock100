# coding: UTF-8
import sys
import codecs
import re
sys.stdout = codecs.lookup('utf-8')[-1](sys.stdout)

f = open('jawiki-country-20.json', 'r')
f = codecs.lookup('utf-8')[-1](f)
p = re.compile("(File|ファイル)+:(.+?)\|")
line = unicode(f.readline())
while line:
    result = p.search(line)
    if result:
        print result.group(2).decode('utf-8')
    line = f.readline()
