# For løkker kan brukes for å kjøre noe en gitt antall ganger
print('Summer sammen alle tallene fra 1 til og med 100')
total = 0
for i in range(101):
    total = total + i
print(total)

# Dette kan også løses med en while løkke
print('Summer sammen alle tallene fra 1 til og med 100')
total = 0
i = 0
while i < 100:
    i = i + 1
    total = total + i
print(total)

# Vi kan også løse dette med en for løkke som teller baklengs
print('Summer sammen alle tallene fra 1 til og med 100')
total = 0
for i in range(100, 0, -1): # Start på 100, stop på 0, tell en ned hver gang løkken kjøres
    total = total + i
print(total)