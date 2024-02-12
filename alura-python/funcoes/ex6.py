from random import randrange
def sorteio(num): 
	sorteado = randrange(num)
	print(f"O usuario sorteado foi o usuario {sorteado}")
	return sorteado
inform = int(input("Informe o numero de usuarios para serem sorteados: "))
sorteio(inform) 
