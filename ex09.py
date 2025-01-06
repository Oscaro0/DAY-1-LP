mot = input("Ecrivez un mot : ")
if len(mot) <= 1:  
    print("C'est un palindrome")
if mot[0] == mot[-1]:  
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")