# 최적 경로

def calculating_distance(cur_x, cur_y, idx, cur_distance):
    global min_distance
    if idx == N:
        cur_distance += abs(end_x - cur_x) + abs(end_y - cur_y)
        if min_distance > cur_distance:
            min_distance = cur_distance
        return

    if min_distance <= cur_distance:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            next_x, next_y = locations[i][0], locations[i][1]
            calculating_distance(next_x, next_y, idx+1, cur_distance + abs(next_x - cur_x) + abs(next_y - cur_y))
            visited[i] = 0


for test_case in range(1, int(input()) + 1):
    N = int(input())
    input_data = list(map(int, input().split()))
    start_x, start_y, end_x, end_y = input_data[0], input_data[1], input_data[2], input_data[3]
    locations = [(input_data[x], input_data[x+1]) for x in range(4, (N+1)*2+1, 2)]
    visited = [0] * N
    min_distance = 100 * 100 * N
    calculating_distance(start_x, start_y, 0, 0)
    print('#{} {}'.format(test_case, min_distance))
