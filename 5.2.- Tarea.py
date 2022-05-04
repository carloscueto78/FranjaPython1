#Tarea 1 
#una jugeteria tiene mucho exito en dos de sus productos: payasos y muñecas
#suele hacer ventas por correo y la empresa de logistica les cobra por peso de cada paquete
#asi que deben calcular el peso de los payasos y muñecas que saldran en cada paquete

payasos = int(input("Ingresar la cantidad de payasos: "))
munecas = int(input("Ingresar la cantidad de muñecas: "))
vendidos = (payasos + munecas)
resultado = ((payasos * 112)+(munecas * 75))
print("Peso del paquete entre payasos y munecas"); print(resultado)
print("Cantidad de payasos y munecas vendidos"); print(vendidos)



#tarea 2
# escribir un programa que pida al usuario su peso (en kg) y estatura ( en metros)
#calcule el indice de masa corporal y lo almacene en un variable
# #Calculadora IMC 

kg = float(input("Ingrese su peso en Kilogramos: "))     
metros = float(input("Ingrese su estatura en metros: "))

imc = ((kg)/((metros)**2))

print("Su Índice de Masa Corporal es: ")
print(round(imc,2))