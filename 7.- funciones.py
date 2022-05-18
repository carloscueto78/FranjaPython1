#FUNCIONES
print("bienvenidos a python")
print("Introduccion al python")
print("bienvenidos a python")
print("Introduccion al python")
print("bienvenidos a python")
print("Introduccion al python")




# #PARAMETROS
def saludo(nombre, apellido):
    print("hola " + nombre + " " + apellido)

entrada_texto = input("ingrese su nombre: ")
entrada_apellido = input("ingrese su apellido: ")
saludo(entrada_texto, entrada_apellido)



print("Bienvenidos a la calculadora ")

def suma(numero1, numero2):
    resultado = numero1 + numero2 
    return resultado
def division(numero1, numero2):
    resultado = numero1 / numero2 
    return resultado
def multipliacion(numero1, numero2):
    resultado = numero1 * numero2
    return resultado
def restar(numero1, numero2):
    resultado = numero1 - numero2 
    return resultado 
    
print("""Seleccione la operacion que desea realizar:
1 para divison
2 para suma
3 para multiplicacion
4 para restar """)
opcion = int(input("ingrese la operacion: "))
numero1 = int(input("ingrese  el 1er nº: "))
numero2 = int(input("ingrese el 2do nº: "))

if opcion == 1:
   div = division(numero1, numero2)
   print("la division es: " + str(div))
elif opcion == 2:
    sum = suma(numero1, numero2)
    print("la suma es: " + str(sum))
elif opcion == 3:
    mul = multipliacion(numero1, numero2)
    print("la multiplicacion es: " + str(mul))
elif opcion == 4:
    res = restar(numero1, numero2)
    print("la resta es: " + str(res))
else: 
    print("opcion no valida")
    

    

 




