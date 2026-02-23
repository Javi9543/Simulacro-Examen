#3. Define a function that computes the length of a given list or string. ( It is true that Python has the `len()` function built in, but writing it yourself is nevertheless a good exercise ).

def contadorCadena(cad):
    cont = 0

    for i in cad:
        cont += 1
    
    print (f"La longitud de {cad} es {cont}")

def main():

    cadena = input("Introduzca una cadena para saber su longitud: ")

    contadorCadena(cadena)


if __name__ == "__main__":
    main()
else:
    print("No se pudo ejecutar el programa correctamente")