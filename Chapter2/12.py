# coding: UTF-8
f_r = open('hightemp.txt')
f1_w = open('col1.txt', 'w')
f2_w = open('col2.txt', 'w')
line = f_r.readline()
while line:
    f1_w.write(line.split("\t")[0]+"\n")
    f2_w.write(line.split("\t")[1]+"\n")
    line = f_r.readline()
f1_w.close()
f2_w.close()
