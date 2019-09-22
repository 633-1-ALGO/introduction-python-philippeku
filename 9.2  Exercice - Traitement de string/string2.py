# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

cpt = texte.count("exemple")

print("Il y'a " + str(cpt) + ' occurences du mot "exemple"')
print(texte.replace("est", "représente"))


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


print(reverse(texte))
