# D2
# 미로

def escape(r, c):
    global result

    if result:
        return

    if maze[r][c] == '3':
        result = 1
        return

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != '1':
            visited[nr][nc] = 1
            escape(nr, nc)
            visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0

    for row in range(N):
        for col in range(N):
            if maze[row][col] == '2':
                visited[row][col] = 1
                escape(row, col)

    print('#{} {}'.format(tc, result))