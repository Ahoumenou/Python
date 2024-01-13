#  Changé le contenu d'un fichier 
with open('exemple.txt', 'w') as fichier:
    fichier.write('Ceci est une ligne écrite dans le fichier \n Je suis trop bon .')

with open('exemple.txt', 'a') as fichier:
    fichier.write('Ceci est une ligne écrite dans le fichier \n Je suis trop bon .\n Aujourd\'hui c\'est un Samedi .')

# Lecture du fichier
with open('exemple.txt','r') as fichier:
    contenu = fichier.read()
    print(contenu)

try:
    # Code susceptible de générer une exception
    
except ExceptionType as e:
    # Code à exécuter si une exception de type ExceptionType est levée
    # e est une variable qui contient l'instance de l'exception
    
else:
    # Code à exécuter si aucune exception n'est levée dans le bloc try
    
finally:
    # Code à exécuter quelle que soit la situation (exception levée ou non)
    


