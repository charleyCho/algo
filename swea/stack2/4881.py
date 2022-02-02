# D2
# 최소 배열 합

def solve(idx, curr):
    global min_sum

    if curr >= min_sum:
        return

    if idx == N:
        if curr < min_sum:
            min_sum = curr

    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            solve(idx + 1, curr + arr[idx][i])
            selected[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N
    min_sum = 0
    for i in range(N):
        min_sum += arr[i][i]
    solve(0, 0)
    print('#{} {}'.format(tc, min_sum))