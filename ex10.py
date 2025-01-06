notes = input("Entrer plusieurs notes séparées par des virgules : ")
liste = [float(note) for note in notes.split(',')]
moyenne = sum(liste)/len(liste)
print(f"La moyenne est de {moyenne}")