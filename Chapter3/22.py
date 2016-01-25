# coding: UTF-8
import sys
import codecs
import re
sys.stdout = codecs.lookup('utf-8')[-1](sys.stdout)

f = open('jawiki-country-20.json', 'r')
f = codecs.lookup('utf-8')[-1](f)
p = re.compile("\[\[Category:(.*)\]\]")
line = f.readline()
while line:
    result = p.search(line)
    if result:
        print result.group(1).decode('utf-8')
    line = f.readline()
