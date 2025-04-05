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
