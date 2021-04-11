#if, elif og else er condition statements som kan brukes for å styre hvilken kode som skal kjøre ut i fra et eller annet utsagn

# Blokken inne i if statmenten kjøres gitt at den boolske sjekken i if er lik True. Så her vil print('Hei, Ole!') kjøres hvis variabelen name er lik 'Ole'.
name = 'Ole'
if name == 'Ole':
    print('Hei, Ole!')
print("Done")

# Hvis man har behov for å kjøre noe kode gitt at if statementen evalueres til False, kan man bruke en else statement.
name = 'Kari'
if name == 'Ole':
    print('Hei, Ole!')
else:
    print('Du er ikke Ole!')
print("Done")

# Hvis man har behov for å ha flere sjekker som skal kjøres, så kan elif brukes. Dette er forkortelse for "else if" og evalueres kun hvis foregående if og elif statements er False.
name = 'Vigdis'
if name == 'Ole':
    print('Hei, Ole!')
elif name == 'Kari':
    print('Hei, Kari!')
else:
    print('Du er ikke Ole eller Kari!')
print("Done")

