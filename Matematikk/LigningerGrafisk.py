# Dette er et mer avansert eksempel på hvordan man kan løse ligningssett og krever installasjon av tilleggsmodulene numpy og matplotlib på den maskinen koden skal kjøre på.

import numpy as np # Import numpy og gi den aliaset np
import matplotlib.pyplot as plt # Import matplotlib.pyplot og gi den aliaset plt

# Funskjon nr 1: y = 6x + 120
def f1(x):
    return 6 * x + 120 

# Funksjon nr 2: y = 3x + 150
def f2(x):
    return 3 * x + 150

x = np.linspace(0, 30, 60) # Hent 60 verdier mellom 0 og 30

y1 = f1(x) # evaluer f1(x) på disse 60 ulike verdiene
plt.plot(x, y1) # plot den inn i grafen

y2 = f2(x) # evaluer f2(x) på disse 60 ulike verdiene
plt.plot(x, y2) # plot den inn i grafen

plt.show() # vis grafen

