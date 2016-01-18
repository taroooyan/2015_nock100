# coding: UTF-8
f = open('hightemp.txt')
lines = f.readlines()
f.close()
n = int(raw_input())
for line in lines[-n::]:
    print line.strip()
    n -= 1
    if n == 0:
        break
