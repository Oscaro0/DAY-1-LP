from random import randint
print("hello word")
x = randint(1,100)
n = 0
while x != n:
    n = int( input('Votre proposition: ') )
    if x < n: print("C'est moins.")
    elif x > n: print("C'est plus.")
    else: print("Bravo, vous avez trouvé le nombre !")