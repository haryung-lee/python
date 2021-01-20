# 2003 - 수들의 합
import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

s = e = cnt = sum = 0

for _ in range(n):
    while e < n and sum < m:
        sum += arr[e]
        e += 1
    if sum == m: cnt += 1
    while s < n and sum >= m:
        sum -= arr[s]
        s += 1
        if sum == m: cnt += 1

print(cnt)



