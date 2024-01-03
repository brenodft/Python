texto = input("Digite uma palavra \n")
letra1 = texto[0:1]
texto = texto[1:].replace(texto[0:1],"$")
texto = letra1+texto
print(texto)