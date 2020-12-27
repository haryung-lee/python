import sys

numOfCup, target, n = map(int, sys.stdin.readline().split())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a == target:
        target = b
    elif b == target:
        target = a
print(target)