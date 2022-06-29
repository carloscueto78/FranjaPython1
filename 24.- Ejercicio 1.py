#Ejercicio 1
#Escriba una funcion que aleatoriamente escoja un numero entreo entre
#1 y 10 y lo guarde en un fichero de nombre tabla-n.txt donde n es el
# numero que salio. Escribir en el archivo la tabla del numero .


import random

def main():
    numero_aleatorio = random.randint(1, 10)
    nombre_fichero = "tabla-" + str(numero_aleatorio) + ".txt"
    with open(nombre_fichero, "w", encoding="utf-8") as file:
        for i in range(1, 13):
            linea = str(i) + "X" + str(numero_aleatorio) + " = " + str(numero_aleatorio * i)

            file.write(linea)
            file.write("\n")

if __name__ == '__main__':
    main()
