# D4
# 수열 편집

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 수열 길이 / 추가 횟수 / 출력할 인덱스
    seq = list(input().split())
    for _ in range(M):
        add = list(input().split())
        if add[0] == 'I':
            seq.insert(int(add[1]), add[2])
        elif add[0] == 'D':
            seq.pop(int(add[1]))
        elif add[0] == 'C':
            seq[int(add[1])] = add[2]

    print('#{}'.format(tc), end=' ')
    if len(seq) < L-1:
        print(-1)
    else:
        print(seq[L])
