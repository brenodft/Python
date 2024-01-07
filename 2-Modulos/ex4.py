import random
intgroup = [1,2,3,4,5,6,7,8,9,10]
randint = random.choice(intgroup)
number = 0

while(number != randint):
    number = int(input("Tente adivinhar o numero escrito de 1 a 10 \n"))
    if number != randint:
        print("Errou!")
    else:
        print("Boa!")
    