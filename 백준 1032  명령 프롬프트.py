# 1032 - 명령 프롬프

n = int(input())
user = list(input()) # 문자열 리스트 n개 줄로 입력받기

for i in range(n-1):
    tmp = list(input())
    for j in range(len(user)):
        if user[j] != tmp[j]:
            user[j] = '?'

print("".join(user))
