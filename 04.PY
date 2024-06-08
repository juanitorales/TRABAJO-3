#4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
#realizar lo siguiente:
#a. Imprimir la cantidad de elementos que tiene la lista. echo
#b. Imprimir el primer y último elemento. echo
#c. Imprimir el resto. echo
#d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
#la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.

import os
os.system("cls")

paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

print ("La cantidad de elementos en la lista es un total de:",len(paises))

print (paises [0]), print (paises [-1])

print (paises [1:4])

pais = input  ("Ingrese un pais: ")
pais = pais.capitalize()

if pais in paises:
    print ("Se encuentra en la lista!")
else:
    print ("No se encuentra en la lista!")
    