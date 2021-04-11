# Dette programmet kan brukes for å finne lengden på en ukent side av en rettvinklet trekant
# Programmet ber først brukeren å fortelle om det er hypotenusen eller et av katetenes lengde som er ukjent
# Så ber den om lengden på begge katetene eller hypotenusen og kateten
# Så regner den seg frem til lengden av den ukjente siden
import math

print('Hvilken side av den rettvinklede trekanten er ukjent? (hypotenus/katet)')
ukjent = input()

if (ukjent.lower() == 'hypotenus'):
    a = float(input('Hva er lengden av første katet? '))
    b = float(input('Hva er lengden av andre katet? '))
    c = math.sqrt(a ** 2 + b ** 2)

    print('Lengden av hypotenus er ' + str(c))

elif (ukjent.lower() == 'katet'):
    c = float(input('Hva er lengden av hypotenusen? '))
    a = float(input('Hva er lengden av en av katetene? '))
    b = math.sqrt(c ** 2 - a ** 2)

    print('Lengden av den ukjente kateten er ' + str(b))

else:
    print('Du må skrive enten hypotenus eller katet')