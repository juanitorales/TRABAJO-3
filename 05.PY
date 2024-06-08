#Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
#usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
#de los números ingresados por el usuario deberá ser almacenado en una lista. A
#continuación, realice las siguientes tareas:
#a. Determinar el máximo.
#b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#c. Determinar el mínimo.
#d. Calcular la multiplicación de todos los números de la lista.
#e. Contar los valores pares e impares.
#f. Remover los elementos repetidos.
import os
os.system("cls")

datos = []


print("Ingresa numeros enteros y pone fin cuando termines.")

while True:
    numeros = input("Ingresa un numero entero: ")
    
    if numeros.lower() == 'fin':
        break
    
    datos.append(int(numeros))

print("Los numeros enteros ingresados son:", datos)

datos.sort()

print ("Te ordene los numeros enteros ingresados mira:", datos)
print ("El numero mas grande que ingresate es el:", datos[-1])
print ("El segundo numero mas grande que ingresate es el:", datos[-2])
print ("El numero mas bajo que ingresate es el:", datos[0])

resultado = 1

for num in datos:
    resultado *= num
print("El resultado de tus numeros multiplicados es de:", resultado)

for num in datos:
    if num % 2 ==0:
        print ("Los numeros pares de la lista son:", num)
for num in datos:
    if num % 2 != 0:
        print ("Los numeros impares de la lista son:", num)
        
i = len(datos) - 1
while i >= 0:
    n = datos [i]
    if datos.count(n) >1:
        datos.remove (n)
    i -=1
print ("La lista sin duplicados es:", datos)
        