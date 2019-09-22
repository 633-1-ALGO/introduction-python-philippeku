# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

max_val = 0
indice_i = 0
indice_j = 0

for i in range(0, len(tab)):
    #print(tab[i])
    for j in range(0, len(tab[i])):
        #print(tab[i][j])
        if tab[i][j] > max_val:
            max_val = tab[i][j]
            indice_i = i
            indice_j = j
print("La valeur maximum est : " + str(max_val) + " et elle se trouve à l'indice [ " + str(indice_j) + " ] [ " + str(indice_j) + " ]")
