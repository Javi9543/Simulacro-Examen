#2. Define a function `max_of_three()` that takes three numbers as arguments and returns the largest of them.
def maxv2(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f'{n1}, es mayor que {n2} y {n3}')

    elif n2 > n3 and n2 > n1:
        print(f'{n2} es mayoe que {n1} y {n3}')

    elif n3 > n2 and n3 > n1:
        print(f'{n3} es mayor que {n2} y {n1}')

def main():
    num1 = int(input("Introduzca el primer numero: "))
    num2 = int(input("Introduzca el segundo numero: "))
    num3 = int(input("Introduzca el tercer numero: "))

    maxv2(num1, num2, num3)

if __name__ == "__main__":
    main()
    print("Hubo un error en el programa o no se ejecutó correctamente")