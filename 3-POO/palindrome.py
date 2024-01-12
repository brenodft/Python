def palindrome(string):
    if string == string[::-1]:
        return True
    return False

frase = input("Digite uma frase\n")
if palindrome(frase):
    print("É palindromo.")
else:
    print("Não é palindromo.")