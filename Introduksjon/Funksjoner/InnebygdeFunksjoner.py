# Python har en rekke innebygde funksjoner som kan brukes
print('Hei') # Print funksjonen som skriver ut tekst
input() # Input funksjonen som ber brukeren å skrive inn noe 
len('Hei') # Len funksjonen som skriver ut lengden av noe

# Det finnes også en rekke andre moduler som kan inkluderes, men disse må importeres ved behov. Disse er med andre ord ikke innebygget. Et eksempel på dette er math biblioteket som inneholder en rekke matematiske funskjoner.
# For klaring av alle funksjonene til math finnes her: https://docs.python.org/3/library/math.html
import math

#Eksempler:
math.sqrt(9) # => kvadratroten av 9 => 3.0
math.exp(5) # => basen til naturlige logaritmer e opphøyd i 5 => 148.4131591025766
math.log(148.4131591025766) # => log 148.41... som er lik 5.0
math.hypot(3, 4) # hypotenus av katetene 3 og 4

#Math bibliteket inneholder også noen matematiske konstanter som kan brukes:
math.pi # 3.141592…
math.e # 2.718281…
math.tau # 6.283185…

# Det finnes også andre 3. parts biblioteker som kan innstalleres, men disse gjennomgår vi ikke her.