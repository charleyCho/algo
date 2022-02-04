# D4
# 암호

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 숫자 개수 / 칸 추가 / 반복 횟수
    nums = list(map(int, input().split()))
    idx = 0
    for k in range(1, K+1):
        N = len(nums)
        idx = (idx + M) % N
        if idx == 0:
            nums.append(nums[-1] + nums[0])
            idx = N
        else:
            nums.insert(idx, nums[idx] + nums[idx-1])

    nums.reverse()
    print('#{}'.format(tc), end=' ')
    print(*nums[:10])
