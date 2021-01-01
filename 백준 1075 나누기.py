# 1075 - 나누기
# 두 정수 입력받기
n = int(input())
f = int(input())

# n의 마지막 두 자릿수
n2 = 0
tmpN = n
for i in range(2):
    n2 += (tmpN % 10) * (10 ** i)
    tmpN = tmpN // 10

# n의 마지막 두 자릿수가 n % f 보다 작으면 더해줘야 함
# 새로운 n 탄생
if n2 >= n % f:
    n -= (n % f)
else:
    n += f - (n % f)

# 새로운 n의 마지막 두 자릿수 구하기
n2 = 0
for i in range(2):
    n2 += (n % 10) * (10 ** i)
    n = n // 10

if n2 % f < 10:
    print(0, n2 % f, sep = '')
else:
    print(n2 % f)