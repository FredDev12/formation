"""
Demander deux nombres à l'utilisateur 
et afficher leurs valeurs 
après les avoir échangées
"""

a = input("Entrez le premier nombre : ")
b = input("Entrez le deuxième nombre : ")

# Échange des valeurs
a, b = b, a

print("Après échange :")
print("Premier nombre :", a)
print("Deuxième nombre :", b)
