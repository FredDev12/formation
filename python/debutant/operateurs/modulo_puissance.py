"""
verifier si un nombre est pair ou impair avec %
calculer la puissance d'un nombre (ex: 2**3 = 2*2*2=8)
"""

nombre = int(input("Entrez un nombre entier : "))
puissance = int(input("Entrez la puissance : "))
pair = (nombre % 2) == 0
impair = (nombre % 2) != 0
resultat = nombre ** puissance
print(f"Le nombre {nombre} est pair : {pair}")
print(f"Le nombre {nombre} est impair : {impair}")
print(f"Le résultat de {nombre} à la puissance {puissance} est : {resultat}")