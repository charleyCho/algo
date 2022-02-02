# D3
# 미로의 거리

def escape(cr, cc, cnt):
    global result
    if cnt >= result:
        return

    if maze[cr][cc] == '3':
        if cnt < result:
            result = cnt
        return

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != '1':
            visited[nr][nc] = 1
            escape(nr, nc, cnt + 1)
            visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = N*N

    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                visited[r][c] = 1
                escape(r, c, 0)

    if result == N*N:
        result = 0
    else:
        result -= 1
    print('#{} {}'.format(tc, result))