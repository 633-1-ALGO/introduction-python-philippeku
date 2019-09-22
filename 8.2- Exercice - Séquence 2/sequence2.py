# Problème : Calculer le prix TTC d'un nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75
prix_ttc = (prix_ht + (prix_ht * 7.7) / 100) * nb_articles

print("Le prix total TTC est de " + str(prix_ttc) + " chf.")
