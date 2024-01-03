num = int(input("Informe um numero inteiro\n"))
limit = int (input("Informe um limite\n"))

print("TABUADA\n")
for i in range(limit+1):
    print(f"{i}: {num*i}\n")