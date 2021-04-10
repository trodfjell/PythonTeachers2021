# While løkker kan brukes for å gjenta en blokk med kode så lenge evalueringen i while løkken er True

verdi = 0
while verdi < 3: # Kjør blokken i koden så lenge verdien er mindre enn 3
    print('Hei')
    verdi = verdi + 1 # pluss på 1 på variabelen verdi


# Obs på at man kan lage evige løkker som aldri vil stoppe
while True:
    print('Hei')


# Det er mulig å tvinge while løkker til å terminere ved bruk av kodeordet break
navn = ''
while True:
    print('Skriv inn ditt navn.')
    navn = input()
    if (navn == 'ditt navn'): # Hvis bruker skriver inn 'ditt navn', så stopper while løkken opp.
        break
print('Takk!')

# Det er også mulig å få while løkken til å hoppe tilbake til starten av løkken og evaluere
verdi = 0
while verdi < 5:
    verdi = verdi + 1
    if verdi == 3: # Hvis verdien er 3, hopper løkken tilbake til evalueringen "verdi < 5" og print linjen blir ikke skrevet ut
        continue
    print('verdien er ' + str(verdi))