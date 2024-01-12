print('**************Exercice 1************')   
compter = 0

while compter < 21 :
    compter += 1
    # compter *= 7
    x = compter * 7
    print(x)
    if x % 3 == 0 :
        print( 'le nombre', x , 'est un', 'multiple de 7 diviisible par 3')

print('**************Exercice 2************')   
mult = 3
while mult <= 3 ** 12:
 mult *= 3 
 print(mult)  


print('**************Exercice 3************')    
n = 0
i = 0
u = 0
w = 0
nombre = int(input('Entré un nombre: '))
while nombre > 0:
    i += 1 
    n += nombre

    print(n)
    nombre = int(input('entré un nombre: ') )

    if nombre <= 0 :
        print('total = ', n)
        print('nombre total de données: ',i)
        if nombre > 100 :
            u += 1
            print('nombre total de données superieurs à 100: ', u)
        else:
            w += 1 
            print('nombre total de données inferieurs à 100 ', w)

print('**************Exercice 4************')    
for el in range(1, 64):
    print('Case ', el, ':' , el * 2 , 'grains')

print('**************Exercice 5************')    

for element in range(2, 10000):
     nbrs = 0
     nbr = input('Entré un nombre: ')
     if int(nbr) % element == 0 :
        nbrs += 1
        print(element ,'soit',nbrs, 'diviseurs propres')
  
