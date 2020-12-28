# 백준 4673 셀프 넘버 - 2

selfArr = [i for i in range(1, 10001)]  # 1 ~ 10000
nonSelfArr = [True for i in range(10000)]


# selfNumber 아닌 것들 return 해주는 함수
def nonSelfNum(num):
    sum_ = num
    while num != 0:
        sum_ += num % 10
        num = num // 10  # num /= 10 으로 하면 double형으로 됨
    return sum_


for i in range(1, 10000):
    tmp = i  # 여기서 selfArr의 첫번째 수는 무조건 셀프넘버 !
    tmp = nonSelfNum(tmp)
    if tmp <= 10000:
        nonSelfArr[tmp - 1] = False

for i in range(10000):
    if nonSelfArr[i]:
        print(selfArr[i])