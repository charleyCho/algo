# D2
# 종이붙이기
# DP

def dp(num):
    if not num:
        return 0

    if num == 1:
        return 1

    if num == 2:
        return 3

    if not data[num]:
        data[num] = dp(num-1) + 2*dp(num-2)

    return data[num]


data = [0] * 31
T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    print('#{} {}'.format(tc, dp(N)))
