# coding: UTF-8
import sys
s = "Now I need a drink, alcoholic of course, after the heavy lectures \
involving quantum mechanics.".replace(',','').replace('.','').split()
print s
for i in range(len(s)):
    sys.stdout.write(str(len(s[i])))
