from datetime import datetime, timedelta


class Commande:
    
    def __init__(self, date, numero, prix=0.0):
        self.date = date
        self.numero = numero
        self.prix = prix
        print("Commande créée le", self.date, "n°", self.numero, "au prix de", self.prix, "euros")
        
    def get_date(self):
        return self.date

    def set_date(self, date):
        self._date = date

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_prix(self):
        return self.prix

    def set_prix(self, prix):
        self.prix = prix

    def __str__(self):
        return f"Commande {self.numero} du {self.date}, prix : {self.prix}"
    
    def calculerTVA(self):
        return self.prix * 19.6 / 100
    
    def add(self, autre):
        if self.numero > autre.numero:
            commandeNew = Commande(self.date, self.numero+1, self.prix)
            # date plus 1
            commandeNew.prix += autre.prix
            return commandeNew
        else:
            commandeNew = Commande(autre.date, autre.numero+1, autre.prix)
            # date plus 1
            commandeNew.prix += self.prix
            return commandeNew
        
                
        
class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        print("Client créé :", self.nom, "domicilié à", self.adresse)
        
    def get_nom(self):
            return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self._adresse = adresse

    def __str__(self):
        return f"Client {self._nom}, adresse : {self._adresse}"
    
    
    
class CommandeAcquittee(Commande):
    
    def __init__(self, date, numero, prix=0.0, date_paiement=None):
        super().__init__(date, numero, prix)
        self.date_paiement = date_paiement
        print("et acquittée le", self.date_paiement)

            
    def acquitter(self):
        self.date_paiement = datetime.now().strftime('%Y-%m-%d')
        return CommandeAcquittee(self.date, self.numero, self.prix, self.date_paiement)
    
commande1 = CommandeAcquittee("2022-03-10", 1, 100.0)
commande2 = CommandeAcquittee("2022-03-11", 2, 120.0)

print(commande1)
print(commande2)

commande1_acquittee = commande1.acquitter()

print(commande1_acquittee)
