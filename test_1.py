#!/usr/bin/pyton3

def modify_str(l):
    str = ''
    for i in range(len(l)) :
        if l[i].isalpha() :
            str += " " + l[i] + " "
        else:
            str += l[i]
    return str.strip()

def decod_str(l):
    m = l.split(' ')
    for i in range(0, len(m) -1, 2):
        

with open('123.txt', 'r') as f:
    str = f.readline()
print(decod_str(modify_str(str)))
