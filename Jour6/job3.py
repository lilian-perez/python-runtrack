def draw_carpet(n):
    print('+' + '-' * n + '+')
    for i in range(n):
        line = '#' * n
        line = line[:n - i - 1] + ' ' + line[n - i:]
        print('|' + line + '|')
    print('+' + '-' * n + '+')

draw_carpet(10)
