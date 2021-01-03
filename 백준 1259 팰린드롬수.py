# 1259 - 팰린드롬수

# 우선 시작
while True:
    # 입력받기 - 리스트 형태로 저장
    n = list(map(int, input()))

    # 여기서 주의! 0 이 이나리 리스트 형태여서 [0]이여야 함
    if n == [0]:
        break
    # 입력받은 리스트 n을 거꾸로 했을때랑 n이랑 같은지 비교
    if list(reversed(n)) == n:
        print('yes')
    else:
        print('no')




