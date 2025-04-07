# backtracking.py
from collections import deque
from ac3 import AC_3

def ricerca_backtracking(domains, peers):
    assegnamento = {}
    for cella, dominio in domains.items():
        if len(dominio) == 1:
            assegnamento[cella] = {next(iter(dominio))}
    return backtracking(domains, assegnamento, peers)

def backtracking(domains, assegnamento, peers, livello=0):
    if len(assegnamento) == 81:
        return assegnamento

    var = scegli_variabile_non_assegnata(domains, assegnamento)
    if var is None:
        return "fallimento"

    for valore in list(domains[var]):
        if verifica_consistenza(valore, var, assegnamento, peers):
            assegnamento[var] = {valore}
            original_domain = domains[var].copy()
            domains[var] = {valore}
            removed = []
            queue = deque([(xk, var) for xk in peers[var]])

            if AC_3(peers, domains, queue, removed):
                risultato = backtracking(domains, assegnamento, peers, livello + 1)
                if risultato != "fallimento":
                    return risultato

            domains[var] = original_domain
            for xi, val in removed:
                domains[xi].add(val)
            del assegnamento[var]

    return "fallimento"

def verifica_consistenza(valore, var, assegnamento, peers):
    for peer in peers[var]:
        if peer in assegnamento and valore in assegnamento[peer]:
            return False
    return True

def scegli_variabile_non_assegnata(domains, assegnamento):
    non_assegnate = [var for var in domains if var not in assegnamento]
    return min(non_assegnate, key=lambda var: len(domains[var])) if non_assegnate else None
