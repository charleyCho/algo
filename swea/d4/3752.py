# 가능한 시험점수

for tc in range(1, int(input()) + 1):
    N = int(input())
    grades = list(map(int, input().split()))

    # cases = set()
    # for i in range(2**N):
    #     case = 0
    #     for j in range(N):
    #         if i & (1 << j) != 0:
    #             case += grades[j]
    #     cases.add(case)

    visited = [1] + [0] * sum(grades)
    cases = [0]
    for grade in grades:
        for i in range(len(cases)):
            if not visited[grade + cases[i]]:
                visited[grade + cases[i]] = 1
                cases.append(grade + cases[i])

    print('#{} {}'.format(tc, len(cases)))
