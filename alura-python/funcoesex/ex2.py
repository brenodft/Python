def tabuada(num):
	print(f"Tabuada do {num}\n")
	for i in range(11):
		print(f"{num} x {i} = {num*i}")
	return

num = int(input())
tabuada(num)
