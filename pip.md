## PIP og eksterne bibliotek

pip er et verktøy i python som brukes for å hente eksterne bibliotek som gir muligheter til å lage mer avanserte programmer enn ved å bruke kun det som følger med python biblioteket. 

Eksempler på biblioteker som er aktuell å bruke er:
- [Numpy](https://numpy.org/) som gir mange matematiske operasjoner.
- [Matplotlib](https://matplotlib.org/) som kan brukes for visualisering av grafer m.m.

Begge disse pakkene brukes i noen av eksempelene i matematikk.

## Steg for Steg installering av PIP og Numpy + Matplotlib

#### 1. Python må være installert
Hvis ikke dette er gjort, må Python være lastet ned til den lokale maskinen din. Python finner du på [python.org](https://www.python.org/).

For å sjekke om Python er installert, kan man prøve å skrive python i kommandovinduet til windows eller terminal på mac.
- På windows: Trykk windowstasten og søk etter cmd.
- På mac: Finder -> Applications -> Terminal

Skriv så inn følgende kommando:
python
og trykk enter.

Hvis python er installert kommer det da opp noe slikt som dette:
```
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
Hvis python ikke er installert, eller ikke registrert ved installasjon som en kommando i Windows, kommer meldingen:
```
Python is not recognized as an internal or external command, operable program or batch file.
```

#### 2. Sjekk om PIP allerede er installert
Skriv inn følgende kommando i kommandovinduet/terminal: 
```
pip --version
```
og trykk enter. Hvis det kommer opp en en tekst som sier pip og versjonsnummer, så er PIP allerede innstallert, og du kan hoppe til steg 4.

#### 3. Installering av PIP
1. Last ned [get-pip.py](https://bootstrap.pypa.io/get-pip.py) til en mappe på maskinen.
2. Åpne kommandovindu/terminal og naviger til mappen get-pip.py er lastet ned til (kommando "cd mappenavn" - eksempelvis: cd C:\Users\Username\Downloads)
3. Skriv inn kommandoen: 
```
python get-pip.py
```

Se at det kommen en nedlastingsmelding i kommandovinduet / terminalen. Når dette er gjort, så kan man skrive inn kommandoen: 
```
pip --version
```
for å se om pip har blitt installert.

#### 4. Installering av Numpy og Matplotlib
Etter pip er installert, kan eksterne bibliotek i python bli installert med kommandoen:
```
pip install <pakkenavn>
```

For å installere numpy og matplotlib skrives følgende kommandoer inn:
```
pip install numpy
```
og
```
pip install matplotlib
```

#### 5. Bruk Numpy og Matplotlib i python program
Når numpy og matplotlib er installert, kan de importeres som andre bibliotek i python filer som lages ved å bruke import kodeordet:

```python
import numpy
import matplotlib
```

Dette vil dere kjenne igjen i noen av eksemplene.