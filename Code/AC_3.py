from collections import deque
queue = deque([(xi, xj) for xi in domains for xj in peers[xi]])   

#global queue_copy

def AC_3(peers, domains, queue):
    iteration = 0
    #queue_copy =  deque(queue)

    while queue:

        xi, xj = queue.popleft()
        iteration += 1
        print(f"[Iterazione {iteration}] Controllo arco {xi} -> {xj}")

        if remove_inc_val(domains, xi, xj):
            if len(domains[xi]) == 0:
                return False #l'algortimo non è risolvibile
            elif len(domains[xi]) == 1:
                print(f"Cella {xi} è stata risolta: {next(iter(domains[xi]))}")

            for xk in peers[xi]:
                if xk != xj:
                    queue.append((xk, xi))

        
            #queue_copy =  deque(queue)

    return True

def remove_inc_val(domains, xi, xj):
    rimosso = False
    for i in domains[xi].copy():
        # Se per il valore i in xi non esiste nessun valore diverso in xj, allora rimuovi i
        if len(domains[xj]) == 1 and i in domains[xj]:
            domains[xi].remove(i)
            rimosso = True
    return rimosso
