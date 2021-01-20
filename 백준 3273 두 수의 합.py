# 3273 - 두 수의 합
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
x = int(input())

arr.sort()
s = cnt = 0
e = n - 1

while s < e:
    if arr[s] + arr[e] > x:
        e -= 1
    elif arr[s] + arr[e] < x:
        s += 1
    else:
        cnt += 1
        s += 1

if n == 1:
    if arr[0] == 1: print(1)
    else: print(0)
else: print(cnt)






