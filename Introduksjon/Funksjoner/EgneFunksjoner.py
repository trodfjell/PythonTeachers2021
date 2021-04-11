# Det er mulig å lage egne funksjoner i python. Dette er spesielt aktuelt hvis man ønsker å gjenta en lik oppførsel flere ganger. Kodeordet for å definere en blokk av kode som en funskjon er "def" etterfulgt av navnet på metoden og parantes.
def hallo():
    print('Hei')
    print('Hei')
    print('Hallo')

hallo()
hallo()
hallo()

# Det er også mulig å sende inn verdier til funsjoner. Dette kalles for parametre til metoden og oppfører seg på lik måte som variabler inne i selve funksjonen.
def hallo(navn):
    print('Hallo, ' + navn + '!')

hallo('Ola') # Hallo, Ola!
hallo('Kari') # Hallo, Kari!

# Det er også for funksjoner å returnere en verdi ut av funksjonen. Dette gjøres ved bruk av return statmenten.
def gangMedSegSelv(tall):
    return tall * tall

verdi = gangMedSegSelv(5) # verdi blir satt til 5 * 5 som er lik 25
print(verdi)

verdi = gangMedSegSelv(10) # verdi blir satt til 10 * 10 som er lik 100
print(verdi)