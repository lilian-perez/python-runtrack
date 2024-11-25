longueur1 = int(input("Entrez la première longueur : "))
longueur2 = int(input("Entrez la deuxième longueur : "))
longueur3 = int(input("Entrez la troisième longueur : "))


if longueur1 == longueur2 == longueur3:
    print("Le triangle est équilatéral.")

elif longueur1 == longueur2 or longueur2 == longueur3 or longueur1 == longueur3:
    
    if (longueur1**2 + longueur2**2 == longueur3**2 or
        longueur2**2 + longueur3**2 == longueur1**2 or
        longueur1**2 + longueur3**2 == longueur2**2):
        print("Le triangle est isocèle et rectangle.")
    else:
        print("Le triangle est isocèle.")

elif (longueur1**2 + longueur2**2 == longueur3**2 or
      longueur2**2 + longueur3**2 == longueur1**2 or
      longueur1**2 + longueur3**2 == longueur2**2):
    print("Le triangle est rectangle.")

else:
    print("Le triangle est quelconque.")
