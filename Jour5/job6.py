L = [8, 24,48,2,16]

def count_multiple(L):
    count = 0
    for i in L:
        if i % 3 == 0:
            count += 1
    return count

print(count_multiple(L))