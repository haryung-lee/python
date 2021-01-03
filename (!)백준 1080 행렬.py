# 1080 - 행열

row, columns = map(int, input().split())

lst1 = [list((map(int, input()))) for j in range(row)]
lst2 = [list((map(int, input()))) for j in range(row)]

# 2차원 리스트
set = [[lst1[j][i] == lst2[j][i] for i in range(columns)] for j in range(row)]

n = set[0].count(False)

sum = 0
if n == columns or n == 0:
    if n == columns:
        sum += 1
    for i in range(1, row):
        tmp = set[i].count(False)
        if tmp != 0 and tmp != columns:
            print(-1)
            exit()
        elif tmp == columns:
            sum += 1
elif n > 0:
    sum += set[0].count(False)
    for i in range(1, row):
        if set[0] != set[i]:
            print(-1)
            exit()

print(sum)