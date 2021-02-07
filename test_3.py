#!/usr/bin/pyton3
with open('out.txt', 'w') as out_file, open('3.txt', 'r') as in_file:
    s = 0
    s1 = 0
    s2 = 0
    s3 = 0
    l = list()
    for line in in_file.readlines():
        m = (line.rstrip('\n').split(';'))
        s += 1
        s1 += int(m[1])
        s2 += int(m[2])
        s3 += int(m[3])
        out_file.writelines(str((int(m[1]) + int(m[2]) + int(m[3])) / 3) + '\n')
    out_file.writelines(str(s1 / s) + ' ' + str(s2 / s) + ' ' + str(s3 / s))
