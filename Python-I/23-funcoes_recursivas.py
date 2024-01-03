def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

def somaTotal(num):
    if num == 1:
        return 1
    else:
        return num + somaTotal(num-1)
    
arg = int(input("Digite um numero\n"))
print(factorial(arg))
print(somaTotal(arg))
