# 15565 - 귀여운 라이언
import sys
from collections import deque

n, k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

que = deque([])
s = 0
e = 0
min_len = n + 1
cnt = 0

for i in range(n):
    while e < n and cnt < k:
        que.append(arr[e])
        if arr[e] == 1:
            cnt += 1
        e += 1
    if cnt == k:
        min_len = min(min_len, len(que))
        if arr[s] == 1: cnt -= 1
        que.popleft()
        s += 1

if min_len > n:
    print(-1)
else:
    print(min_len)
