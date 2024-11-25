L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def between_calc(L):
    between = []
    for i in L:
        if i >= 25 and i <= 90:
            between.append(i)
    return sum(between)

print(between_calc(L))