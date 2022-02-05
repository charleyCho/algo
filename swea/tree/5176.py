# D2
# 이진탐색

def making_tree(n):
    global cnt
    if n <= N:
        making_tree(2*n)
        nodes[n] = cnt
        cnt += 1
        making_tree(2*n + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nodes = [0] * (N+1)
    cnt = 1
    making_tree(1)

    print('#{} {} {}'.format(tc, nodes[1], nodes[N//2]))