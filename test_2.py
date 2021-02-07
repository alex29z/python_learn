#!/usr/bin/pyton3

def key_list(l):
    m = list()
    for i in l:
        if i not in m :
            m.append(i)
    key = list()
    key.append(m[0])
    for i in range(1, len(m)) :
        flag = True
        for j in range(len(key)) :
            if m[i].lower() == key[j].lower() :
                flag = False
                break
        if flag :
            key.append(m[i])
    return key

def dic(key, list) :
    dict = {}
    for i in range(len(key)):
        count = 0
        for j in range(len(list)):
            if key[i].lower() == list[j].lower() :
                count += 1
        dict.update({key[i]:count})
    return dict

with open('1234.txt', 'r') as f:
    l = f.read().split()
v = (list(dic(key_list(l), l).keys())[list(dic(key_list(l), l).values()).index(max(list(dic(key_list(l), l).values())))])
print(v, (dic(key_list(l), l).get(v)))
