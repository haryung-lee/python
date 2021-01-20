# 2075 - N번째 큰 수
import sys
n = int(input())
ans = []
for i in range(1, n + 1):
    ans += list(map(int, sys.stdin.readline().split()))
    ans = sorted(ans)[-n:]

print(ans[-n])
