N = int(input("Entrez un entier supérieur à zéro : "))
for i in range(1, N + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()