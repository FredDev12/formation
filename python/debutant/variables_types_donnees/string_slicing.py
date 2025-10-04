"""
Demander un mot et afficher
- la permiere lettre
- ladernier lettre
- le mot en majuscule
"""

mot = input("Entrez un mot : ")

premiere = mot[0]
derniere = mot[-1]
majuscule = mot.upper()

print("Premiere lettre :", premiere)
print("Derniere lettre :", derniere)
print("Mot en majuscule :", majuscule)