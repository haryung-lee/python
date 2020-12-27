import sys
n, tOfWalk = map(int, sys.stdin.readline().split())
posX = 0
posY = 0

dirX = 1
dirY = 0

turnOfDir = 1

t = 0

for i in range(n):
    tOfTurn, dir = input().split()
    tOfTurn = int(tOfTurn)
    temp = tOfTurn
    tOfTurn -= t
    t = temp
    posX += dirX * tOfTurn
    posY += dirY * tOfTurn
    if turnOfDir == 1:
        if dir == 'left':
            dirY += dirX
        elif dir == 'right':
            dirY -= dirX
        dirX = 0
    elif turnOfDir == -1:
        if dir == 'left':
            dirX -= dirY
        elif dir == 'right':
            dirX += dirY
        dirY = 0
    turnOfDir *= -1

tOfTurn = tOfWalk
tOfTurn -= t

posX += dirX * tOfTurn
posY += dirY * tOfTurn
print(posX, posY)
