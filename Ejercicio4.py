def vocal(caracter):
    vocales = "aeiou"

    if caracter in vocales:
        print(f'el caracter {caracter} es vocal')
    else:
        print(f'el caracter {caracter}, no es vocal')

def main():
    try:
        caracter = str(input("Introduzca un caracter: "))
        vocal(caracter)
    except Exception as e:
        print("Introduce un caracter no cualquier otra cosa")

if __name__ == "__main__":
    main()