def tempMedia(temperaturas):
	media = sum(temperaturas)/12
	return media

def maiorMedia(temperaturas,media):
	maiorm = {}
	for mes,temp in temperaturas.items():
		if temp > media:
			maiorm[mes] = temp
	return maiorm

temperaturas = {'Janeiro':0,'Fevereiro':0,'Março':0,'Abril':0,'Maio':0,'Junho':0,'Julho':0,'Agosto':0,'Setembro':0,'Outubro':0,'Novembro':0,'Dezembro':0}
for temp in temperaturas:
	temperaturas[temp] = float(input("Digite a temperatura desse mes: "))
media = tempMedia(temperaturas.values())
maiorMedia = maiorMedia(temperaturas,media)
print(f"Media : {media} ") 
print("\nMaior media:", maiorMedia)

