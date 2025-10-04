"""
Demander l'âge d'une personne et vérifier
si elle a entre 18 et 30 ans.
Afficher True ou False selon la condition.
"""

age = int(input("Entrez votre âge : "))

resultat = 18 <= age <= 30
print(resultat)
