import csv

import contact
# import main

class ContactManager(contact.Contact):
    def __init__(self, nom, prenom, numero_de_telephone, adresse, e_mail):
        super().__init__(nom, prenom, numero_de_telephone, adresse, e_mail)

    def create_contact(self):
        self.nom = input('Entrer votre nom : ')
        self.prenom = input('Entrer votre prénom : ')
        self.numero_de_telephone = input('Entrer votre numéro de téléphone : ')
        self.adresse = input('Entrer votre adresse : ')
        self.e_mail = input('Entrer votre e-mail : ')

        with open('info.csv', 'a', newline='') as fichier:
            writer = csv.writer(fichier)
            writer.writerow([self.nom, self.prenom, self.numero_de_telephone, self.adresse, self.e_mail])
   

    def Read_contact(self):
        with open('info.csv', 'r') as fichier:
            contenu = fichier.read()
            print(contenu)

    def deleted_contact(self):
        with open('info.csv', 'r') as fichier:
            self.contenus = fichier.read()
            self.supprimer = input('Voulez-vous supprimer les informations de qui ?')
            self.donnees = []
            for contenu in self.contenus:
                if self.supprimer != contenu[0]:
                    self.donnees.append(contenu)
        with open('info.csv', 'w', newline='') as nouveau:
            new = csv.writer(nouveau)
            new.writerows(self.supprimer)
        
 
            fichier.write('')

    def update_contact(self):
        with open('info.csv', 'r') as fichier:
            self.contenus = fichier.read()
            self.ancien_nom = input('Voulez-vous modifier les informations de qui ? :')
            for el in self.contenus:
                if el[0] == self.ancien_nom :
                    with open('info.csv', 'a', newline='') as fichier:
                        self.nom = input('Nouveau nom : ')
                        self.prenom = input('Votre nouveau prénom : ')
                        self.numero_de_telephone = input('Votre nouveau numéro de téléphone : ')
                        self.adresse = input('Votre nouveau adresse : ')
                        self.e_mail = input('Votre nouveau e-mail : ')    
                    writer = csv.writer(fichier)
                    writer.writerow([self.nom, self.prenom, self.numero_de_telephone, self.adresse, self.e_mail])               
                else:
                    print('Le nom que vous essayer de modifier n\'existe pas')
                print(self.contenus)
    def demararer(self):
        with open('main.csv', 'r') as menu:
            self.options = menu.read()
            print(self.options)
            option = int(input('Que Voulez vous faire: '))
            if option == 1:
               self.create_contact()
            elif option == 2:
                self.Read_contact()
            elif option == 3:
                self.deleted_contact()
            elif option == 4:
                self.update_contact()
            else:
                exit




           
        



# contact_manager.create_contact()
# contact_manager.Read_contact()
ContactManager('', '', '', '', '').demararer()



