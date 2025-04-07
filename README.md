# Algoritmo IA per la Risoluzione del Sudoku con AC-3 e Backtracking

Questo progetto riguarda la risoluzione di un puzzle Sudoku utilizzando due tecniche di intelligenza artificiale: **AC-3 (Arc-Consistency 3)** e **Backtracking**. Il Sudoku è un gioco di logica che richiede di completare una griglia 9x9 con numeri da 1 a 9, rispettando alcune regole di coerenza: ogni numero deve apparire una sola volta per riga, colonna e blocco 3x3.

## Panoramica dell'Algoritmo

### 1. **AC-3 (Arc-Consistency 3)**

AC-3 è un algoritmo di *arc-consistency* che viene applicato per ridurre i domini delle variabili prima di iniziare la ricerca vera e propria. L'algoritmo si assicura che, per ogni coppia di variabili con una relazione, se una di esse è già assegnata a un valore, allora i domini della variabile rimanente vengano ridotti in modo tale da eliminare i valori incompatibili. Questo passaggio aiuta a ridurre il numero di possibilità e rende la ricerca successiva più efficiente.

### 2. **Backtracking**

Una volta che AC-3 ha ridotto i domini, si avvia la ricerca con **Backtracking**. Qui, si prova ad assegnare un valore a una variabile, scegliendo prima la variabile con il **dominio minimo**, ossia la variabile con il minor numero di possibili valori (questa è una tecnica di ottimizzazione per ridurre lo spazio di ricerca, chiamata *Minimum Remaining Values* - MRV). Se l'assegnamento di un valore porta a un conflitto, si effettua un *rollback* e si prova un altro valore. Il processo continua fino a trovare una soluzione completa o determinare che non è possibile.

## Dettagli Implementativi

### Struttura dei Dati

La gestione del puzzle Sudoku avviene tramite due componenti principali:

1. **Variabili e Domini**: Ogni cella del Sudoku è rappresentata come una coppia di coordinate `(r, c)` dove `r` è la riga e `c` è la colonna. I domini delle variabili sono rappresentati come un dizionario, in cui ogni chiave è la coppia `(r, c)` e il valore è un insieme di numeri possibili per quella cella.

    - La funzione `inizializzazione_domains` imposta inizialmente tutti i domini come l'insieme `{1, 2, 3, 4, 5, 6, 7, 8, 9}` per tutte le celle.
    - La funzione `val_domains` modifica questi domini per riflettere i numeri già precompilati nel puzzle.

    Ecco un esempio della struttura dei domini iniziali e personalizzati:

    ```python
    domains[(0, 0)] = {8}
    domains[(1, 2)] = {3}
    domains[(1, 3)] = {6}
    domains[(2, 1)] = {7}
    domains[(2, 4)] = {9}
    # Altri valori per altre celle
    ```

2. **Peer (Vicini)**: Ogni cella ha dei "peer", ossia altre celle che sono vincolate dalla stessa riga, colonna o blocco 3x3. La funzione `set_peers` costruisce un dizionario chiamato `peers`, in cui ogni chiave è una cella e il valore è l'insieme delle celle adiacenti in riga, colonna e blocco 3x3.

    - Per esempio, per la cella `(0, 0)`, i peer saranno tutte le altre celle nella stessa riga (eccetto `(0, 0)`), nella stessa colonna, e nel blocco 3x3.

3. **Rimozione di Valori Incoerenti**: La funzione `remove_inc_val` è utilizzata per rimuovere valori che diventano inconsistente a causa di una modifica in una cella vicina. Quando un valore in una cella è fissato, i domini delle celle adiacenti (i peer) vengono aggiornati per rimuovere quel valore, garantendo che i vincoli di riga, colonna e blocco siano rispettati.

4. **Eliminazione Incoerente con AC-3**: Durante l'esecuzione dell'algoritmo AC-3, le celle vengono esplorate e i domini ridotti fino a che non si ottiene una soluzione consistente o fino a quando non si scopre che non esistono più valori validi per una cella (fallimento).

### Selezione della Variabile con Dominio Minimo

Durante la fase di ricerca con backtracking, la scelta della variabile da assegnare segue l'euristica **Minimum Remaining Values (MRV)**. Questo approccio sceglie la variabile che ha il dominio più piccolo, ossia quella che ha il minor numero di valori possibili. Questo aiuta a ridurre lo spazio di ricerca, affrontando prima le variabili più difficili da risolvere.

## Vantaggi e Ottimizzazione

- **AC-3** riduce significativamente il numero di valori che devono essere esplorati, limitando i conflitti durante il backtracking.
- L'uso dell'euristica MRV ottimizza ulteriormente il processo, riducendo lo spazio di ricerca e migliorando l'efficienza del backtracking.

## Conclusioni

Questo approccio, che combina la consistenza degli archi (AC-3) con la ricerca tramite backtracking, rappresenta una soluzione efficiente per la risoluzione di puzzle Sudoku complessi. La riduzione dei domini tramite AC-3 e la selezione delle variabili con il dominio minimo contribuiscono a migliorare notevolmente la performance dell'algoritmo, portando a una risoluzione più rapida del problema.

---



