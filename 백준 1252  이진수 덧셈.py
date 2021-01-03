# 1252 - 이진수 덧셈
n = input().split()

# 2진수 문자열을 정수로 바꿔줌
a = int(n[0], 2)
b = int(n[1], 2)

# bin을 이용해 2진수로 바꿔줌
print(bin(a + b)[2:])



