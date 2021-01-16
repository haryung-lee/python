# 1094 - 막대기

X = int(input())

lstRod = [64]
sumOfRod = 0
tmp = 0

if X == 64:
    print(1)
    exit()

while sum(lstRod) > X:
    # min 값은 항상 마지막 원소!
    minOfRod = lstRod.pop()
    # 어차피 주어진 조건 안에서는 무조건 짝수여서 /= 로 해도 항상 정수형임
    minOfRod /= 2

    if (sumOfRod + minOfRod) == X:
        tmp += 1
        print(tmp)
        exit()
    elif (sumOfRod + minOfRod) < X:
        tmp += 1
        sumOfRod += minOfRod

    for i in range(2):
        lstRod.append(minOfRod)
        # 절반 자른게 X보다 크거나 같으면 루프에서 바로 빠져나오자!
        if minOfRod >= X:
            break


