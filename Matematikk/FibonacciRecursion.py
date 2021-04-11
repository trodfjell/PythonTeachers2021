# Dette programmet ber en bruker å skrive inn hvor mange siffer av fibonacci rekken han vil ha skrevet ut. Dette er samme funksjon som Fibonacci.py, men bruker noe som kalles for rekursjon.
# Rekursjon er når en funskjon kaller seg selv inne i funksjon.
# Fibonacci rekken er en tallrekke hvor det neste tallet er summen av de 2 foregående tallene: 0 1 1 2 3 5 8 13

def fiboRecur(n):
   if n <= 1:
       return n
   else:
       return(fiboRecur(n-1) + fiboRecur(n-2))

print('Hvor mange tall vil du vise?')
antall = int(input())

# check if the number of terms is valid
if antall <= 0:
   print("Du må skrive inn et positivt tall")
else:
   print("Fibonacci sekvensen:")
   for i in range(antall):
       print(fiboRecur(i))