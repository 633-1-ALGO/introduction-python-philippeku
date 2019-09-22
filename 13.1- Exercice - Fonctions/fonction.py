# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def freq_lettres(texte, tab_lettres):
    for i in range(0, len(tab_lettres[0])):
        tab_lettres[1][i] = texte.count((tab_lettres[0][i]))
    print(tab_lettres[1])


freq_lettres(texte, tab_lettres)
