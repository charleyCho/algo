# D3
# 부분집합의 합

T = int(input())
for tc in range(1, T+1):
    A = [x for x in range(1, 13)]
    N, K = map(int, input().split())
    result = 0

    for i in range(1 << len(A)):
        sub_set = []
        for j in range(len(A)):
            if i & (1 << j):
                sub_set.append(A[j])
        if len(sub_set) == N and sum(sub_set) == K:
            result += 1

    print('#{} {}'.format(tc, result))