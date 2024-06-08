#Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
#Imprimir por pantalla el resultado

numeros = []

for i in range(5):
    numero = float(input("Ingresa un numero: "))
    numeros.append(numero)

numeros.sort()

print("Los numeros en orden son:", numeros)

