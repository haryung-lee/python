# 1011 - Fly me to the Alpha Centauri
import math

n = int(input())

def calCount(dis):
    a = math.ceil((math.sqrt(dis)))
    if dis > a ** 2 - a : return 2 * a - 1
    else: return 2 * a - 2

for i in range(n):
    a, b = map(int, input().split())
    if b - a > 3: print(calCount(b - a))
    else: print(b - a)
