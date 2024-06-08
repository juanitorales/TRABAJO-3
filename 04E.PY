#e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
#la lista. Quitar el elemento correspondiente de esa posición.

import os
os.system("cls")

paises=["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

numero=int (input("Ingresa un numero del 0 al 4 para quitar un pais:"))

numero>=0 and numero<=4

del paises[numero]

print("El pais fue quitado con exito, la lista queda asi:", paises)