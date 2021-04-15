#Skisser grafen av polynomfunskjonen 2x^3 - x^2 - 7x + 6

import numpy as np # Import numpy og gi den aliaset np
import matplotlib.pyplot as plt # Import matplotlib.pyplot og gi den aliaset plt

# Definer funskjonen med python syntax
def f(x):
    return 2 * x ** 3 - x ** 2 - 7 * x + 6

x = np.linspace(-4, 4, 50) # Hent 50 verdier mellom -4 og 4

y = f(x) # evaluer f1(x) på disse 50 ulike verdiene
plt.plot(x, y) # plot den inn i grafen

# Horisontal og vertikal linje der hvor x og y er lik 0
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')

plt.show()