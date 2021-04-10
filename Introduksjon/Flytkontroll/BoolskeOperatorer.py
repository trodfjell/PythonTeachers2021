#Alle boolske operatorer evalueres enten til sann (True) eller usann (False).
print(True)
print(False)

# Er lik
print(True == True) # True
print(12 == 12.0) # True
print(12 == 11) # False

# Er ikke lik
print(True != True) # False
print(12 != 12.0) # False
print(12 != 11) # True

# Er større enn
print(12 > 11) # True
print(12 > 12) # False
print(12 > 13) # False

# Er mindre enn
print(12 < 11) # False
print(12 < 12) # False
print(12 < 13) # True

# Er større enn eller lik
print(12 >= 11) # True
print(12 >= 12) # True
print(12 >= 13) # False

# Er mindre enn eller lik
print(12 <= 11) # False
print(12 <= 12) # True
print(12 <= 13) # True

# Obs: Tekst og tall kan ikke sammenlignes direkte, men tall kan sammenlignes med hverandre selv om de ikke er samme datatype.
print('12' == 12) # False
print(12.0 == 12) # True


# Det er også mulig og kombinere flere verdier for sammenligning. Dette gjøres med operatorene and, or og not.
alder = 33
dyr = 'katt'
print(alder == 33 and dyr == 'katt') # True
print(alder == 33 or dyr == 'katt') # True
print(alder == 33 and not dyr == 'katt') # False