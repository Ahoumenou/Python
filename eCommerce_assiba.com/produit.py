# from BaseDeDonnees import BaseDeDonnees
import mysql.connector

class Produit():  
    def create_produit(self, nom,qts):
        self.nom = input('Nom du Produit: ')
        while True:
            try:
                self.qts = int(input('Quantité du Produit: '))
                break  # Sortir de la boucle si la conversion en entier est réussie
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        # self.qts = int(input('quantité du Produit: '))
        # Se connecter à la base de données
        mysdb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="mydatabase"
        )
        mycursor = mysdb.cursor()

        # Insérer des données dans la table "Produits"
        mycursor.execute("INSERT INTO Produits (nom_produit, prix) VALUES (%s, %s)", (self.nom, self.qts))
        mysdb.commit()
        self.cmd = input('Voulez encore de Produits ?: Oui/Non ')
        if(self.cmd == 'Oui'):
            self.create_produit("","")
        else:
            exit


    
produit = Produit()

produit.create_produit("","")