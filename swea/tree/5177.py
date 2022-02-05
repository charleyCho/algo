# D2
# 이진 힙

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * (N+1)

    for i, num in enumerate(nums):
        if tree