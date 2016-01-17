# coding: UTF-8
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might \
Also Sign Peace Security Clause. Arthur King Can.".replace('.', '').split()
f1 = [1, 5, 6, 7, 8, 9, 15, 19]
f2_t = range(len(s))
f2 = list(set(f2_t)-set(f1))
string_map = {}
for f in f1:
    select_s = s[f][:1]
    string_map[select_s] = f
for f in f2:
    select_s = s[f][:2]
    string_map[select_s] = f
print string_map
