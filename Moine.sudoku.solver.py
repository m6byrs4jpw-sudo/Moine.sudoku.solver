Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.

================ RESTART: /Users/fla/Desktop/options/esempio.py ================
La tabella fornita è un sudoku
La tabella fornita è un Sudoku valido!
Traceback (most recent call last):
  File "/Users/fla/Desktop/options/esempio.py", line 148, in <module>
    print(candidati(tabella))
  File "/Users/fla/Desktop/options/esempio.py", line 135, in candidati
    candidati_ij = candidati - nrico
TypeError: unsupported operand type(s) for -: 'function' and 'set'

================ RESTART: /Users/fla/Desktop/options/esempio.py ================
La tabella fornita è un sudoku
La tabella fornita è un Sudoku valido!
[{1, 3, 4, 5}, {3, 4, 5}, {1, 3, 4}, 7, 6, 2, {8, 5}, 9, {4}]
[{1, 4, 5}, {9, 4, 5, 6}, {1, 4, 6, 9}, 3, 8, {1}, {5}, 2, 7]
[2, 8, {4, 7}, {4}, 5, 9, 1, 6, 3]
[{8, 3, 4, 7}, {9, 3, 4}, {2, 3, 4, 7, 8, 9}, {2}, {9, 7}, {8}, 6, {3, 4, 5}, 1]
[{8, 4, 7}, 1, 5, {6}, {9, 7}, 3, 2, {4}, {9, 4}]
[6, {9, 3}, {9, 2, 3}, {1, 2}, 4, 5, 7, {3}, 8]
[{8, 1, 3}, 2, {8, 1, 3, 6}, 9, {1, 3}, {1, 6}, 4, {1, 3, 7}, 5]
[{1, 3, 5}, 7, {1, 3, 6}, 8, 2, 4, {9, 3}, {1, 3}, {9, 6}]
[9, {3, 4, 6}, {1, 3, 4, 6}, 5, {1, 3}, 7, {3}, 8, {2, 6}]
>>> 
================= RESTART: /Users/fla/Desktop/options/esempio.py ================
La tabella fornita è un sudoku
La tabella fornita è un Sudoku valido!
[{1, 3, 4, 5}, {3, 4, 5}, {1, 3, 4}, 7, 6, 2, {8, 5}, 9, 4]
[{1, 4, 5}, {9, 4, 5, 6}, {1, 4, 6, 9}, 3, 8, 1, 5, 2, 7]
[2, 8, {4, 7}, 4, 5, 9, 1, 6, 3]
[{8, 3, 4, 7}, {9, 3, 4}, {2, 3, 4, 7, 8, 9}, 2, {9, 7}, 8, 6, {3, 4, 5}, 1]
[{8, 4, 7}, 1, 5, 6, {9, 7}, 3, 2, 4, {9, 4}]
[6, {9, 3}, {9, 2, 3}, {1, 2}, 4, 5, 7, 3, 8]
[{8, 1, 3}, 2, {8, 1, 3, 6}, 9, {1, 3}, {1, 6}, 4, {1, 3, 7}, 5]
[{1, 3, 5}, 7, {1, 3, 6}, 8, 2, 4, {9, 3}, {1, 3}, {9, 6}]
[9, {3, 4, 6}, {1, 3, 4, 6}, 5, {1, 3}, 7, 3, 8, {2, 6}]
>>> 
================= RESTART: /Users/fla/Desktop/options/esempio.py ================
La tabella fornita è un sudoku
Traceback (most recent call last):
  File "/Users/fla/Desktop/options/esempio.py", line 169, in <module>
    risultato = loopsingoli(tabella)
  File "/Users/fla/Desktop/options/esempio.py", line 158, in loopsingoli
    while nuovo_sud:
NameError: name 'nuovo_sud' is not defined. Did you mean: 'nuovo_sudoku'?
>>> 
================= RESTART: /Users/fla/Desktop/options/esempio.py ================
La tabella fornita è un sudoku
Il sudoku finale:
[3, 5, 1, 7, 6, 2, 8, 9, 4]
[4, 6, 9, 3, 8, 1, 5, 2, 7]
[2, 8, 7, 4, 5, 9, 1, 6, 3]
[7, 3, 4, 2, 9, 8, 6, 5, 1]
[8, 1, 5, 6, 7, 3, 2, 4, 9]
[6, 9, 2, 1, 4, 5, 7, 3, 8]
[1, 2, 8, 9, 3, 6, 4, 7, 5]
[5, 7, 3, 8, 2, 4, 9, 1, 6]
[9, 4, 6, 5, 1, 7, 3, 8, 2]
