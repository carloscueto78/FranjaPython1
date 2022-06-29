# Numpy

#¿Que es Numpy?
# Libreria para el calculo numerico y manejo de arreglos(array)
#(listas organizadas de numeros)
# mas veloz y eficiente para manejar listas/arreglos en python 
# Agrega soporte para grandes arreglos, multidimensionales y matrices
# utilizada en el mundo de la inteligencia artificial y la ciencia de datos

#Como se instala:
# en la consola activar ambiente virtual de miniconda
# pip install numpy

#como importar numpy en el codigo
#Import numpy as np

import numpy as np

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista)

    # Crear un arreglo
    arreglo = np.array(lista)
    print(arreglo)
    print(type(arreglo))

    #Crear arreglo de 2 dimensiones
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matriz)

    # Indexacion de arreglos
    print( arreglo[0])
    print( arreglo[0] + arreglo[1] )

    # Indexacion de matrices
    print( matriz[0] )
    print( matriz[0,0] )
    print( matriz[0,1] + matriz[0,0] )

    print( arreglo[0:3] )
    



if __name__ == '__main__':
    main()
