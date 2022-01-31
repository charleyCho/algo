# D2
# 숫자 카드

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input()
    cnt = [0] * 10
    for card in cards:
        cnt[int(card)] += 1

    max_num = 0
    max_cnt = 0
    for c in range(10):
        if cnt[c] >= max_cnt:
            max_num = c
            max_cnt = cnt[c]

    print('#{} {} {}'.format(tc, max_num, max_cnt))
