##5. Write a function `translate()` that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, `translate("this is fun")` should return the string `"tothohisos isos fofunon".`
def traductor(texto):
    lista_vocal = "aeiou"
    total = ""

    for i in texto:
        vocales = False
        for j in lista_vocal:
            if i == j:
                vocales = True
                break
        
        if vocales or i == " ":
            total += i
        else:
            total = i + "o" + i
    
    print (total)

def main():
    cadena = input("Introduce un texto para pasarlo a idioma ladron: ")
    traductor(cadena)


if __name__ == "__main__":
    main()
