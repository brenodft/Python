import hashlib

#1 - Verificar os algoritmos disponiveis
print(hashlib.algorithms_available)

#2- Algoritmos disponiveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

#3 - Utilizando o sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "Matheus Banana".encode()
algorithm.update(message)
print(algorithm.hexdigest())

#4 - utilizando o md5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())