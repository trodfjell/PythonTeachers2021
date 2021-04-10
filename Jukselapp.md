### Skrive ut tekst
```python
print("Programmering er morsomt!")
```

### Kommentarer
Kommentarer kan brukes for å skrive informasjon om programmet, uten at dette er noe som kjøres i kode. Hver linje som starter på # ignoreres ved kjøring av programmet.
```python
#Dette er en kommentar
```

### Variabler
```python
navn = "Ola"
alder = 39
radius = 15.42
```

### Utregning
| Operator       | Python        |
| :------------  |:-------------:|
| Pluss          | +      |
| Minus          | -      |
| Multiplikasjon | *      |
| Divisjon       | /      |
| Potens         | **     |

### Skrive ut datatyper
```python
print(type(2))
print(type(3.14))
print(type("Tekst"))
```

### Betingelser
```python
tall = -15
if tall > 0:
    print("Tallet er positivt")
elif tall < 0:
    print("Tallet er negativt")
else:
    print("Tallet er lik null")
```

### Boolsk logikk
Alle boolske operatorer evaluerer til enten True eller False (sann eller usann).

#### Sammenlignings-operatorer
| Operator       | Python        |
| :------------  |:-------------:|
| Er lik          | ==      |
| Er ikke lik          | !=      |
| Mindre enn | <      |
| Større enn       | >      |
| Mindre enn eller lik         | <=    |
| Større enn eller lik | >= |

#### Boolske operatorer
Man kan i tillegg kombinere flere operatorer sammen ved bruk av operatorene and, or og not.
```python
True and True # True
True and False # False
False and True # False
False and False # False

True or True # True
True or False # True
False or True # True
False or False # False

not True # False
not False # True
```


### While løkker
```python
#Skriver ut tallene 0 til og med 9
tall = 0
while tall < 10:
    print(tall)
    tall += 1
```

### For løkker
```python
for i in range(5, 8):
    print(i, "*", i, "=", i ** 2)
print('Ferdig')
# 5 * 5 = 25
# 6 * 6 = 36
# 7 * 7 = 49
# ferdig
```

### Input fra bruker
```python
navn = input("Skriv inn ditt navn: ")
```

### Input med tall
```python
heltall = int(input("Skriv inn et heltall: "))
desimaltall = float(input("Skriv inn et desimaltall (. som skilletegn): "))
```

### Importering av eksterne bibliotek
Math biblioteket til Python kan hentes inn i enkelte program hvis man har behov for flere matematiske operatorer enn enkelt utregning. Eksempler på dette kan være kvadratrot (sqrt), sinus (sin), tangens (tan), cosinus (cos) m.m.

Dokumentasjon av math biblioteket finnes [her](https://docs.python.org/3/library/math.html "math - Mathematical functions")
```python
# Import av hele math biblioteket til python programmet
import math

# Import av kun deler av math biblioteket til python programmet
from math import sqrt
```
