# texto = input("Digite um texto \n")
def contarmaiuscula(texto):
    countmaiuscula = 0
    countminuscula = 0
    for i in range(len(texto)):
        if texto[i] == texto[i].upper():
            countmaiuscula += 1
        else:
            countminuscula += 1

    print(f"Maiusculas = {countmaiuscula} \nMinusculas = {countminuscula}")

# contarmaiuscula(texto)
    

def parimpar():
    listapar = []
    listaimpar = []
    num = 0

    while(num != -1):
        num = int(input("Digite um numero \n"))
        if num != -1:
            if num%2 == 0:
                listapar.append(num)
            else:
                listaimpar.append(num)

    print(f"Numeros pares: {listapar}\nNumeros impares: {listaimpar}")


# parimpar()
