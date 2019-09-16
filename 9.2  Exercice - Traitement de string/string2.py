# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

cpt = texte.count("exemple")

print("Il y'a " [::-1] + str(cpt) + " occurences du mot exemple" [::-1])