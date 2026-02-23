#6. Define a function `sum()` and a function `multiply()` that sums and multiplies (respectively) all the numbers in a list of numbers. For example, `sum([1, 2, 3, 4])` should return `10`, and `multiply([1, 2, 3, 4])` should return `24`.

def suma(listasuma):
    s = 0
    for i in listasuma:
        s += i
    return s

def multiply(listamulti):
    mult = 1
    listamulti = [1,2,3,4]
    for i in listamulti:
        mult = mult * i
    return mult

def main():
    numeros = [1,2,3,4]

    total1 = suma(numeros)
    total2 = multiply(numeros)

    print ("suma lista 1: ",total1)
    print("multiplicacion lista 2: ",total2)

if __name__ == "__main__":
    main()