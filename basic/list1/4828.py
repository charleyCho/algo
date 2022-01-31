# D2
# mix max

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_num = 0
    min_num = 1000000
    for num in nums:
        if num > max_num: max_num = num
        if num < min_num: min_num = num

    print('#{} {}'.format(tc, max_num - min_num))
