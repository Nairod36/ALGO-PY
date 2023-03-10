# La classe AB est une implémentation d'un arbre binaire.
class AB:
    #La méthode init définit la racine de l'arbre, son sous-arbre gauche et son sous-arbre droit. Si la racine est nulle, elle définit la racine comme étant nulle.
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = [racine] if racine is not None else None
        self.gauche = gauche
        self.droite = droite
    #La méthode str retourne la représentation en chaîne de caractères de l'arbre, selon le format (sous-arbre_gauche, racine, sous-arbre_droit).
    def __str__(self):
        if self.estVide():
            return ""
        elif self.gauche is None and self.droite is None:
            return str(self.racine[0])
        else:
            return "(" + str(self.gauche) + ',' + str(self.racine[0]) +',' + str(self.droite) + ")"

    #Getters et setters
    def get_racine(self):
        return self.racine
    
    def set_racine(self, racine):
        self.racine = racine
        
    def set_gauche(self, gauche):
        self.gauche = gauche
        
    def set_droite(self, droite):
        self.droite = droite
    
    #La méthode estVide renvoie vrai si la racine est nulle.
    def estVide(self):
        return self.racine is None
    #La méthode taille renvoie le nombre de nœuds dans l'arbre.
    def taille(self):
        if self.estVide():
            return 0
        else:
            taille_gauche = 0
        if self.gauche is not None:
            taille_gauche = self.gauche.taille()
        taille_droite = 0
        if self.droite is not None:
            taille_droite = self.droite.taille()
        return 1 + taille_gauche + taille_droite
    #Les méthodes prefixe, infixe et suffixe renvoient la liste des valeurs des nœuds parcourus respectivement en parcours préfixe, infixe et postfixe.
    def prefixe(self):
        if self.estVide():
            return []
        else:
            prefixe_gauche = []
        if self.gauche is not None:
            prefixe_gauche = self.gauche.prefixe()
        prefixe_droite = []
        if self.droite is not None:
            prefixe_droite = self.droite.prefixe()
        return [self.racine[0]] + prefixe_gauche + prefixe_droite
    
    def sufixe(self):
        if self.estVide():
            return []
        else:
            sufixe_gauche = []
        if self.gauche is not None:
            sufixe_gauche = self.gauche.sufixe()
        sufixe_droite = []
        if self.droite is not None:
            sufixe_droite = self.droite.sufixe()
        return sufixe_gauche + sufixe_droite + [self.racine[0]]
    
    def infixe(self):
        if self.estVide(): #vérifie si l'arbre est vide, auquel cas elle retourne une liste vide
            return []
        else:
            infixe_gauche = [] #initialise une liste vide pour les éléments dans le sous-arbre gauche
        if self.gauche is not None: #vérifie si le sous-arbre gauche existe et appelle la méthode infixe() sur ce sous-arbre. 
            #La liste retournée est stockée dans la variable infixe_gauche.
            infixe_gauche = self.gauche.infixe()
        infixe_droite = [] #initialise une liste vide pour les éléments dans le sous-arbre droite
        if self.droite is not None:
            infixe_droite = self.droite.infixe()
        return infixe_gauche + [self.racine] + infixe_droite
    
    #La méthode hauteur renvoie la hauteur de l'arbre.
    def hauteur(self):
        if self.estVide():
            return -1
        else:
            if self.gauche is not None:
                h_gauche = self.gauche.hauteur()
            else:
                h_gauche = -1
            if self.droite is not None:
                h_droite = self.droite.hauteur()
            else:
                h_droite = -1
            return 1 + max(h_gauche, h_droite)
    #La méthode estEquilibre renvoie vrai si l'arbre est équilibré, 
    # c'est-à-dire que la différence de hauteur entre ses sous-arbres gauche et droit est inférieure ou égale à 1.
    def estEquilibre(self):
        if self.estVide():
            return True

        hauteur_gauche = self.gauche.hauteur() if self.gauche is not None else -1
        hauteur_droite = self.droite.hauteur() if self.droite is not None else -1

        if abs(hauteur_gauche - hauteur_droite) > 1:
            return False

        if self.gauche is not None and not self.gauche.estEquilibre():
            return False

        if self.droite is not None and not self.droite.estEquilibre():
            return False

        return True
    #La méthode estABR renvoie vrai si l'arbre est un arbre binaire de recherche, 
    # c'est-à-dire que pour chaque nœud de l'arbre, 
    # tous les nœuds dans son sous-arbre gauche sont inférieurs à sa valeur 
    # et tous les nœuds dans son sous-arbre droit sont supérieurs à sa valeur.
    def estABR(self):
        if self.estVide():
            return True

        if self.gauche is not None and not self.gauche.estABR():
            return False
        if self.droite is not None and not self.droite.estABR():
            return False
    
        # sous-arbre gauche sont inférieurs à la racine
        if self.gauche is not None:
            for elem in self.gauche.sufixe():
                if elem > self.racine[0]:
                    return False
    
        # sous-arbre droit sont supérieurs à la racine
        if self.droite is not None:
            for elem in self.droite.prefixe():
                if elem < self.racine[0]:
                    return False
    
        return True


    #Dans les deux cas, 
    # la méthode retourne le nouveau pivot qui est désormais la nouvelle racine de l'arbre après la rotation.
    
    def rotation_droite(self):
        if self.gauche is None:
            return self
        pivot = self.gauche
        self.gauche = pivot.droite
        pivot.droite = self
        return pivot


    def rotation_gauche(self):
        if self.droite is None:
            return self
        pivot = self.droite
        self.droite = pivot.gauche
        pivot.gauche = self
        return pivot

