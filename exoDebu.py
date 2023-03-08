import math

# # 2
# nom = input("Entrez votre nom : ")
# age = input("Entrez votre âge : ")
# print("Votre nom est : ", nom)
# print("Votre âge est : ", age)
# nom = str(nom)
# age = int(age)
# print("Votre nom est : ", nom)
# print("Votre âge est : ", age)


# # 3
# nombre = float(input("Entrez un nombre : "))
# if nombre >= 0:
#     racine_carree = math.sqrt(nombre)
#     print("La racine carrée de", nombre, "est", racine_carree)
# else:
#     print("Le nombre saisi doit être positif ou nul.")

# # 4
# mot1 = input("Entrez le premier mot : ")
# mot2 = input("Entrez le deuxième mot : ")
# if mot1 < mot2:
#     print(mot1, "est le plus petit.")
# elif mot2 < mot1:
#     print(mot2, "est le plus petit.")
# else:
#     print("Les deux mots sont égaux.")

# # 5
# pSeuil = 2.3
# vSeuil = 7.41
# pression = float(input("Entrez la pression courante de l'enceinte : "))
# volume = float(input("Entrez le volume courant de l'enceinte : "))
# if pression > pSeuil and volume > vSeuil:
#     print("Arrêt immédiat ! La pression et le volume sont supérieurs aux seuils.")
# elif pression > pSeuil:
#     print("Augmentez le volume de l'enceinte pour baisser la pression.")
# elif volume > vSeuil:
#     print("Diminuez le volume de l'enceinte pour baisser la pression.")
# else:
#     print("Tout va bien !")

# # 6
# chaine = input("Entrez une chaîne de caractères : ")
# if "@" in chaine and chaine.endswith(".com"):
#     print("C'est un email valide.")
# else:
#     print("Ce n'est pas un email valide.")

# # 7
# for i in range(10):
#     print("Ceci est un message affiché 10 fois.")
    
# # 8
# mot = input("Entrez un mot : ")
# for lettre in mot:
#     print(lettre)

# # 9
# a = 0
# b = 10
# while a < b:
#     print(a)
#     a += 1

# # 10
# b = 10;
# while b > 0:
#     b -= 1
#     if b % 2 == 1:
#         print(b)

# # 11
# nombre = 0
# while nombre < 1 or nombre > 10:
#     nombre = int(input("Entrez un entier entre 1 et 10 : "))
# print("Vous avez saisi", nombre)

# # 12
# chaine = input("Entrez une chaîne de caractères : ")
# for chatacter in chaine:
#         print(chatacter)
# list = input("Entrez une liste de nombres : ")
# for nombre in list:
#     print(nombre)
# for list in range(1,14,3):
#     print(list)

# # 13
# nombre = 3
# list = input("Entrez une liste de nombres : ")
# while nombre > list 
# 
#     for lettre in list:
#           if letter % 2 == 1:
#               print(letter)
#               nombre -= 1

# # 15
# liste = [17, 38, 10, 25, 72]
# liste.sort()
# liste.append(12)
# liste.reverse()
# print(liste.index(17))
# liste.remove(38)
# print(liste[1:3])
# print(liste[:2])
# print(liste[2:])
# print(liste[:])

# # 16
# chaine = "Hello World"
# inverse = chaine[::-1]
# print(inverse)

# # 17
# same avec if else si chaine == inverse

# # 18
# email = "dodo.so@example.com"
# if "@" in email and "." in email:
#     dot_index = email.rindex(".") # on récupère l'indice du dernier point
#     if len(email[dot_index+1:]) <= 3:
#         print("La chaîne est un email.")
#     else:
#         print("La chaîne n'est pas un email.")
# else:
#     print("La chaîne n'est pas un email.")
    
# # 19
# truc = []
# machin = [0.0] * 5

# # 20
# print(list(range(4)))
# print(list(range(4, 8)))
# print(list(range(2, 9, 2)))
# chose = list(range(6))
# print(3 in chose)
# print(6 in chose)

# # 21
# x = int(input("Entrez un nombre : "))
# with open("data.txt", "w") as f:
#     for i in range(x):
#         chaine = input("Entrez une chaîne de caractères : ")
#         f.write(chaine + "\n")

# # 22
