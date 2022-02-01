# D2
# 이진탐색

def binary_search(a_start, a_end, b_start, b_end):
    finished = False

    a_mid = (a_start + a_end) // 2
    if a_mid > Pa: a_end = a_mid
    elif a_mid < Pa: a_start = a_mid
    else: finished = True

    b_mid = (b_start + b_end) // 2
    if b_mid > Pb: b_end = b_mid
    elif b_mid < Pb: b_start = b_mid
    else:
        if finished: return '0'
        else: return 'B'

    if finished: return 'A'
    print(a_start, a_end, b_start, b_end)
    binary_search(a_start, a_end, b_start, b_end)


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    print('#{} {}'.format(tc, binary_search(0, P, 0, P)))