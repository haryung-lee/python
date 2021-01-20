# 6064 - 카잉 달력

t = int(input())

# < : > 쌍에서 왼쪽을 l, 오른쪽을 r이라고 하자

for i in range(t):
    m, n, x, y = map(int, input().split())
    l = r = ans = 0
    sum_left = m * l + x
    sum_right = n * r + y
    while True:
        if sum_left == sum_right:
            ans = sum_left
            break
        elif sum_left < sum_right:
            l += 1
            sum_left = m * l + x
        else:
            r += 1
            sum_right = n * r + y
        if sum_left > m * n: break
    if ans: print(ans)
    else: print(-1)


