def analisarData(data):
	meses = [31,28,31,30,31,30,31,31,30,31,30,31]
	if data['dia'] > meses[data['mes']]:
		print("Invalida!")
		return False
	else:
		print("Valida!")
		return True
data = {'dia': 0, 'mes': 0, 'ano': 0}
data['dia'] = int(input("Informe o dia: "))
data['mes'] = int(input("Informe o mes: "))
data['ano'] = int(input("Informe o ano: "))
analisarData(data)
