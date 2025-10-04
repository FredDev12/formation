"""
Demander une note (0-20)
afficher :
Excellent si >= 16
bien si >= 12
passable si >= 8
echec sinon
"""

note = float(input("Entrez une note entre 0 et 20 : "))

if note >= 16:
    print("Excellent") 
elif note >= 12:
    print("Bien")
elif note >= 8:
    print("Passable")
else:
    print("Echec")