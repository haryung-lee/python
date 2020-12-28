# 백준 4673 셀프 넘버

selfArr = [i for i in range(1, 10001)]     # 1 ~ 10000

# selfNumber 아닌 것들 return 해주는 함수
def nonSelfNum(num):
    sum = num
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum

for i in selfArr:
    tmp = i     # 여기서 selfArr의 첫번째 수는 무조건 셀프넘버 !
    tmp = nonSelfNum(tmp)
    while tmp <= selfArr[-1]:
        if tmp in selfArr:
            selfArr.remove(tmp)
        tmp = nonSelfNum(tmp)

for i in selfArr:
    print(i)
