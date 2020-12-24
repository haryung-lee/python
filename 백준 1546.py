import sys
n = int(input())
s = list(map(int, sys.stdin.readline().split()))

maxI = max(s)
sum = 0
for i in s:
    sum += i / maxI * 100
print(sum / n)



