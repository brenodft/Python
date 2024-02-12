def calcpercBac(lista):
	percBaclist = [0]
	pos = 1
	while pos<len(lista):
		percBaclist.append(100*(lista[pos] - lista[pos-1])/lista[pos-1])
		pos = pos+1
	
	return percBaclist

listabac = [1.2,2.1,3.3,5.0,7.8,11.3,16.6,25.1,37.8,56.9]
print(calcpercBac(listabac))

