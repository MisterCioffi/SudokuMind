# ac3.py
from collections import deque

def remove_inc_val(domains, xi, xj, removed):
    rimosso = False
    for i in domains[xi].copy():
        if len(domains[xj]) == 1 and i in domains[xj]:
            domains[xi].remove(i)
            removed.append((xi, i))
            rimosso = True
    return rimosso

def AC_3(peers, domains, queue, removed):
    while queue:
        xi, xj = queue.popleft()
        if remove_inc_val(domains, xi, xj, removed):
            if len(domains[xi]) == 0:
                return False
            for xk in peers[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True
