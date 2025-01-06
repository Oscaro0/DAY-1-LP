from random import randint
clavier_caracteres_ascii = [chr(i) for i in range(32, 127)]
longueur = int(input("Entrer la longueur du mot de passe : "))
mot_de_passe = ""
for i in range(longueur):
    nombre = randint(0, len(clavier_caracteres_ascii) - 1)
    mot_de_passe += clavier_caracteres_ascii[nombre]
print(mot_de_passe)