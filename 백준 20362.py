# 20362 - 유니대전 퀴즈쇼

import sys
n, winner = sys.stdin.readline().split()
n = int(n)

player = {}

for i in range(n):
    name, chat = sys.stdin.readline().split()
    if name == winner:
        answer = chat
        break
    player[name] = chat

mis = 0
keyList = player.values()

for i in keyList:
    if i == answer:
        mis += 1
print(mis)