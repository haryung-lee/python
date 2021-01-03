# 1475 - 방 번호

n = int(input())
set = [0 for i in range(9)]
if n == 0:
    set[0] += 1
while n > 0:
    if n % 10 == 9:
        set[6] += 1
    else:
        set[n % 10] += 1
    n = n // 10

set[6] = (set[6] // 2) + (set[6] % 2)

print(max(set[0:9]))

