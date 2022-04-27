# Ejercicio 1
# Escribir un programa que pregunte el nombre por consola
# y un numero entero e imprimir por pantalla el nombre
# tantas veces el numero que introdujo

#Ejercicio 1
numero1 = int(input("Ingrese su numero:"))
print(numero1)
nombre1 = input("Ingrese su nombre:")
print(numero1 * nombre1)

#Ejercicio 2
#Escribir un programa que muestre por pantalla el resultado
#de la siguiente opracion matematica

resultado = ((3 + 2)/(2 * 5))**2
print(resultado)


#ejercicio 3
# Escribir un programa que lea un entero positivo n
#introduccido por el usuario y despues muestre por pantalla
#la suma de todos los enteros desde 1 hasta n
#la suma de los n primeros positivos puede ser calculado
#de la siguiente forma

n = int(input("ingrese su numero entero positivo n: "))
if n > 0:
    valor=str(((n * (n + 1)) / 2))
    print("el valor de 1 hasta n es:" + valor)
else:
    print("no se puede calcular")







