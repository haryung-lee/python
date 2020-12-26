import sys

day, night, tree = map(int, sys.stdin.readline().split())

if (tree - night) % (day - night) == 0:
    print(int((tree - night) / (day - night)))
else:
    print(int((tree - night) / (day - night)) + 1)
