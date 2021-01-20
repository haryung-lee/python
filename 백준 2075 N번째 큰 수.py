# 2075 - N번째 큰 수

import sys

n = int(input())
arr = [(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
data = enumerate(arr[i] for i in range(n))
print(type(data))
sol = []
max_idx = [n - 1] * n # 현재
i = n - 1
while n > 0:
    # max_idx[data[i].get]
    sol.append(max(arr[i]))
    n -= 1
    max_idx