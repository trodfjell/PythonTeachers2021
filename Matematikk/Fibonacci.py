# Dette programmet ber en bruker å skrive inn hvor mange siffer av fibonacci rekken han vil ha skrevet ut
# Fibonacci rekken er en tallrekke hvor det neste tallet er summen av de 2 foregående tallene: 0 1 1 2 3 5 8 13

def fibonacci(antallNummer):
    n1 = 0
    n2 = 1
    count = 0

    if(antallNummer <= 0):
        print('Du må skrive inn et positivt tall')
    elif(antallNummer == 1):
       print("Fibonacci sekvensen opp til upto",antallNummer,":")
       print(n1)
    else:
        print("Fibonacci sequence:")
        while count < antallNummer:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

print('Hvor mange tall vil du vise?')
nAntall = int(input())

fibonacci(nAntall)