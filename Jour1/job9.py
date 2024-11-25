produit = ['Baguette', 'Pain au chocolat', 'Croissant', 'Pain aux raisins']
quantité = [10, 15, 15, 10]
prix = [0.80, 1.20, 1.00, 1.20]

print("Produits disponibles :")
for i in range(len(produit)):
    print(f'{i + 1}. {produit[i]} - {quantité[i]} en stock - {prix[i]} € l\'unité')

choix = int(input("Entrez le numéro du produit que vous voulez acheter : ")) - 1

if 0 <= choix < len(produit):
    quantite_achat = int(input(f"Combien de {produit[choix]} voulez-vous acheter ? "))

    if quantite_achat <= quantité[choix]:
        quantité[choix] -= quantite_achat
        print(f"Vous avez acheté {quantite_achat} {produit[choix]}.")
    else:
        print("Désolé, nous n'avons pas assez de stock.")
else:
    print("Produit non valide.")

print(f"Il reste {quantité[choix]} {produit[choix]} en stock.")
