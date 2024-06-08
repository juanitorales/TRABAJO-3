#6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
#de una lista vacía:
#a. Agregar un elemento al final.
#b. Agregar un elemento al principio.
#c. Quitar un elemento al final.
#d. Quitar un elemento al principio
import os
os.system("cls")

lista = []

elemento_final=input ("Ingresa un numero o palabra, sera almacenado al final de la lista: ")

lista.append(elemento_final)

print (lista)

elemento_principio=input ("Ingresa un numero o palabra, sera almacenado al principio de la lista: ")

lista.insert(0, elemento_principio)

print(lista)

uno = 0
dos = 1

print("Ahora quitaremos un elemento de la lista" )
eliminar= (input("ingrese la palabra uno o dos, segun la posicion en la cual se encuentra el elemento a eliminar:"))

