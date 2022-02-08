# D3
# 화물 도크

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tasks = [list(map(int, input().split())) for _ in range(N)]
    tasks.sort(key=lambda x: x[1])

    cnt = 1
    time = tasks[0][1]
    tasks.pop(0)

    while(tasks):
        task = tasks.pop(0)
        if task[0] >= time:
            cnt += 1
            time = task[1]

    print('#{} {}'.format(tc, cnt))
