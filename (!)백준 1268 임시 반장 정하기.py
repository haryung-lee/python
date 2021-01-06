# 1268 - 임시 반장 정하기

# 아이들 수
n = int(input())
lstClass = [list(map(int, input().split())) for i in range(n)]
ans = [0 for i in range(n)]

for i in range(n):
    # 0반부터 8반
    num = [[] for i in range(9)]
    for j in range(n):
        # j번째 학생을 i 학년 j 반에 append함
        # 사용자가 입력했을 땐 1반부터 9반이므로, -1 해줘야 함
        num[lstClass[j][i] - 1].append(j)
    for j in range(9):
        # j반에 2명 이상 있을 경우, ans 해당 학생 index에 +1 해줌
        if len(num[j]) > 1:
            for k in num[j]:
                ans[k] += 1

mIdx = 0
for i in range(1, n):
    if ans[mIdx] < ans[i]:
        mIdx = i
print(mIdx + 1)