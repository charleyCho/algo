# D3
# 숫자 추가

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    seq = list(map(int, input().split()))

    for _ in range(M):
        idx, num = map(int, input().split())
        seq.insert(idx, num)

    print('#{} {}'.format(tc, seq[L]))

