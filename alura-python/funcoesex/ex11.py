def maisde5 (palavra):
	return len(palavra)>5

frase = "Aprender Python aqui na Alura é muito bom"
palavras = list(filter(maisde5,frase.split())
print(palavras)
