# D2
# 노드의 거리

def is_connected(start, cnt):
    global result

    if cnt >= result:
        return

    if start == G:
        if cnt < result:
            result = cnt
        return

    for end in range(1, V+1):
        if adj[start][end] and not visited[start][end]:
            visited[start][end] = 1
            is_connected(end, cnt+1)
            visited[start][end] = 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1
        adj[e][s] = 1

    visited = [[0] * (V+1) for _ in range(V+1)]
    S, G = map(int, input().split())
    result = V + 1
    is_connected(S, 0)
    if result == V + 1:
        result = 0

    print('#{} {}'.format(tc, result))