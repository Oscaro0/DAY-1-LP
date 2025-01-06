liste = (input("Entrer une liste de nombres séparés par des virgules : "))
liste = [float(i) for i in liste.split(",")]
print(sorted(liste))