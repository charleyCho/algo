# D2
# Forth

operator_list = ['+', '-', '*', '/']
T = int(input())
for tc in range(1, T+1):
    code = list(input().split())[:-1]
    operand = []
    is_error = False

    for c in code:
        if c not in operator_list:
            operand.append(int(c))
        else:
            if len(operand) < 2:
               is_error = True
               break

            second = operand.pop(-1)
            first = operand.pop(-1)
            if c == '+':
                operand.append(first + second)
            elif c == '-':
                operand.append(first - second)
            elif c == '*':
                operand.append(first * second)
            elif c == '/':
                operand.append(first // second)

    if len(operand) > 1:
        is_error = True

    if is_error:
        print('#{} error'.format(tc))
    else:
        print('#{} {}'.format(tc, operand[0]))