from ProjetArbreDorianM import AB

# A1 = AB()
# print("A1 est vide ?", A1.estVide()) 

# A2 = AB(racine=5)
# print("A2 est vide ?", A2.estVide())

# A3 = AB(racine=3)

# A2.set_gauche(A3)

AtestG1 = AB(racine=3)

AtestG2 = AB(racine=8)

AtestG1D = AB(racine=4)

AtestG2D = AB(racine=6)

AtestG = AB(racine=5, gauche= AtestG1, droite=AtestG2)

AtestD = AB(racine=12, gauche= AtestG1D, droite=AtestG2D)

Atest = AB(racine=10, gauche= AtestG, droite=AtestD )

# print("Atest est vide ?", Atest.estVide())

# print("Atest taille: ",Atest.estABR())


# print("Atest", Atest)
print(Atest.__str__())
print("Atest rotate droite", Atest.rotation_droite())
# print("Atest new", Atest)
