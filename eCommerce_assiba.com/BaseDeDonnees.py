import mysql.connector

class BaseDeDonnees():
    def __init__(self, host, username, password, port):
        self.host = host,
        self.username = username,
        self.password = password,
        self.port = port
    

    def connection(self):
        mysdb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
        )

        mycursor = mysdb.cursor()

        mycursor.execute("CREATE DATABASE mydatabase")
        for x in mycursor:
            print(x)
    def create_table(self):
        mysdb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="mydatabase"
        )
        mycursor = mysdb.cursor()
        mycursor.execute('CREATE TABLE Produits(id INT AUTO_INCREMENT PRIMARY KEY, nom_produit VARCHAR(225), prix INT)')
        mycursor.execute('CREATE TABLE Clients(id INT AUTO_INCREMENT PRIMARY KEY, produit_id INT, nom VARCHAR(225), prenom VARCHAR(225), produits VARCHAR(225), prix INT, Qts INT, FOREIGN KEY (produit_id) REFERENCES Produits(id))')
        mycursor.execute('CREATE TABLE Panier(id INT AUTO_INCREMENT PRIMARY KEY, produit_id INT, client_id INT, Qts INT, FOREIGN KEY (produit_id) REFERENCES Produits(id), FOREIGN KEY (client_id) REFERENCES Clients(id))')
        mycursor.execute('CREATE TABLE Facture(id INT AUTO_INCREMENT PRIMARY KEY, client_id INT, panier_id INT, prix_total INT, FOREIGN KEY (client_id) REFERENCES Clients(id), FOREIGN KEY (panier_id) REFERENCES Panier(id))')

    def donnees(self):
        # Se connecter à la base de données
        mysdb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="mydatabase"
        )
        mycursor = mysdb.cursor()


        

        # Insérer des données dans la table "Panier"
        mycursor.execute("INSERT INTO Panier (produit_id, client_id, Qts) VALUES (%s, %s, %s)", (1, 1, 3))
        mysdb.commit()

        # Insérer des données dans la table "Facture"
        mycursor.execute("INSERT INTO Facture (client_id, panier_id, prix_total) VALUES (%s, %s, %s)", (1, 1, 60))
        mysdb.commit()

        # Fermer la connexion à la base de données
        mysdb.close()


mydb = BaseDeDonnees("","","","")
# mydb.connection()
mydb.donnees()