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
