# D2
# κΈμ μ

T = int(input())
for tc in range(1, T+1):
    chars = input()
    sentence = list(input())
    max_cnt = 0

    for char in chars:
        cnt = 0
        for c in sentence:
            if char == c:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt))