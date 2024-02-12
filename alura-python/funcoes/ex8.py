from random import choice
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
saladasurpresa = []
for i in range(3):
	saladasurpresa.append(choice(frutas))

print(saladasurpresa)
