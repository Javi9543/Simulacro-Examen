#1. Define a function `max()` that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the `max()` function built in, but writing it yourself is nevertheless a good exercise ).

def maxnum(n1, n2):
    if n1 > n2:
        print(f'{n1}, es mayor que {n2}') 
    elif n2 > n1:
        print(f'{n2} es mayor que {n1}')
    else:
        print("Ninguno de los dos numeros es mayor que el otro")

def main():
    try:
        numero = int(input("Introduzca el primer numero: "))
        numero2 = int(input("Introduzca el segundo numero: "))
        maxnum(numero, numero2)
        
    except ValueError: 
        print("Introduzca SOLO numeros enteros")
    

if __name__ == "__main__":
    main()
else:
    print("El programa ha fallado")