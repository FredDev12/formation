"""
Verifier si un nombre esntre
par l'utilisateur est positif(TRUE)
ou negatif(FALSE)
"""

nombre = float(input("entrez un nombre : "))

positif = nombre >= 0
print("Le nombre est positif :", positif)
negatif = nombre < 0
print("Le nombre est negatif :", negatif)  
