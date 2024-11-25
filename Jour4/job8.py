def moyenne(a, b, c):
    return (a + b + c) / 3

# Demander à l'utilisateur d'entrer ses notes
notes1 = float(input("Entre ta première note : "))
notes2 = float(input("Entre ta deuxième note : "))
notes3 = float(input("Entre ta troisième note : "))

# Calculer la moyenne des notes
moyenne_notes = moyenne(notes1, notes2, notes3)

# Vérifier la moyenne et afficher le message correspondant
if 0 < moyenne_notes <= 7:
    print("Élève devant faire des efforts")
elif 8 <= moyenne_notes <= 10:
    print("Élève moyen")
elif 11 <= moyenne_notes <= 14:
    print("Bon élève")
elif 15 <= moyenne_notes <= 20:
    print("Très bon élève")
else:
    print("Notes invalides")