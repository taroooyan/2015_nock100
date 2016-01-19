# coding: UTF-8
import math
n = int(raw_input())
i = 0
c = 0
f_r = open('hightemp.txt')
while f_r.readline():
    c += 1
else:
    f_r.close()
f_r = open('hightemp.txt')
line = f_r.readline()
# if c isn't to divide n
flag = math.ceil(float(c)/n)
tmp = n
while line:
    name = str(tmp-n)+".txt"
    open(name, 'a').write(line)
    i += 1
    if i % flag == 0:
        n -= 1
    line = f_r.readline()
