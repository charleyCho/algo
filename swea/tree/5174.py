# D2
# subtree

def counting(idx):
    global children_count
    children_count += 1
    if left[idx]:
        counting(left[idx])
    if right[idx]:
        counting(right[idx])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(0, E*2, 2):
        idx, child = data[i], data[i+1]
        if left[idx]:
            right[idx] = child
        else:
            left[idx] = child

    children_count = 0
    counting(N)
    print('#{} {}'.format(tc, children_count))

