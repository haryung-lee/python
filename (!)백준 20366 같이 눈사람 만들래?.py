# 20366 - 같이 눈사람 만들래?

# 각 눈덩이의 차이 또한 최소가 되어야 함
# 첫 번째 눈덩이 두 개를 고를 때, 차이가 제일 적은 것 선택
# 두 번째도 똑같이 반복

import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
snow_1 = 0
snow_2 = 0
arr.sort()
diff = {0 : arr[0]}

for i in range(1, n):
    diff[i] = arr[i] - arr[i - 1]
    # diff.append(arr[i] - arr[i - 1])

min_idx = diff.items(min(diff.values()))
snow_1 = arr[min_idx] + arr[min_idx - 1]
del(diff[min_idx], diff[min_idx - 1])

min_idx = diff.items(min(diff.values()))
snow_2 = arr[min_idx] + arr[min_idx - 1]





