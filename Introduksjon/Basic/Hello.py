# Dette programmet ber først brukeren om å skrive inn navnet sitt og sier hei til brukeren. 
# Programmet gir så informasjon om hvor langt navnet til brukeren er.
# Etter dette ber den om å få vite alderen til brukeren og skriver ut hvor gammel vedkommende blir på sin neste bursdag.

print('Hei')

print('Hva er ditt navn?') # Be brukeren om å skrive inn navnet sitt
navn = input()
print('Hyggelig å hilse på deg, ' + navn)
print('Lengden på ditt navn er:')
print(len(navn))

print('Hvor gammel er du?') # Be brukeren å skrive inn alderen sin
alder = input()
print('Du blir ' + str(int(alder) + 1) + ' år på din neste bursdag.')