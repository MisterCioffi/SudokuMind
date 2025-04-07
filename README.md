# Progetto IA per la Risoluzione del Sudoku con AC-3 e Backtracking

Questo progetto riguarda la risoluzione di un puzzle Sudoku utilizzando due tecniche di intelligenza artificiale: **AC-3 (Arc-Consistency 3)** e **Backtracking**. Il Sudoku è un gioco di logica che richiede di completare una griglia 9x9 con numeri da 1 a 9, rispettando alcune regole di coerenza: ogni numero deve apparire una sola volta per riga, colonna e blocco 3x3.

## Panoramica dell'Algoritmo

### 1. **AC-3 (Arc-Consistency 3)**

AC-3 è un algoritmo di *arc-consistency* che viene applicato per ridurre i domini delle variabili prima di iniziare la ricerca vera e propria. L'algoritmo si assicura che, per ogni coppia di variabili con una relazione, se una di esse è già assegnata a un valore, allora i domini della variabile rimanente vengano ridotti in modo tale da eliminare i valori incompatibili. Questo passaggio aiuta a ridurre il numero di possibilità e rende la ricerca successiva più efficiente.

### 2. **Backtracking**

Una volta che AC-3 ha ridotto i domini, si avvia la ricerca con **Backtracking**. Qui, si prova ad assegnare un valore a una variabile, scegliendo prima la variabile con il **dominio minimo**, ossia la variabile con il minor numero di possibili valori (questa è una tecnica di ottimizzazione per ridurre lo spazio di ricerca, chiamata *Minimum Remaining Values* - MRV). Se l'assegnamento di un valore porta a un conflitto, si effettua un *rollback* e si prova un altro valore. Il processo continua fino a trovare una soluzione completa o determinare che non è possibile.

## Dettagli Implementativi

### Struttura dei Dati

Le variabili del Sudoku (ogni cella della griglia) sono rappresentate come coordinate (riga, colonna), e i loro domini (i valori possibili) sono gestiti come insiemi. I vincoli tra le variabili (riga, colonna, blocco 3x3) sono rappresentati attraverso un dizionario che indica i "peer" (i vicini) di ciascuna cella.

### Riduzione dei Domini con AC-3

Inizialmente, il dominio di ogni variabile è l'insieme di numeri da 1 a 9. AC-3 viene applicato per ridurre i domini, assicurandosi che i numeri in un dominio siano coerenti con quelli già assegnati nelle celle adiacenti (righe, colonne e blocchi 3x3).

### Selezione della Variabile con Dominio Minimo

Durante la fase di ricerca con backtracking, la scelta della variabile da assegnare segue l'euristica **Minimum Remaining Values (MRV)**, che seleziona la variabile con il dominio più piccolo. Questo approccio mira a ridurre il numero di passaggi necessari per risolvere il puzzle, perché si affrontano prima le variabili con meno opzioni disponibili.

## Vantaggi e Ottimizzazione

- **AC-3** riduce significativamente il numero di valori che devono essere esplorati, limitando i conflitti durante il backtracking.
- L'uso dell'euristica MRV ottimizza ulteriormente il processo, riducendo lo spazio di ricerca e migliorando l'efficienza del backtracking.

## Conclusioni

Questo approccio, che combina la consistenza degli archi (AC-3) con la ricerca tramite backtracking, rappresenta una soluzione efficiente per la risoluzione di puzzle Sudoku complessi. La riduzione dei domini tramite AC-3 e la selezione delle variabili con il dominio minimo contribuiscono a migliorare notevolmente la performance dell'algoritmo, portando a una risoluzione più rapida del problema.

---

Se hai bisogno di ulteriori chiarimenti o spiegazioni, fammi sapere!

