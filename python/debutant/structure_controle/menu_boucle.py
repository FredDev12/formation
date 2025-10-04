"""
Afficher un menu (
1 = addition, 2 = soustraction, 
3 = multiplication, 4 = division, 5 = quitter).
Tant que l'utilisateur n'appuie pas sur 5,
exécuter l'opération demandée
"""
choix = 0
while choix != 5:
    print("Menu :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    try:
        choix = int(input("Entrez votre choix : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    if choix in [1, 2, 3, 4]:
        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Veuillez entrer des nombres valides.")
            continue

        if choix == 1:
            print(f"Résultat : {a} + {b} = {a + b}")
        elif choix == 2:
            print(f"Résultat : {a} - {b} = {a - b}")
        elif choix == 3:
            print(f"Résultat : {a} * {b} = {a * b}")
        elif choix == 4:
            if b == 0:
                print("Erreur : division par zéro.")
            else:
                print(f"Résultat : {a} / {b} = {a / b}")
    elif choix == 5:
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez réessayer.")
