# D3
# 수열 합치기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))

    for _ in range(M - 1):
        seq2 = list(map(int, input().split()))
        x = seq2[0]

        seq1 = []
        seq3 = []
        min_v = 1001
        min_i = 0
        max_v = 0
        max_i = 0
        for i, v in enumerate(seq1):

            if v < min_v: miv_v = v
            if v > max_v: max_v = v
            if v > x:
                seq1 =