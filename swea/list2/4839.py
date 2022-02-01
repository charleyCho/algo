# D2
# 이진탐색

def binary_search(a_start, a_end, b_start, b_end):
    global result
    finished = False

    a_mid = int((a_start + a_end) / 2)
    if a_mid > Pa: a_end = a_mid
    elif a_mid < Pa: a_start = a_mid
    else: finished = True

    b_mid = int((b_start + b_end) / 2)
    if b_mid > Pb: b_end = b_mid
    elif b_mid < Pb: b_start = b_mid
    else:
        if finished:
            result = '0'
            return
        else:
            result = 'B'
            return

    if finished:
        result = 'A'
        return

    binary_search(a_start, a_end, b_start, b_end)


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    result = ''
    binary_search(1, P, 1, P)
    print('#{} {}'.format(tc, result))