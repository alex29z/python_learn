#!/usr/bin/pyton3

def modify_list(l):
    m = [i for i in l if i % 2 == 0]
    l.clear()
    for i in range(len(m)) :
        l.append(int(m[i] / 2))
        

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst) 
