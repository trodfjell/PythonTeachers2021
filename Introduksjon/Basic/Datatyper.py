# Vi vil i dette kurset se primært på 3 datatyper som følger med python, disse er Int, Float og String

# String brukes for å representere tekst
'Dette er en tekst'

# Int brukes for å representere heltall
1
10

# Float brukes for å representere flyttall. I Python er punktum skilletegnet for desimaler.
16.5
10.0

# Vær obs på at flyttall ikke alltid er helt presis når det kommer til utregning på desimaler. 
# Eksempelvis hvis man summerer sammen 0.1 + 0.2 så får man i python (og de fleste andre programmeringsspråk) svaret: 0.30000000000000004
# Dette kan leses mer om her: https://no.wikipedia.org/wiki/Flyttall

# Alternativ til flyttall er å bruke Decimal typen hvis man har behov for å ha helt korrekt presisjon.
from decimal import *
Decimal('0.1') + Decimal('0.2') # => Decimal(0.3)

# Det er også mulig å konvertere datatyper mellom hverandre

# Konvertering av Int og Float til String
str(1) # => '1'
str(15.5) # => '15.5'

# Konvertering av String og Float til Int
int('15') # => 15
int(15.5) # => 15 (Desimalen kuttes bort)
int('abc') # => Gir feilmelding

# Konvertering av String og Int til Float
float(15) # => 15.0
float('15') # => 15.0
float('abc') # => Gir feilmelding

# Det er også mulighet å skrive ut hvilken datatype en verdi har. Dette gjøres gjennom kodeordet type.
type(15) # <class 'int'>
type(15.0) # <class 'float'>
type('abc') # <class 'str'>

# Alle operatorene som nevnt i Operatorer.py kan også brukes på String datatypen.
'Alice' + 'Bob' # => 'AliceBob'
'Hei' + '!' * 10 # => 'Hei!!!!!!!!!!'
