
from collections import deque
from time import sleep
# La gestione di ogni posizione è definita mediante la tupla (r,c), dove r è la riga e c la colonna. 
# Da notare come r e c vadano da 0 a 8.
# Tutte le tuple sono all'interno di un dizionario domains che ci permette di associare ad ogni tupla i vincoli
# All'inizio andiamo a imporre un dominio a tutte che va da 1 a 9
domains = {}

for r in range(9):
    for c in range(9):
        domains[(r, c)] = set(range(1, 10))

# Ogni valore iniziale deve avere un dominio con un solo elemento
# Riga 0
domains[(0, 0)] = {5}
domains[(0, 1)] = {1}
domains[(0, 5)] = {3}
domains[(0, 7)] = {6}
domains[(0, 2)] = {4}

domains[(1, 1)] = {3}
domains[(1, 4)] = {4}
domains[(1, 6)] = {5}

domains[(2, 2)] = {2}
domains[(2, 4)] = {5}
domains[(2, 8)] = {8}

domains[(3, 3)] = {3}
domains[(3, 0)] = {6}
domains[(3, 1)] = {8}
domains[(3, 4)] = {1}
domains[(3, 7)] = {9}

domains[(4, 1)] = {4}
domains[(4, 4)] = {7}
domains[(4, 6)] = {2}

domains[(5, 2)] = {7}
domains[(5, 5)] = {6}
domains[(5, 8)] = {3}
domains[(5, 0)] = {1}

domains[(6, 2)] = {1}
domains[(6, 3)] = {5}
domains[(6, 6)] = {6}
domains[(6, 7)] = {4}

domains[(7, 1)] = {8}
domains[(7, 7)] = {7}
domains[(7, 3)] = {4}
domains[(7, 8)] = {2}

domains[(8, 0)] = {2}
domains[(8, 2)] = {8}
domains[(8, 5)] = {7}
domains[(8, 3)] = {1}
domains[(8, 8)] = {9}

# Stampa della griglia in modo leggibile
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

#CREAZIONE DIZIONARIO AVENTE COME CHIAVE TUTTE E 81 TUPLE --> AD OGUNA DI ESSE ASSOCIAMO I VINCOLI
def set_peers():
    global peers
    peers = {}
    # Itera per ogni cella della griglia 9x9
    for ri in range(9):
        for cj in range(9):
            l = set()  # Inizializza l'insieme dei peers per la cella (ri, cj)
            
            # Aggiungi tutte le celle della stessa riga
            for i in range(9):
                if i != cj:  # Escludi la cella stessa
                    l.add((ri, i))
            
            # Aggiungi tutte le celle della stessa colonna
            for i in range(9):
                if i != ri:  # Escludi la cella stessa
                    l.add((i, cj))
            
            # Calcola l'inizio del blocco 3x3 in cui si trova la cella (ri, cj)
            box_row_start = 3 * (ri // 3)
            box_col_start = 3 * (cj // 3)
            
            # Aggiungi tutte le celle dello stesso blocco 3x3
            for i in range(box_row_start, box_row_start + 3):
                for j in range(box_col_start, box_col_start + 3):
                    if (i, j) != (ri, cj):  # Escludi la cella stessa
                        l.add((i, j))
            
            # Assegna l'insieme dei peers alla cella corrente nel dizionario
            peers[(ri, cj)] = l
    return peers

peers = set_peers()

# Inizializza la coda con tutti gli archi: ogni coppia (xi, xj) dove xj è un peer di xi

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

# Esecuzione iniziale
if __name__ == "__main__":
    print("Griglia iniziale:")
    print_grid(domains)

    
    #print(str(queue))
    AC_3(peers, domains, queue)
    print("Griglia finale:")
    print_grid(domains)

    for key, value in domains.items():
        print(f"{key}: {value}" + "\t" + "\n")
