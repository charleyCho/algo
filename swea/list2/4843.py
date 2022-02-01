# D3
# 특별한 정렬

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    nums_reversed = list(reversed(nums))

    print('#{}'.format(tc), end=' ')
    for i in range(10):
        if i % 2:
            print(nums[i // 2], end=' ')
        else:
            print(nums_reversed[i // 2], end=' ')
    print()
