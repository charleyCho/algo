# D2
# 괄호검사

T = int(input())
for tc in range(1, T+1):
    chars = input()
    check_stack = []
    result = 1

    for char in chars:
        if char in ['(', '{']:
            check_stack.append(char)

        if char == ')':
            if not check_stack:
                result = 0
                break

            if check_stack[-1] == '(':
                check_stack.pop()
            else:
                result = 0
                break

        if char == '}':
            if not check_stack:
                result = 0
                break

            if check_stack[-1] == '{':
                check_stack.pop()
            else:
                result = 0
                break

    if check_stack:
        result = 0

    print('#{} {}'.format(tc, result))