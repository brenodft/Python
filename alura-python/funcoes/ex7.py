from random import randrange
def gerartoken():
	return randrange(1000,9998)
token = gerartoken()
nome = input()
print(f"Ola {nome}, seu token de acesso é {token}! Seja bem vindo(a)")
	

