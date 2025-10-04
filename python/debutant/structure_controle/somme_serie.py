"""
calculer la somme des entier 
de 1 a N N est fourni par l'utilisateur
"""
N = int(input("Entrez un nombre entier positif : "))
somme = 0
for i in range(1, N + 1):
    somme += i
print("La somme des entiers de 1 à", N, "est :", somme)
