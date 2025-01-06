from random import randint
nb_mystere = randint(1,1000)
guess = int(input("Trouver le nombre entre 1 et 1000: "))
for i in range (10):
    if guess != nb_mystere:
        if guess < nb_mystere:
            print("Plus grand")
        elif guess > nb_mystere:
            print("Plus petit")
        guess = int(input())
if guess == nb_mystere:
    print("Bravo, vous avez trouvé le nombre mystère !")
else:
    print("Dommage, vous n'avez pas trouvé le nombre mystère !")