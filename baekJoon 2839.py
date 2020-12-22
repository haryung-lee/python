import sys
n = int(input())

maxI = int(n / 5)

for i in range(maxI, -1, -1):
    if (n - i * 5) % 3 == 0:
        print(i + int((n - i * 5) / 3))
        sys.exit()
print(-1)
