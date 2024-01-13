import csv

def adicionar_contato(name, phone):
    with open("contacts.csv", "a", encoding = 'utf-8', newline = "\n") as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([name, phone])

def listar_contatos():
    with open("contacts.csv", "r", encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Nome: {row['name']} - Numero: {row['phone']}")

def remover_contato(name):
    contacts = []
    with open("contacts.csv", "r", encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    with open("contacts.csv", "w", encoding = 'utf-8', newline = "\n") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "phone"])
        for contact in contacts:
            if contact["name"] != name:
                writer.writerow([contact["name"], contact["phone"]])