# D2
# 반복문자 지우기

def deduplicate():
    global s

    n = len(s)
    check = [s[0]]
    for i in range(1, n):
        if s[i] == check[0]:
            s.pop(i - 1)
            s.pop(i - 1)
            deduplicate()
            break
        else:
            check.clear()
            check.append(s[i])


T = int(input())
for tc in range(1, T+1):
    s = list(input())
    deduplicate()
    print('#{} {}'.format(tc, len(s)))

