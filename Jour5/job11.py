def tri_bulle(liste):
    n = 0
    for x in liste:
        n += 1
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
liste_triee = tri_bulle(L)
print("Liste triée:", liste_triee)