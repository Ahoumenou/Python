# import csv
# # import donnees

# #  Créer un fichier CSV simple et le lire
# donnees = [['Nom', 'Age', 'ville'], ['Alice', '25', 'Paris'], ['Bob', 30, 'Londres']]

# # Ecriture dans un fichier CSV

# with open('donnees.CSV', 'w', newline='') as fichier_csv:
#     write = csv.writer(fichier_csv)
#     write.writerows(donnees)

# # Lecture d'un fichier CSV
# with open('donnees.CSV', 'r') as fichier_csv:
#     lecture =  csv.reader(fichier_csv)
#     for ligne in lecture:
#         print(ligne)

# POO
class Faune:
    def __init__(self, animal, region):
        self.animal = animal
        self.region = region
    def affiche_faune(self):
        print(f"La faune de {self.region} est composée de {self.animal} ")

class Animal:
    def __init__(self, nom, category):
        self.nom = nom
        self.category = category

    def aboyer(self):
        print(f"Ceci est un {self.category}. IL s'appelle {self.nom}")


class Chien(Faune, Animal):
    def __init__(self, animal, region ,nom , category,poids,race):
        super().__init__(nom, category)
        super().__init__(animal, region)
        self.poids = poids
        self.race = race
    def affiche_animal(self):
        super().affiche_faune()
        super().affiche_animal()

chien = Chien('Rex', 'Homnivore','Jpn', 'homnivor',5.0, 'Berger')
print(chien.nom)
print(chien.category)
print(chien.animal)
print(chien.region)
print(chien.poids)
print(chien.race)

