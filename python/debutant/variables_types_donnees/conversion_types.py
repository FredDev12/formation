"""
Demander un nombre a virgule et 
affciher sa partie entiere et 
sa partie decimale
"""

a = input("Entrez un nombre a virgule : ")

a = float(a)
partie_entiere = int(a)
partie_decimale = a - partie_entiere
print("Partie entiere :", partie_entiere)
print("Partie decimale :", partie_decimale)
print("Partie decimale (arrondie) :", round(partie_decimale, 2))
print("Partie decimale (formattee) : {:.2f}".format(partie_decimale))
print(f"Partie decimale (f-string) : {partie_decimale:.2f}")