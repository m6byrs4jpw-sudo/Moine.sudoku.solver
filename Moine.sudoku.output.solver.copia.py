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
# 3.1 SVOLGIMENTO
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
# 3.2 TECNICA DOUBLE-PAIRS
# ==========================================

def doublepairs(sudoku):
    sudoku = loopsingoli(sudoku)
    griglia_candidati2= candidati(sudoku)
    inserito_newnumber = False

# DOUBLE-PAIRS, controllo sulle RIGHE
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
             cell1 = griglia_candidati2[i][j]
             cell2 = griglia_candidati2[i][k]
 #dopo aver trovato sulle righela coppia in comune, creo un terzo for che elimina i candidati dalle altre celle   
             if ( isinstance( cell1, set) and isinstance( cell2, set)):
                 if len(cell1)== 2 and len(cell2)==2 and cell1== cell2:
                     coppia= cell1
                     for h in range(9):
                         if j != h and k != h:
                             cell3 =  griglia_candidati2[i][h]
                             if (isinstance (cell3, set)):
                                 griglia_candidati2[i][h] = cell3- cell1

# DOUBLE-PAIRS, controllo sulle COLONNE
    for j in range(9):
        for i in range (9):
           for k in range (i+1, 9):
                cell4= griglia_candidati2[i][j]
                cell5 = griglia_candidati2[k][j]
  #dopo aver trovato sulle colonne la coppia in comune, creo un terzo for che elimina i candidati dalle altre celle                               
                if (isinstance(cell4, set) and isinstance(cell5, set)):
                  if len(cell4)==2 and  len(cell5)==2 and cell4== cell5:
                    coppia= cell4
                    for h in range(9):
                      if i!= h and k!= h:
                        cell6= griglia_candidati2[h][j]
                        if (isinstance( cell6, set)):
                                 griglia_candidati2[h][j]= cell6 - coppia

# DOUBLE-PAIRS, controllo sui QUADRATI 3X3
    for i in range(0,9,3):
       for j in range(0,9,3):                          
        candidati_blocco= []
        posizioni_blocco = []
        for a in range(3):
          for b in range(3):
             riga_reale= i + a
             colonna_reale = j + b                    
             candidati_blocco.append(griglia_candidati2[riga_reale][colonna_reale])
             posizioni_blocco.append((riga_reale,colonna_reale))                    
                                 
  #ora il sudoku 9x9 è diventato 3x3, quindi agiamo normalmente come in precedenza                               
        for c in range(9):
            for d in range(c+1,9):
                   cell1 = candidati_blocco[c]                  
                   cell2 = candidati_blocco[d]
                   if ( isinstance( cell1,set) and isinstance( cell2, set)):
                     if len(cell1)==2 and len(cell2)== 2 and cell1== cell2:
                       candidato_singolo1 = list(cell1)[0]
                       candidato_singolo2 = list(cell1)[1]

                       for e in range(9):
                        if c != e and d!= e:
                          riga_pulita, colonna_pulita = posizioni_blocco[e]
                          cell3 = griglia_candidati2[riga_pulita][colonna_pulita]
                          if (isinstance( cell3, set)):
                                   griglia_candidati2[riga_pulita][colonna_pulita]= cell3.discard(candidato_singolo1)
                                   griglia_candidati2[riga_pulita][colonna_pulita]= cell3.discard(candidato_singolo2)

      
    for i in range(9):
           for j in range(9):
             if (isinstance(griglia_candidati2[i][j], set) and len(griglia_candidati2[i][j])==1):
                 numero = list(griglia_candidati2[i][j])[0]
                 sudoku [i][j] = numero 
                 inserito_newnumber = True
    
    sudoku = loopsingoli(sudoku)
    return sudoku
                 




# ==========================================
# 4. ESECUZIONE
# ==========================================
if validita(tabella): 
    cambiamento = True
    while cambiamento:
        tabella_precedente = [riga[:] for riga in tabella]
        tabella = doublepairs(tabella)
        if tabella == tabella_precedente:
          break;
 # Stampiamo la tabella riga per riga
 
    print("Il sudoku finale:")
    for riga in candidati(tabella):
        print(riga)

else:
    print("Il sudoku richiesto non può essere svolto")
        
