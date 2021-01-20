# 1644 - 소수의 연속합

# 소수 배열 만들기
n = int(input())
# index 0, 1은 소수가 아님
lst = [False, False] + [True] * (n - 1)
prime = []

for i in range(2, n + 1):
    if lst[i]:
        prime.append(i)
        for j in range(i * 2, n + 1, i):
            lst[j] = False

# 투 포인터 사용
s = 0
e = -1
sum = 0
cnt = 0

for i in range(len(prime)):
    if sum == n: cnt += 1
    while sum < n:
        if e == len(prime) - 1: break
        if sum + prime[e + 1] > n: break
        e += 1
        sum += prime[e]
    if sum == n: cnt += 1
    sum -= prime[s]
    s += 1

print(cnt)
