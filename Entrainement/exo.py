# 1- Ecrire un programme qui à partir de la saisir d'un rayon et d'une hauteur, calcule le volume d'un cône droit 
import math
def volume():
    rayon = int(input("Entrez le rayon du cône: "))
    hauteur = int(input("Entrez le hauteur du cône: "))
    volume = (( math.pi * rayon ** 2 )/3) * hauteur
    return print(f'le Volume d\'un cône de rayon {rayon} et de hauteur {hauteur} est : {volume}' 
    )

volume()

# 2- L'utilisateur donne un entier positif et le programme annonce combien de fois de suites cet entier est divisible par 2 
def compter_de_divisions(entier):
    if entier <= 0 or type(entier) != int:
        print("Veuillez entrer un entier positif.")
        return
    compte_divisions = 0
    while entier % 2 == 0:
        entier //= 2  # division entière par 2
        compte_divisions += 1
    print(f"L'entier {entier} est divisible par 2: {compte_divisions} fois.")

def diviseurs(param = 0):
    param = int(input("Entrez un entier positif : "))
    return compter_de_divisions(param)

diviseurs()

# 3- L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est diviisible par 2 , IMPAIR
def impair_pair():
    param = int(input('Entré un nombre , je vous dis s\'il est pair ou pas '))
    if param % 2 == 0 :
        return print('Ce nombre est PAIR')
    else:
        return print(' Ce nombre est IMPAIR')

impair_pair()

#  4- Afficher un nombre aléatoire en 5 et 13
def rang():
    for nbr in range(5, 14):
        return print(f'Un nombre aléatoire entre 5 et 13 est donne: {nbr}')

rang()