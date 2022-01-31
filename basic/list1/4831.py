# D3
# 전기버스
# 무지성 백트래킹으로 풀었으나, 오히려 비효율적인 접근이었음

def go(present, left, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return

    if left == 0:
        return

    if present == N:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    if stations[present]:
        if not visited[present]:
            visited[present] = 1
            go(present + 1, K, cnt + 1)
            visited[present] = 0
    go(present + 1, left - 1, cnt)



T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    S = list(map(int, input().split()))
    stations = [0] * (N + 1)
    visited = [0] * (N + 1)
    for m in range(M):
        stations[S[m]] = 1

    min_cnt = M + 1
    go(1, K, 0)
    if min_cnt == M + 1:
        min_cnt = 0
    print('#{} {}'.format(tc, min_cnt))
