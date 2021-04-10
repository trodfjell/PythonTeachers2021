#Enkel implementasjon i python av flytdiagrammet "Flytdiagram eksempel.png"

print('Regner det ute? (For enkelhetsskyld så tolkes teksten ja som True på spørsmålene, mens alt annet av input tolkes som False)')
svar = input()
if (svar.lower() == 'ja' ):
    print('Har du paraply?')
    svar = input()

    if (svar.lower() == 'nei'):

        while True:
            print('Vent en stund...')
            print('Regner det fortsatt?')
            svar = input()
            if svar.lower() == 'nei':
                break

print('Du kan nå gå ut.')
