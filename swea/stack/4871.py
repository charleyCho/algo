# D2
# 그래프 경로
# 완전탐색 - 백트래킹

def find_next(s):
    global result
    if result:
        return

    if s == G:
        result = 1
        return

    for g in range(1, V+1):
        if adj[s][g] and not visited[g]:
            visited[g] = 1
            find_next(g)
            visited[g] = 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        S, E = map(int, input().split())
        adj[S][E] = 1

    S, G = map(int, input().split())
    visited = [0] * (V+1)
    result = 0
    find_next(S)
    print('#{} {}'.format(tc, result))
