# coding: UTF-8
import sys
import codecs
sys.stdout = codecs.lookup('utf-8')[-1](sys.stdout)

f = open('jawiki-country-20.json', 'r')
f = codecs.lookup('utf-8')[-1](f)
line = f.readline()
while line:
    if line.find('Category') != -1:
        print line.decode('utf-8')
    line = f.readline()
