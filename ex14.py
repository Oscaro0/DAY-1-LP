n = int(input("Entrer un nombre : "))
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
print(factorielle(n))