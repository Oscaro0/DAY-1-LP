phrase = input("Rentrer une phrase sans accent : ")
phrase_min=phrase.lower() 
liste_voyelles=["a","e","i","o","u","y"]
nombre_voyelles = 0
for caractere in phrase.lower():  
    if caractere in liste_voyelles:
        nombre_voyelles += 1

print(f"Le nombre de voyelles dans la phrase est : {nombre_voyelles}")
