#Palindromo

#Escribir un programa que indentifique
#si una palabra es palindromo o no
# Luz azul
# Ana
# Anita lava la tina
# yo hago yoga hoy


def palindromo(palabra):
    palabra = palabra.replace(' ' , '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

# Funcion principal main/run
def main(): 
    palabra = input("ingrese una frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("es palindromo")
    else:
        print("no es palindromo")

# Punto de entrada
# Buena practica
if __name__ == "__main__":
    main()

