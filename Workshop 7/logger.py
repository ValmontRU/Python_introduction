def calc_logger(a, b, operator, result):
    with open('log.txt', 'a') as file:
        file.write(f'{a} {operator} {b} = {result}\n')