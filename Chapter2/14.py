# coding: UTF-8
f = open('hightemp.txt')
line = f.readline()
n = int(raw_input())
while n:
    print line.replace('\n', '')
    line = f.readline()
    n -= 1
