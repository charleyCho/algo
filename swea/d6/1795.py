# 인수의 생일파티

def dijkstra(dist, start):
    weight = dist[start][:]
    weight[start] = 0
    visited = [0] * (N+1)
    visited[start] = 1

    for _ in range(1, N):
        min_idx = -1
        min_value = INF
        for i in range(1, N+1):
            if not visited[i] and min_value > weight[i]:
                min_idx = i
                min_value = weight[i]
        visited[min_idx] = 1

        for j in range(1, N+1):
            if not visited[j] and weight[j] > weight[min_idx] + dist[min_idx][j]:
                weight[j] = weight[min_idx] + dist[min_idx][j]

    return weight


for test_case in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    INF = 1000 * 10000
    dist1 = [[INF] * (N+1) for _ in range(N+1)]
    dist2 = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        dist1[x][y] = c
        dist2[y][x] = c

    dist_to_X = dijkstra(dist1, X)[1:]
    dist_to_home = dijkstra(dist2, X)[1:]
    result = max([dist_to_X[i] + dist_to_home[i] for i in range(N)])
    print('#{} {}'.format(test_case, result))
