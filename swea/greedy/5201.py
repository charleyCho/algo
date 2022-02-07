# D3
# 컨테이너 운반

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 컨테이너 수 / 트럭 수
    goods = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    result = 0

    for i in range(len(trucks)):
        for j in range(len(goods)):
            if goods[j] <= trucks[i]:
                result += goods.pop(j)
                break

    print('#{} {}'.format(tc, result))
