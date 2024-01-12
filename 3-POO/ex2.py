class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f"Nome do produto: {self.nome}\nPreço do produto: R${self.preco}"
    def discount(self):
        porcent = float(input("Quantos % você quer dar de desconto? "))
        print(f"O valor do produto com o desconto aplicado é {self.preco - (self.preco*(porcent/100))}")


banana = Product("banana",3.0)
print(banana)
banana.discount()