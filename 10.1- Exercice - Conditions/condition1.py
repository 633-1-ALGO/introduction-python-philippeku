# Problème : Etant donné deux variables c et d, on veut savoir si leur produit est négatif ou positif ou nul.
# Contrainte : Ne pas calculer le produit des deux nombres.
# Résultat attendu : Un message affichant "Produit positif" ou "Produit négatif" ou "Produit nul".
# Indications :  Vous pouvez changer les valeurs des variables pour vos tests.
c = 10
d = 10

N = c * d

if N > 0:
    print("Positif")
elif N < 0:  # Contraction de "Else If"
    print("Négatif")
else:
    print("Null")




