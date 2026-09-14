# 🧩 Sudoku Solver in Python

Un algoritmo leggero e performante scritto in Python per la risoluzione automatica di schemi di Sudoku, basato sulle tecniche di logica deduttiva **Naked Singles** (candidati unici) e **Double Pairs** (coppie nascoste/esclusive).

---

## 📌 Descrizione

Il programma analizza una griglia di Sudoku fornita in input sotto forma di matrice e procede secondo i seguenti passaggi:

1. **Validazione della griglia**: Verifica che il tabellone iniziale rispetti le regole del Sudoku (nessun duplicato su righe, colonne o sotto-griglie 3x3).
2. **Calcolo dei candidati**: Identifica i numeri possibili per ciascuna cella vuota incrociando i vincoli di riga, colonna e blocco.
3. **Risoluzione deduttiva**: Applica iterativamente le strategie di logica per inserire i valori certi fino al completamento dello schema.

---

## 📊 Performance e Copertura

L'algoritmo risolve con successo e senza backtracking i livelli di difficoltà:

- 🟢 **Facile** (100% di successo)
- 🟡 **Medio** (100% di successo)
- 🟠 **Difficile** (100% di successo)
- 🔴 **Esperto** (Raggiunge un'alta percentuale di completamento, in fase di ottimizzazione per la copertura totale)

---

## 🚀 Come Eseguire il Progetto

### Requisiti
- **Python 3.8+** installato sul sistema.

### Istruzioni

1. **Clona la repository** o scarica lo script:
   ```bash
   git clone [https://github.com/tuo-username/nome-repo.git](https://github.com/tuo-username/nome-repo.git)
   cd nome-repo
