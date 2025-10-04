"""
Demander deux nombre et 
afficher lequel est plus grand, 
ou s'ils sont egaux
"""

a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

if a > b:
    print(f"Le nombre {a} est plus grand que {b}.")
elif a < b:
    print(f"Le nombre {b} est plus grand que {a}.")
else:
    print(f"Les deux nombres sont égaux.")