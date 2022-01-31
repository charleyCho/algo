# D2
# 구간합

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_sum = 0
    min_sum = 0xffffff
    for i in range(N - M + 1):
        tmp_sum = sum([nums[x] for x in range(i, i + M)])
        if tmp_sum > max_sum:
            max_sum = tmp_sum
        if tmp_sum < min_sum:
            min_sum = tmp_sum

    print('#{} {}'.format(tc, max_sum - min_sum))