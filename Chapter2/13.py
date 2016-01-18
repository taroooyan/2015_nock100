# coding: UTF-8
f1_r = open('col1.txt')
f2_r = open('col2.txt')
f_w = open('paste.txt', 'w')
f1_line = f1_r.readline()
f2_line = f2_r.readline()
while f1_line and f2_line:
    f_w.write("%s\t%s\n" % (f1_line.strip(), f2_line.strip()))
    f1_line = f1_r.readline()
    f2_line = f2_r.readline()
f1_r.close()
f2_r.close()
