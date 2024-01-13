import csv

name = input("Informe o nome da linguagem que deseja aprender: ")
category = input("Qual categoria?: ")
with open("courses.csv","a", encoding= 'utf=8', newline = "\n") as file:
    writer = csv.writer(file)
    writer.writerow([name, category])