def voyelles_du_mot(mot):
    voyelles = "aeiouAEIOU"
    voyelles_du_mot = [lettre for lettre in mot if lettre in voyelles]
    # print(f'Les voyelles sont au nombre de {len(voyelles_du_mot)} dans le mot {mot} sont: {voyelles_du_mot} ')


# voyelles_du_mot('Sahid')

def dont_give_me_five(start, end):
    # Use list comprehension to generate a list of numbers without 5
    result = [num for num in range(start, end + 1) if '5' not in str(num)]
    
    # Return the count of the resulting list
    return len(result)

# Examples
# print(dont_give_me_five(1, 9))  # Output: 8
# print(dont_give_me_five(4, 17))  # Output: 12

def find_deleted_number(arr, mixed_arr):
    # Calculate the sum of the original sequence
    original_sum = sum(arr)
    
    # Calculate the sum of the mixed array
    mixed_sum = sum(mixed_arr)
    
    # The difference between the sums is the deleted number
    return original_sum - mixed_sum

# Example
original_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_sequence = [3, 2, 4, 6, 7, 8, 1, 9]

result = find_deleted_number(original_sequence, mixed_sequence)
# print(result)  # Output: 5

def find_ages(sum_val, difference):
    # Check for invalid input conditions
    if sum_val < 0 or difference < 0 or (sum_val - difference) % 2 != 0:
        return None  # Return None for invalid input

    # Calculate individual ages
    age1 = (sum_val + difference) // 2
    age2 = (sum_val - difference) // 2

    # Check for negative ages
    if age1 < 0 or age2 < 0:
        return None  # Return None if any age is negative

    # Return a tuple with the oldest age first
    return (max(age1, age2), min(age1, age2))

# Examples
# result1 = find_ages(8, 4)
# print(result1)  # Output: (6, 2)

# result2 = find_ages(8, 5)
# print(result2)  # Output: None (negative age)

# result3 = find_ages(10, 2)
# print(result3)  # Output: (6, 4)

# from math import sin
# # print(pi)
# resultat = sin(25)
# print(resultat)


# import math

# print(dir(math))


def moyenne(param):
    somme = 0
    result = 0
    for el in param :
        somme += el 
    result = somme / len(param)
    return print(f'la moyenne est de {param} est: { result}')

# moyenne([10,15,14])

# Exercice 
#  si non.

print('Exercice 1')
# 1- Ecrire un programme qui à partir de la saisir d'un rayon et d'une hauteur, calcule le volume d'un cône droit 
import math
def volume():
    rayon = int(input("Entrez le rayon du cône: "))
    hauteur = int(input("Entrez le hauteur du cône: "))
    volume = (( math.pi * rayon ** 2 )/3) * hauteur
    return print(f'le Volume d\'un cône de rayon {rayon} et de hauteur {hauteur} est : {volume}' 
    )

volume()

print('Exercice 2')
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

print('Exercice 3')
# 3- L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est diviisible par 2 , IMPAIR
def impair_pair():
    param = int(input('Entré un nombre , je vous dis s\'il est pair ou pas '))
    if param % 2 == 0 :
        return print('Ce nombre est PAIR')
    else:
        return print(' Ce nombre est IMPAIR')

impair_pair()

print('Exercice 4')
#  4- Afficher un nombre aléatoire en 5 et 13
def rang():
    for nbr in range(5, 14):
        return print(f'Un nombre aléatoire entre 5 et 13 est donne: {nbr}')

rang()    
