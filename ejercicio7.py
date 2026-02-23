#7. Define a function `reverse()` that computes the reversal of a string. For example, `reverse( "I am testing" )` should return the string `"gnitset ma I"`.

def invertido(cadena):

    resultdo = " "

    for i in cadena:
        resultdo = i + resultdo

    print(resultdo)

def main():
    cadena = input("Escribe algo: ")
    invertido(cadena)  

if __name__ == "__main__":
    main()