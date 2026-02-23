#8. Define a function `is_palindrome()` that recognizes palindromes (i.e. words that look the same written backwards). For example, `is_palindrome( "radar" )` should return `True`.

def palindromo(cadena):
    total = ""
    for i in cadena:
        total = i + total
    
    if cadena == total:
        print(f'la cadena {cadena} es palíndroma')
    else: 
        print(f'la cadena {cadena}, no es palindroma')

def main():
    cad = input("Introduzca una cadena para saber si es palindroma o no palindroma: ")
    palindromo(cad)

if __name__ == "__main__":
    main()
