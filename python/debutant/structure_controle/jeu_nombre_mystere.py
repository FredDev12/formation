"""
stocker un nombre secret dans une variable
l'utilisateur propose un nombre
afficher trop petit, trop grand ou Bravo
"""

nombre_secret = 42  # Vous pouvez changer ce nombre pour le rendre plus difficile à deviner
nombre_propose = int(input("Proposez un nombre entre 1 et 100 :"))

if nombre_propose < nombre_secret:
    print("Trop petit !")
elif nombre_propose > nombre_secret:
    print("Trop grand !")
else:
    print("Bravo ! Vous avez trouvé le nombre.")