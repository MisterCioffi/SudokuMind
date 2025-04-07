# inizializzazione.py

def inizializzazione_domains():
    domains = {}
    for r in range(9):
        for c in range(9):
            domains[(r, c)] = set(range(1, 10))
    return domains

def set_peers():
    peers = {}
    for ri in range(9):
        for cj in range(9):
            l = set()
            for i in range(9):
                if i != cj:
                    l.add((ri, i))
            for i in range(9):
                if i != ri:
                    l.add((i, cj))
            box_row_start = 3 * (ri // 3)
            box_col_start = 3 * (cj // 3)
            for i in range(box_row_start, box_row_start + 3):
                for j in range(box_col_start, box_col_start + 3):
                    if (i, j) != (ri, cj):
                        l.add((i, j))
            peers[(ri, cj)] = l
    return peers

def print_grid(domains):
    for r in range(9):
        row = ''
        for c in range(9):
            val = domains.get((r, c), {0})
            if len(val) == 1:
                row += str(next(iter(val))) + ' '
            else:
                row += '. '
            if c in [2, 5]:
                row += '| '
        print(row)
        if r in [2, 5]:
            print('-' * 21)
