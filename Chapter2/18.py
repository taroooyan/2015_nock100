# coding: UTF-8
f = open('hightemp.txt')
line = f.readline()
data = dict()
while line:
    temperature = line.split()[2]
    data[line] = temperature
    line = f.readline()

# 辞書(dict型)をvalue値でソート
for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True):
    print k.rstrip()
