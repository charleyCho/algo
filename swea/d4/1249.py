# D4 보급로
# 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.
# 1. dfs(백트래킹) -> 답은 맞으나 시간초과
# 2. bfs(dijkstra)

# def check_recovery_time(cr, cc, time):
#     global min_recovery_time
#
#     if cr == map_size-1 and cc == map_size-1:
#         if min_recovery_time > time:
#             min_recovery_time = time
#         return
#
#     if min_recovery_time <= time:
#         return
#
#     for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#         nr = cr + dr
#         nc = cc + dc
#         if 0 <= nr < map_size and 0 <= nc < map_size and not visited[nr][nc]:
#             visited[nr][nc] = 1
#             check_recovery_time(nr, nc, time + int(map1[nr][nc]))
#             visited[nr][nc] = 0

from collections import deque


def check_recovery_time(sr, sc):
    Q = deque()
    Q.append((sr, sc))
    recovery_times[sr][sc] = 0

    while Q:
        cr, cc = Q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < map_size and 0 <= nc < map_size and recovery_times[nr][nc] > recovery_times[cr][cc] + map2[nr][nc]:
                recovery_times[nr][nc] = recovery_times[cr][cc] + map2[nr][nc]
                Q.append((nr, nc))


for test_case in range(1, int(input()) + 1):
    map_size = int(input())
    INF = map_size ** 3
    # map1 = list(input() for _ in range(map_size))
    # visited = [[0] * map_size for _ in range(map_size)]
    # min_recovery_time = map_size ** 2
    # check_recovery_time(0, 0, 0)
    # print('#{} {}'.format(test_case, min_recovery_time))

    map2 = [[int(i) for i in input()] for _ in range(map_size)]
    recovery_times = [[INF] * map_size for _ in range(map_size)]
    check_recovery_time(0, 0)
    print('#{} {}'.format(test_case, recovery_times[-1][-1]))
