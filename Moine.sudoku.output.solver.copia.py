riga = 9
colonna = 9

tabella = [
]

print("Inserisci i numeri in riga, metti 0 quando il numero non c'è")
for i in range(riga):
    riga_corrente = []
    for j in range(colonna):
        valore_valido = False
        while not valore_valido:
            input_utente = input(f"Inserisci valore per posizione [{i}][{j}]: ")
            if input_utente.isdigit():
                valore = int(input_utente)
                if 0 <= valore <= 9:
                    riga_corrente.append(valore)
                    valore_valido = True
                else:
                    print("Hai inserito un numero non compreso tra 0 e 9, riprova")
            else:
                print("Hai inserito un carattere, riprova")

    tabella.append(riga_corrente)
# ==========================================
# 1. FUNZIONI - VALIDITÀ
# ==========================================
def validita(sudoku):
    #controllo righe
    for i in range(9):
        visti= set()
        for j in range(9):
            valore= sudoku[i][j]
            if valore != 0:
                if valore in visti:
                    print("Il valore è già presente")
                    return False
                visti.add(valore)
#controllo colonne
    for j in range(9):
         visti2= set()
         for i in range(9):
               valore= sudoku[i][j]
               if valore !=0:
                     if valore in visti2:
                         print("Il valore è già presente")
                         return False
                     visti2.add(valore)                            
#controllo quadrato 3x3
    q1, q2, q3 = set(), set(), set()
    q4, q5, q6 = set(), set(), set()
    q7, q8, q9 = set(), set(), set() 

    for i in range (9):
        for j in range(9):
            valore= sudoku [i][j]
            if valore == 0:
             continue
            
#controlli primi 3 quadrati vert
            if 0 <= i <= 2:
                if 0 <= j <= 2:
                    if valore in q1:
                        return False
                    q1.add(valore)
                elif 3<= j <= 5:
                   if valore in q2:
                        return False
                   q2.add(valore)
                elif 6<= j <= 8:
                    if valore in q3:
                        return False
                    q3.add(valore)
#controllo secondi 3 quadrati vert 
            elif 3 <= i <=5 :
                if 0 <= j <= 2:
                    if valore in q4:
                        return False
                    q4.add(valore)
                elif 3<= j <= 5:
                   if valore in q5:
                        return False
                   q5.add(valore)
                elif 6<= j <= 8:
                    if valore in q6:
                        return False
                    q6.add(valore)
#controllo terzi 3 quadrati vert 
            elif 6 <= i <= 8:
                if 0 <= j <= 2:
                    if valore in q7:
                        return False
                    q7.add(valore)
                elif 3<= j <= 5:
                    if valore in q8:
                        return False
                    q8.add(valore)
                elif 6 <= j <= 8:
                      if valore in q9:
                        return False
                      q9.add(valore)


    return True


risultato= validita(tabella)
if risultato:
  print("La tabella fornita è un sudoku")
else:
  print("La tabella fornita NON è un sudoku")




# ==========================================
# 2. CANDIDATI
# ==========================================
candidati_tot= { 1, 2, 3, 4, 5, 6, 7, 8, 9 }

def candidati(sudoku):
#candidati colonne e righe
    griglia2= [ riga[:] for riga in sudoku]
    for i in range(9):
        for j in range(9):
           valore= sudoku[i][j]
           if valore == 0:
               nrico= set()
               for k in range(9):
                   if sudoku [i][k] !=0:
                     nrico.add(sudoku[i][k])
                   if sudoku[k][j] != 0:
                     nrico.add(sudoku[k][j])
               
                   
#candidati quadrato 3x3, facciamo diventare ogni 3x3 un sudoku
               inizioriga= (i//3)*3
               iniziocolonna = (j//3)*3
               for l in range(3):
                   for m in range(3):
                       valoreq= sudoku[inizioriga + l][iniziocolonna + m]
                       if valoreq != 0:
                           nrico.add(valoreq)
                
               candidati_ij = candidati_tot - nrico
               griglia2[i][j] = candidati_ij
            

               
    return griglia2


# ==========================================
# 3. SVOLGIMENTO
# ==========================================            
def singoli(sudoku):
        modificato = False
        griglia_candidati = candidati(sudoku)
        #ricerca caselle singole
        for i in range(9):
            for j in range(9):
                if ( isinstance(griglia_candidati[i][j], set) and len(griglia_candidati[i][j])==1 ):
                    numero = list(griglia_candidati[i][j])[0]
                    sudoku[i][j]= numero
                    modificato = True
        return  sudoku, modificato       
                    
def loopsingoli(sudoku):
    modificato= True
    while modificato:
         sudoku, modificato = singoli(sudoku)
    return sudoku
        





# ==========================================
# 4. ESECUZIONE
# ==========================================
if validita(tabella):
    risultato = loopsingoli(tabella)
    
 # Stampiamo la tabella riga per riga
 
    print("Il sudoku finale:")
    for riga in risultato:
        print(riga)

else:
    print("Il sudoku richiesto non può essere svolto")
        
   

         
            
    
    
                





















