print ("Veuillez choisir l'opération:")
print ("+")
print ("-")
print ("*")
print ("/")

operation = input()

nombre1 = int(input("Entrez le premier nombre:"))
nombre2 = int(input("Entrez le deuxième nombre:"))

if ( operation == "+"):
    print(("La réponse est:", nombre1 + nombre2))
elif ( operation == "-"):
    print(("La réponse est:", nombre1 - nombre2))
elif ( operation == "*"):
    print(("La réponse est:", nombre1 * nombre2))
elif ( operation == "/"):
    if (nombre2 != 0):
        print(("La réponse est:", nombre1 / nombre2))
    else : print("On ne peut pas diviser par zéro")