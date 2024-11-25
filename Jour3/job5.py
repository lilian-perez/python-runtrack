number = int(input("Entre un chiffre ou un nombre : "))

if number % 2 == 0:
    print(f'{number} est un nombre pair')
else:
    print(f'{number} est un nombre impair')

    string = "abcdefghijklmnopqrstuvwxyz"

length = 1

while length <= len(string):
    print(string[:length])
    length += 2
