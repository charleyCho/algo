# D3
# 최소합

def solve(cr, cc, tmp):
    global result
    if tmp >= result:
        return

    if cr == N-1 and cc == N-1:
        if tmp < result:
            result = tmp
        return

    for dr, dc in [(1, 0), (0, 1)]:
        nr, nc = cr+dr, cc+dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = 1
            solve(nr, nc, tmp+arr[nr][nc])
            visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 13*13*10
    solve(0, 0, arr[0][0])
    print('#{} {}'.format(tc, result))