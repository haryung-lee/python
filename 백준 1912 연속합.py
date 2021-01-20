# 1912 - 연속합
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# 첫번째 인덱스 우선 입력
sum = [arr[0]]

for i in range(1, n):
    # arr값을 반영해서 sum에 입력
    # sum의 이전 인덱스에서, 값이 음수라면 다음 sum에서는 반영 X
    if sum[i - 1] > 0: sum.append(sum[i - 1] + arr[i])
    else: sum.append(arr[i])
print(max(sum))