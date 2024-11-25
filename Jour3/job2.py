age = int(input("Quel est votre âge ? "))
if age >= 18:
    print("Tu peux voter.")
else:
    print("Tu ne peux pas voter.")

for i in range(101):
    if i == 26 or i == 37 or i == 88:
        continue
      
    print(i)
        