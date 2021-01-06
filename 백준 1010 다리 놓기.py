# 1010 - 다리 놓기

t = int(input())
for i in range(t):
    sum = 1
    n, m = map(int, input().split())
    for j in range(n):
        sum *= (m - j)
    for j in range(n):
        sum = sum // (j + 1)
    print(sum)


