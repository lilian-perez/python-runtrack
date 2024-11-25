L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def calcul_even(L):
    even_numbers = []
    for i in L:
        if i % 2 == 0:
            even_numbers.append(i)
    return sum(even_numbers)

print(calcul_even(L))