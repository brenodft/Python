str1 = input("Digite uma frase\n")
str2 = input("Digite outra frase\n")
novafrase = str1.replace(str1[:2],str2[:2]) + " " + str2.replace(str2[:2],str1[:2])
print(novafrase)