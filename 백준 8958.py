import sys

n = int(input())
s = [sys.stdin.readline() for i in range(n)]

for i in s:
    p = 0
    sum = 0
    for j in i:
        if j == 'X':
            p = 0
        if j == 'O':
            p += 1
            sum += p
    print(sum)


