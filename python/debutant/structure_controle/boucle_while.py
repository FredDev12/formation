"""
Demander a l'utilisateur un mot de passe 
jusaqu'a ce qu'il entre le bon
"""
mot_de_passe = "python123"
saisie = input("Entrez le mot de passe : ")

while saisie != mot_de_passe:
    print("Mot de passe incorrect. Essayez encore.")
    saisie = input("Entrez le mot de passe : ")

print("Mot de passe correct !")