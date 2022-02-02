# D2
# 토너먼트 카드게임

def matching(i, j):
    if i == j:
        return i

    left = matching(i, (i+j)//2)
    right = matching((i+j)//2 + 1, j)
    if (cards[left], cards[right]) in [(1, 2), (2, 3), (3, 1)]:
        return right
    else:
        return left


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, matching(0, N - 1) + 1))
