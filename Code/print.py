def print_grid(domains):
    for r in range(9):
        row = ''
        for c in range(9):
            val = domains[(r, c)]
            if len(val) == 1:
                row += str(next(iter(val))) + ' '
            else:
                row += '. '
            if c in [2, 5]:
                row += '| '
        print(row)
        if r in [2, 5]:
            print('-' * 21)
