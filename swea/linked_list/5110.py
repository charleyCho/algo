# D3
# 수열 합치기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))

    for _ in range(M - 1):
        seq2 = list(map(int, input().split()))
        for i, v in enumerate(seq):
            if v > seq2[0]:
                seq[i:i] = seq2
                break
        else:
            seq.extend(seq2)

    print('#{}'.format(tc), end=' ')
    print(*seq[: len(seq) - 11: -1])