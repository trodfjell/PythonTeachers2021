#Enkel implementasjon i python av flytdiagrammet "Flytdiagram eksempel.png"

print('Regner det ute?
svar = input()
if (svar.lower() == 'ja' ):
    print('Har du paraply?')
    svar = input()

    if (svar.lower() == 'nei'):
        fortsattRegn = True
        while fortsattRegn:
            print('Vent en stund...')
            print('Regner det fortsatt?')
            fortsattRegn = input()
            if fortsattRegn.lower() == 'nei':
                fortsattRegn = False
        
print('Du kan nå gå ut.')
