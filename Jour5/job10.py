L = [7, 11, 42, 39, 2]

def add_one(L):
    for i in range(len(L)):
        L[i] += 1
    return L

print(add_one(L))
