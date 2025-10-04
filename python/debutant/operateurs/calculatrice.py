"""
Demander deux nombre et afficher
la somme, la difference, le produit, le quotient
"""

a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

s= a+ b
d= a-b
p=a*b
q=a/b

print(f"la somme de {a} + {b} =", s)
print(f"la difference de {a} - {b} =", d)
print(f"le produit de {a} * {b} =", p)
print(f"le quotient de {a} / {b} =", q)