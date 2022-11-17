def calc(x, y, op):
    res = None
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        if y == 0:
            res = 'Делитель равен 0 - деление на 0 невозможно.'
        else:
            res = x / y
    return res