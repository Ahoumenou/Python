# class Pere:
#     def methode_parente1(self,nom_pere,prenom_pere):
#         print(f"le nom du Père: {nom_pere} et son prenom est {prenom_pere} ")

# class Mere:
#     def methode_parente2(self,nom_mere,prenom_mere):
#         print(f"le nom du Père: {nom_mere} et son prenom est {prenom_mere} ")

# class Enfant(Pere, Mere):
#     def __init__(self, nom_pere, prenom_pere, nom_mere, prenom_mere, nom_enfant, prenom_enfant):
#         super.__init__(self,nom_pere, prenom_pere,nom_mere, prenom_mere)
#         # super.__init__(self,nom_mere, prenom_mere)
#         self.nom_enfant = nom_enfant
#         self.prenom_enfant = prenom_enfant
#     def methode_enfant(self):
#         print("Méthode de la classe enfant")

# # Créer une instance de la classe enfant
# objet_enfant = Enfant("Edouard", "Ahn", "Avocetion", "Mahussi", 'Eml', 'Ahn')

# # Appeler des méthodes de différentes classes
# objet_enfant.Pere()
# objet_enfant.Mere()


class ClasseParente1:
    def __init__(self, parametre1):
        self.parametre1 = parametre1

    def methode_parente1(self):
        print("Méthode de la classe parente 1")

class ClasseParente2:
    def __init__(self, parametre2):
        self.parametre2 = parametre2

    def methode_parente2(self):
        print("Méthode de la classe parente 2")

class ClasseEnfant(ClasseParente1, ClasseParente2):
    def __init__(self, parametre1, parametre2, parametre_enfant):
        super().__init__(parametre1)  # Appeler le constructeur de ClasseParente1
        ClasseParente2.__init__(self, parametre2)  # Appeler le constructeur de ClasseParente2
        self.parametre_enfant = parametre_enfant

    def methode_enfant(self):
        print("Méthode de la classe enfant")

# Créer une instance de la classe enfant en passant les paramètres nécessaires
objet_enfant = ClasseEnfant("valeur1", "valeur2", "valeur_enfant")

# Accéder aux attributs de toutes les classes (parentes et enfant)
print(objet_enfant.parametre1)
print(objet_enfant.parametre2)
print(objet_enfant.parametre_enfant)

# Appeler des méthodes de différentes classes
objet_enfant.methode_parente1()
objet_enfant.methode_parente2()
objet_enfant.methode_enfant()
