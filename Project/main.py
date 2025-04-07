# main.py
import time
from collections import deque
from inizializzazione import inizializzazione_domains, set_peers, print_grid
from valori import val_domains
from ac3 import AC_3
from backtracking import ricerca_backtracking

if __name__ == "__main__":
    start_time = time.time()

    domains = inizializzazione_domains()
    val_domains(domains)
    peers = set_peers()

    print("Griglia iniziale:")
    print_grid(domains)

    queue = deque([(xi, xj) for xi in domains for xj in peers[xi]])
    removed = []
    AC_3(peers, domains, queue, removed)

    ac3_completo = all(len(domains[xi]) == 1 for xi in domains)
    if not ac3_completo:
        print("\nGriglia dopo AC-3 (non completamente risolta):")
        print_grid(domains)
        print("\nAvvio della ricerca con backtracking")
        soluzione = ricerca_backtracking(domains, peers)
    else:
        soluzione = domains

    if soluzione != "fallimento":
        print("\nGriglia risolta:")
        print_grid(soluzione)
    else:
        print("Nessuna soluzione trovata.")

    end_time = time.time()
    print(f"\n⏱ Tempo totale: {end_time - start_time:.4f} secondi")
