
from collections import deque
from time import sleep
from copy import deepcopy
# La gestione di ogni posizione è definita mediante la tupla (r,c), dove r è la riga e c la colonna. 
# Da notare come r e c vadano da 0 a 8.
# Tutte le tuple sono all'interno di un dizionario domains che ci permette di associare ad ogni tupla i vincoli
# All'inizio andiamo a imporre un dominio a tutte che va da 1 a 9
global domains
domains = {}

def inizializzazione_domains(domains):
    for r in range(9):
        for c in range(9):
            domains[(r, c)] = set(range(1, 10))

# Ogni valore iniziale deve avere un dominio con un solo elemento
# Riga 0

def val_domains(domains):
    domains[(0, 2)] = {3}
    domains[(0, 4)] = {2}
    domains[(0, 6)] = {6}

    domains[(1, 0)] = {9}
    domains[(1, 3)] = {3}
    domains[(1, 5)] = {5}
    domains[(1, 8)] = {1}

    domains[(2, 2)] = {1}
    domains[(2, 3)] = {8}
    domains[(2, 5)] = {6}
    domains[(2, 6)] = {4}

    domains[(3, 2)] = {8}
    domains[(3, 3)] = {1}
    domains[(3, 5)] = {2}
    domains[(3, 6)] = {9}

    domains[(4, 0)] = {7}
    domains[(4, 8)] = {8}

    domains[(5, 2)] = {6}
    domains[(5, 3)] = {7}
    domains[(5, 5)] = {8}
    domains[(5, 6)] = {2}

    domains[(6, 2)] = {2}
    domains[(6, 3)] = {6}
    domains[(6, 5)] = {9}
    domains[(6, 6)] = {5}

    domains[(7, 0)] = {8}
    domains[(7, 3)] = {2}
    domains[(7, 5)] = {3}
    domains[(7, 8)] = {9}

    domains[(8, 2)] = {5}
    domains[(8, 4)] = {1}
    domains[(8, 6)] = {3}


# Stampa della griglia in modo leggibile
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
 
def AC_3(peers, domains, queue):
    iteration = 0
    #queue_copy =  deque(queue)

    while queue:

        xi, xj = queue.popleft()
        iteration += 1
        #print(f"[Iterazione {iteration}] Controllo arco {xi} -> {xj}")

        if remove_inc_val(domains, xi, xj):
            if len(domains[xi]) == 0:
                print(f"Errore: il dominio della cella {xi} è diventato vuoto. I valori iniziali sono incompatibili.")
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
            #print(f"{domains[xi]}")
            rimosso = True

    return rimosso


def ricerca_backtracking(domains):
    assegnamento = {}
    for cella, dominio in domains.items():
        if len(dominio) == 1:
            assegnamento[cella] = {next(iter(dominio))}

    return backtracking(domains, assegnamento)

def backtracking(domains, assegnamento):
    if len(assegnamento) == 81:
        return assegnamento

    var = scegli_variabile_non_assegnata(domains, assegnamento)
    if var is None:
        return "fallimento"
    
    for valore in domains[var]:
        if verifica_consistenza(valore, var, assegnamento):
            assegnamento_copy = deepcopy(assegnamento)
            assegnamento_copy[var] = {valore}

            domains_copy = deepcopy(domains)
            #for key, value in domains_copy.items():
                #print(f"{key}: {value}" + "\t")
            domains_copy[var] = {valore}
            
            queue_copy = deepcopy(queue)

            #queue_new = deque([(xi, xj) for xi in domains_copy for xj in peers[xi]])  

            if AC_3(peers, domains_copy,queue_copy):
                #print("Iterazione AC-3 SUCCESSO")
                risultato = backtracking(domains_copy, assegnamento_copy)

                if risultato != 'fallimento':
                    return risultato
            else:
                print("AC-3 non è riuscito a ridurre il dominio, si passa alla scelta di un'altro valore")
            
            del assegnamento_copy[var]

    
    return "fallimento"


def verifica_consistenza(valore, var, assegnamento):

    for peer in peers[var]:
        if peer in assegnamento and valore in assegnamento[peer]:
            return False
    
    return True
            
    
def scegli_variabile_non_assegnata(domains, assegnamento):  
    # Troviamo la variabile con il dominio più piccolo che non è già assegnata
    min_domain_size = float('inf')
    min_var = None
    
    for var in domains:
        if var not in assegnamento:
            domain_size = len(domains[var])
            if domain_size < min_domain_size:
                min_domain_size = domain_size
                min_var = var
    
    if min_var is not None:
        return min_var
    else:
        return None


# Esecuzione iniziale
if __name__ == "__main__":
    
    inizializzazione_domains(domains)
    val_domains(domains)
    
    print("Griglia iniziale:")
    print_grid(domains)
    
    global queue
    queue = deque([(xi, xj) for xi in domains for xj in peers[xi]])  
    #AC_3(peers, domains, queue)
   
    #for key, value in assegnamento.items():
        #print(f"{key}: {value} " + "\t" + "\n")
    #print(str(queue))
    
    #print("Griglia finale:")
    #print_grid(domains)

    AC_3(peers, domains, queue)
    print("AC-3 non è riuscito a risolvere il problema.")

    #for key, value in domains.items():
        #print(f"{key}: {value}" + "\t" + "\n")
  
    print("\nAvvio della ricerca con backtracking")
    soluzione = ricerca_backtracking(domains)
    
    if soluzione != "fallimento":
        print("\nGriglia risolta:")
        print_grid(soluzione)
    else:
        print("Nessuna soluzione trovata.")
