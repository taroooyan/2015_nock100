# coding: UTF-8
f = open('hightemp.txt')
line = f.readline()
s = set()
while line:
    s.add(line.split()[0])
    line = f.readline()
for data in s:
    print data
