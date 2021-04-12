# Dette er et eksempel på hvordan ligningssett med 2 ukjente kan løses ved hjelp av python.
# Denne bruker decimal i stedet for float på grunn av flyttall kan være upresise når man summerer sammen desimaler
from decimal import *

# Funskjon nr 1: y = 6x + 120
def f1(x):
    return 6 * x + 120 

# Funksjon nr 2: y = 3x + 150
def f2(x):
    return 3 * x + 150

x = Decimal('0')
while x < 100:
    x = x + Decimal('0.1')
    if f1(x) == f2(x):
        print('Fant løsning:')
        print('x = ' + str(x))
        print('y = ' + str(f1(x)))
        break # Break som avslutter while løkken da løsning er oppnådd
    else:
        print("x er ikke lik " + str(x))