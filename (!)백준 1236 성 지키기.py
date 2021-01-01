# 1236 - 성 지키기
import sys
w, h = map(int, input().split())

numW = []
numH = []
user = []

for i in range(h):
    user.append(sys.stdin.readline())

for i in range(w):
    numW.append('X' not in user[i])
for j in range(h):
    numH.append('X' not in user[i][j] for i in range(w))

print(sum(numW))
print(sum(numH))



