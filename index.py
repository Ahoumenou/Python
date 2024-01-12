print("je suis heureux de commencer python")

# age = 24
# taille = 1.68

# prenom = "Emile Smk"

# mariage = False

# print( 'Je suis ' , prenom, 'j\'ai', age ,'ans', 'et je mesure', taille, 'mètres')

x = True
y = False
print('Et:', y and x)
print('OU:', y or x)
print('OU exclusif:', y ^ x)

c = False
d = True
print('OU exclusif:', y ^ c ^ c)
print('OU exclusif:', x ^ d)

# print(type(x))
temps = "midi"
if temps == 'Jour'  :
  print('je vais au Boulot')
elif temps == 'midi' :
  print('je suis à la pause')
else :
  print(' je suis à la maison')

Fruits = ['Mange', 'Orange', 'Banane']

for el in Fruits:
 print('je suis ', el)

# while Fruits[0] == 'Mange':
#     print('super')


# Lists
# Creation d'une liste
ma_liste = ["Emile", 24, 1.69, True]
print(ma_liste[2])

# apprend() : ajout d'un élement à la fin d'une liste
ma_liste.append('Bonne et Heureuse Année')
ma_liste.append('La santé , Le succès')
print(ma_liste[len(ma_liste)- 2])

# insert() : ajout d'un élement à une position précise dans une liste
ma_liste.insert(2, 'La prospérité')
print(ma_liste)

tabRep = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
# remove(): supprime la valeur spécifiée en paramètre dans une liste
tabRep.remove(4)
print(tabRep)

# pop() : supprime l'element dont l'index est mis en paramètre et le retourne
tabRep.pop(4)
print(tabRep)
tabRep.insert(5, 6)

# Modification d'un élement d'une liste
tabRep[4] = 5
print(tabRep)

# len(): retourne la taille d'une liste
print(len(tabRep))

# Concatenation de 2 ou plusieurs listes 
autre_liste = [10, 11, 12]
liste_concatene = tabRep + autre_liste
print(liste_concatene)

# Les Tuples

# Creation d'un Tuple
mon_tuple = (1, 2, 3, "a", "b")
print(mon_tuple)

# Accès aux élements des Tuples
print(mon_tuple[2])

# Manipulation des Tuples
# Une fois les Tuples crées , ils ne peuvent plus être modifié mais on peut 
# toutefois concatener , dupliquer ....

Tuple_duplique = mon_tuple * 2 
print(Tuple_duplique)

# Introduction aux Sets en Python

# Un ensemble (set) est une collection non ordonné d'élement uniques. Les ensembles sont 
# definis en utilisant des accolades{}

mon_set = {True,1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 'a', 'b', 'c', 'd'}

print(mon_set)
#  Accès aux élements
mon_set.add(True)
print(mon_set)

# Operation sur les ensemble

mon_set2 = {'e', 'f', 'g'}
union = mon_set.union(mon_set2)
print(union)

# Intersection : retourne les élements communs des 2 sets intersectés

intersection = { 6, 7, 8, 9, 'c', 'f', 'e', 'd', 'g'}
Intersection_set = mon_set.intersection(intersection)
print(Intersection_set)

# Exercice pratique
les_cours_disponibles = {
  'html',
  'css',
  'javascript',
  'java',
  'php',
  'python',
  'react',
  'kotlin',
  'go',
  'django',
  'typescript',
  'asp',
  'node.js',
  'git',
  'xml'
}
les_cours_etudiant = (
  'html',
  'css',
  'javascript',
  'java',
  'php',
  'python',
  'kotlin'
)

# Les Operation sur les cours
les_cours_disponibles.remove('django')
les_cours_disponibles.remove('go')
mise_a_jour_des_cours_disponible = les_cours_disponibles.union({'jQuery', 'Bootstrap','Sass', 'Svg', 'Canvas', 'IA'})
print(mise_a_jour_des_cours_disponible)
# les_cours_etudiant.remove('kotlin')
mise_a_jour_des_cours_etudiant = list(les_cours_etudiant)
mise_a_jour_des_cours_etudiant.append('typeScript')
mise_a_jour_des_cours_etudiant.append('node.js')
mise_a_jour_des_cours_etudiant.append('git')
mise_a_jour_des_cours_etudiant.append('IA')

mise_a_jour_des_cours_etudiant = tuple(mise_a_jour_des_cours_etudiant)
print(mise_a_jour_des_cours_etudiant)

# Les Dictionnnaires

# Creation d'une dictionnaire
mon_dictionnaire = {
  'Nom' : "Ahoumenou",
  'Prenom' : "Emile",
  'taille' : 1.68,
  'Age' : 24,
  'Situation matrimoniale': 'celibataire heureux',
}

# Accès aux élements d'une dictionnaire

print(mon_dictionnaire['Nom'])

mon_dictionnaire['taille'] = 1.69

print(mon_dictionnaire['taille'])

# pop(): suppression d'un element dans une dictionnaire 
mon_dictionnaire.pop('Age')
print(mon_dictionnaire)
# Affichage des clés ou valeurs d'une dictionnaire
key = mon_dictionnaire.keys()
valeurs = mon_dictionnaire.values()
print(key)
print(valeurs)

# Exercice Pratique


liste_dictionnaires = [
{
'titre' : 'Sécrétaire paticulière',
'l\'auteur' : 'Jean Pliya',
'genre' : 'Comédie',
},
{
'titre' : 'Roméo et Juliette',
'l\'auteur' : 'William Shakespeare',
'genre' : 'Tragédie',
},
{
'titre' : 'Love in the Time of Cholera',
'l\'auteur' : 'Gabriel García Márquez',
'genre' : 'Réalisme magique',
},
{
'titre' : '1984',
'l\'auteur' : 'George Orwell',
'genre' : ' Science-fiction / Dystopie',
},
{
'titre' : 'One Hundred Years of Solitude',
'l\'auteur' : 'Gabriel García Márquez',
'genre' : ' Réalisme magique',
},
{
'titre' : 'Orgueil et Préjugés',
'l\'auteur' : 'Jane Austen',
'genre' : 'Roman classique / Romance',
},
{'titre' : 'Wuthering Heights',
'l\'auteur' : 'Emily Brontë',
'genre' : 'Roman gothique',
},
{'titre' : 'Fahrenheit 451',
'l\'auteur' : 'Ray Bradbury',
'genre' : 'Science-fiction',
},
{
'titre' : 'Cent ans de solitude (Cien años de soledad)',
'l\'auteur' : 'Gabriel García Márquez',
'genre' : 'Réalisme magique',
},
{
'titre' : 'Brave New World',
'l\'auteur' : 'Aldous Huxley',
'genre' : 'Science-fiction',
},
{
'titre' : 'Le Seigneur des Anneaux" (The Lord of the Rings)',
'l\'auteur' : 'J.R.R. Tolkien',
'genre' : 'Fantasy',
},
{
'titre' : 'Jane Eyre',
'l\'auteur' : 'Charlotte Brontë',
'genre' : 'Roman gothique',
}
]
# Définition des œuvres avec l'auteur, le titre et le genre
oeuvres = [
    {"auteur": "Charlotte Brontë", "titre": "Jane Eyre", "genre": "Roman gothique"},
    {"auteur": "Emily Brontë", "titre": "Wuthering Heights", "genre": "Roman gothique"},
    {"auteur": "Victor Hugo", "titre": "Les Misérables", "genre": "Roman historique"},
    {"auteur": "Alexandre Dumas", "titre": "Le Comte de Monte-Cristo", "genre": "Roman historique"},
    {"auteur": "Aldous Huxley", "titre": "Brave New World", "genre": "Science-fiction / Dystopie"},
    {"auteur": "Ray Bradbury", "titre": "Fahrenheit 451", "genre": "Science-fiction / Dystopie"},
    {"auteur": "Gabriel García Márquez", "titre": "One Hundred Years of Solitude", "genre": "Réalisme magique"},
    {"auteur": "Gabriel García Márquez", "titre": "Love in the Time of Cholera", "genre": "Réalisme magique / Romance"}
]

# Création d'un dictionnaire pour regrouper les œuvres par genre
groupes_par_genre = {}

# Boucle pour regrouper les œuvres par genre
for oeuvre in oeuvres:
    genre = oeuvre["genre"]
    if genre not in groupes_par_genre:
        groupes_par_genre[genre] = []
    groupes_par_genre[genre].append({"auteur": oeuvre["auteur"], "titre": oeuvre["titre"]})

# Affichage des groupes par genre
for genre, liste_oeuvres in groupes_par_genre.items():
    print(f"Genre : {genre}")
    for oeuvre in liste_oeuvres:
        print(f"  - Auteur : {oeuvre['auteur']}, Titre : {oeuvre['titre']}")
    print()

oeuvres_empruntes = [
  ("One Hundred Years of Solitude", "Emile"),
  ("Le Comte de Monte-Cristo", "Smk"),
  ("Love in the Time of Cholera", "Abk"),
]

# print(oeuvres_empruntes)

verification = {}

for empruntes in oeuvres_empruntes:
  for oeuvre in oeuvres:
    if empruntes[0] == oeuvre['titre']:
      oeuvre['disponible'] = 'Nom'
      # print(empruntes[0])
      print('le livre', oeuvre['titre'] , 'est emprunté')
    elif empruntes[0] != oeuvre['titre']:
      oeuvre['disponible'] = 'Oui'
    #   print('le livre', oeuvre['titre'] , 'est disponible')
print(oeuvres)

def return_oeuvre(param):
  for empruntes in oeuvres_empruntes:
    for oeuvre in oeuvres:
      if empruntes[1] == param :
        # empruntes = list(empruntes)
        # empruntes.remove()
        oeuvre['disponible'] = 'Oui'
        print('le livre',empruntes[0], 'est rendu par', param)
        print(oeuvres)

        print(oeuvres_empruntes)
        # print('le livre', empruntes[0] , 'est emprunté')
      # else:
      #   print('Le livre',empruntes[0], 'n\'est pas emprunté par', param)

return_oeuvre('Emile')