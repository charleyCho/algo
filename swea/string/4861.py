# D2
# 회문

def is_circular(s):
    mid = len(s) // 2
    if len(s) % 2:
        if s[:mid] == ''.join(list(reversed(list(s[mid + 1:])))):
            return True
    else:
        if s[:mid] == ''.join(list(reversed(list(s[mid:])))):
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    charMap = [input() for _ in range(N)]
    completed = False
    result = ''

    # 가로방향 검사
    for i in range(N):
        if completed: break
        target = charMap[i]
        for j in range(N - M + 1):
            if is_circular(target[j: j + M]):
                completed = True
                result = target[j: j + M]
                break

    # 세로방향 검사
    for i in range(N):
        if completed: break
        target = []
        for j in range(N):
            target.append(charMap[j][i])
        for k in range(N - M + 1):
            if is_circular(''.join(target)[k: k + M]):
                completed = True
                result = ''.join(target)[k: k + M]
                break

    print('#{} {}'.format(tc, result))
