# 1059 - 좋은 구간

n = int(input())

# index = 0에 0 입력 -> target이 첫번째로 입력받는 수 보다 작을 경우 대비!
lst = [0] + list(map(int, input().split()))
target = int(input())

# 리스트 미리 정렬해주기
lst.sort()


preIdx = 0
nextIdx = n

for i in range(1, n + 1):
    # list 안에 target이 있으면 만들 수 있는건 제로!
    if lst[i] == target:
        print(0)
        exit()
    elif lst[i] > target:
        nextIdx = i
        preIdx = i - 1
        break

sum = 0

for i in range(lst[preIdx] + 1, target + 1):
    for j in range(target, lst[nextIdx]):
        # [a, b] 에서 a랑 b가 같으면 안됨
        if i != j:
            sum += 1

print(sum)
