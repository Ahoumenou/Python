import mysql.connector

class Command():
    def demande(self,produit_id, nom, prenom, produits, prix, Qts):
        mysdb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="mydatabase"
        )
        mycursor = mysdb.cursor()
        while True:
            try:
                produit_id = int(input('La Position du Produit: '))
                break  # Sortir de la boucle si la conversion en entier est réussie
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        nom = input('Nom du Client: ')
        prenom = input('Prenom du Client: ')
        produit = int(input('Produit commandé: ')) 
        while True:
            try:
                prix = int(input('le Prix du Produit: '))
                Qts = int(input('Le Nombre du Produit: '))
                break  # Sortir de la boucle si la conversion en entier est réussie
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        # self.qts = int(input('quantité du Produit: '))
        # Se connecter à la base de données
        

        mycursor.execute("INSERT INTO Clients (produit_id, nom, prenom, produits, prix, Qts) VALUES (%s, %s, %s, %s, %s, %s)",
        (produit_id, nom, prenom, produit, prix, Qts))
        mysdb.commit()

        # self.cmd = input('Voulez encore de Produits ?: Oui/Non ')
        # if(self.cmd == 'Oui'):
        #     self.create_produit("","")
        # else:
        #     exit




        # while True:
        #     try:
        #         self.produit_id = int(input('Quel est la position de Prduit que voulez vous: '))
        #         break
        #     except:
        #         print('Veuillez entrer un nombre Valide')
        
        # self.nom = input('Nom du Client: ')
        # self.prenom = input('Prenom du Client: ')
        # while True:
        #     try: 
        #         self.produit = int(input('Produit commandé: ')) 
        #         self.prix = int(input('le Prix du Produit: '))
        #         self.Qts = int(input('Le Nombre du Produit: '))
        #         break
        #     except:
        #         print('Veuillez entrez un nombre valide')
            
        # mysdb = mysql.connector.connect(
        #     host = '127.0.0.1',
        #     username = 'root',
        #     password = '',
        #     database = 'mydatabase',
        # )

        # mycursor = mysdb.cursor()

        # mycursor.execute()

        # # Insérer des données dans la table "Clients"
        

Command.demande('','','','','','','')