#3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
#frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
#debajo la misma lista pero sólo con las frutas que añadió el usuario.

lista = ["banana", "manzana", "pera"]
print ('Las frutas que estan en la lista son: banana, manzana, pera.')

frutas = input("Ingresa 3 diferentes frutas a las de la lista separadas por comas: ")

lista.append(frutas)
        
print ("La lista completa es: ",lista)
print ("Las frutas agregadas son: ", [frutas])