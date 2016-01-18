# coding: UTF-8

f = open('hightemp.txt')
i = 0
while f.readline():
    i += 1
print i
f.close()
