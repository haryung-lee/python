# 14465 - 소가 길을 건너간 이유 5

sumOfLight, sucOfLight, n = map(int, input().split())
lstOfLight = [1 for i in range(sumOfLight)]

# 고장난 신호등은 0으로
for i in range(n):
    lstOfLight[int(input()) - 1] = 0

# 첫 sucOfLight 범위에서 고장나지 않은 신호등 수
lighting = [i for i in range(sucOfLight) if lstOfLight[i] == 1]
lighting = len(lighting)
maxLighting = lighting

# 위를 풀어서 쓰면,
# lighting = 0
# for i in range(sucOfLight):
#     if lstOfLight[i] == 1:
#         lighting += 1

# 첫 묶음에서의 빠질 인덱스와 다음 묶음에서의 추가 될 인덱스
firIdx = 0
lasIdx = sucOfLight

while lasIdx < sumOfLight:
    lighting += lstOfLight[lasIdx] - lstOfLight[firIdx]
    if maxLighting < lighting:
        maxLighting = lighting
    firIdx += 1
    lasIdx += 1

print(sucOfLight - maxLighting)


