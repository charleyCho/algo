# D2
# 문자열 비교

T = int(input())
for tc in range(1, T+1):
    part = input()
    full = input()
    N, M = len(part), len(full)
    result = 0

    for i in range(M - N + 1):
        if full[i] == part[0]:
            if full[i: i + N] == part:
                result = 1
                break

    print('#{} {}'.format(tc, result))