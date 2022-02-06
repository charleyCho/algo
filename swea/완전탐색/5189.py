# D3
# 전자카트

def solve(cur, cnt, tmp):
    global min_battery
    if tmp >= min_battery:
        return

    if cnt == N-1:
        tmp += arr[cur][0]
        if tmp < min_battery:
            min_battery = tmp
        return

    for next in range(1, N):
        if not visited[next]:
            visited[next] = 1
            solve(next, cnt+1, tmp+arr[cur][next])
            visited[next] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    min_battery = 10*100
    solve(0, 0, 0)
    print('#{} {}'.format(tc, min_battery))
