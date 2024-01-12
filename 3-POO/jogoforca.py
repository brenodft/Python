import random
import requests

def iniciajogo():
    palavras = requests.get("https://raw.githubusercontent.com/fserb/pt-br/master/palavras", timeout = 10)

    listapalavras = palavras.content.decode('utf-8').splitlines()

    error = 0
    palavra = random.choice(listapalavras)
    lacuna = ["_" for i in range(len(palavra))]
    while "_" in lacuna and error<4:
        print(lacuna)
        print(f"Erros: {error}")
        achou = False
        letra = input("Digite uma letra: ")
        print(lacuna)
        for i in range(len(palavra)):
            if letra == palavra[i]:
                lacuna[i] = letra
                achou = True
        if not achou:
            error = error+1
            
    if error == 4:
        print("Infelizmente você perdeu...")
        print(f"A palavra era: {palavra}")
    else:
        print("Parabéns! Você acertou a palavra!")
        print(f"A palavra era: {palavra}")

