"""
Demander une phrase et compter
combien de voyelles elle contient
"""
phrase = input("Entrez une phrase : ")
voyelles = "aeiouyAEIOUY"
compteur = 0

for lettre in phrase:
    if lettre in voyelles:
        compteur += 1

print("Le nombre de voyelles dans la phrase est :", compteur)
