# D3
# 피자 굽기
# 요구사항 flow 그대로 구현하자

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    inventory = [[data[x], x+1] for x in range(M)]
    pot = [inventory.pop(0) for _ in range(N)]

    while len(pot) > 1:
        pizza = pot.pop(0)
        pizza[0] //= 2
        if pizza[0] == 0:
            if inventory:
                pot.append(inventory.pop(0))
        else:
            pot.append(pizza)

    print('#{} {}'.format(tc, pot[0][1]))
