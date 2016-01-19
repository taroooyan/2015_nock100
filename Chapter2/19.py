# coding: UTF-8
f = open('hightemp.txt')
line = f.readline()
data = dict()
while line:
    city = line.split()[0]
    if city in data:
        data[city] += 1
    else:
        data[city] = 1
    line = f.readline()

# 辞書(dict型)をvalue値でソート
for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True):
    print k, v
