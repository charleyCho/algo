# D2
# 색칠하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    squares = [list(map(int, input().split())) for _ in range(N)]
    colorMap = [[0] * 10 for _ in range(10)]
    purples = 0

    for square in squares:
        x1, y1, x2, y2, color = map(int, square)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                colorMap[y][x] += 1
                if colorMap[y][x] == 2:
                    purples += 1

    print('#{} {}'.format(tc, purples))
