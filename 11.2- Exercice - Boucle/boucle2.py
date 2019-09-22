# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]


def tri_par_insertion(tab):
    for i in range(0, len(B)):
        cle = tab[i]
        j = i - 1
        while j >= 0 and cle <= tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
            tab[j + 1] = cle


tri_par_insertion(B)

print(B)
