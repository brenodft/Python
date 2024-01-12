class Contact:
    def __init__(self,name,phone,mail):
        self.name = name
        self.phone = phone
        self.mail = mail

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def addcontact(self):
        novonome = input("Digite o nome do seu novo contato: ")
        novonum = int(input("Digite o numero do seu novo contato: "))
        novomail = input("Digite o email do seu novo contato: ")
        pessoa = Contact(novonome,novonum,novomail)
        self.contacts[novonome] = pessoa
        print("Contato adicionado com sucesso!")
        return
    
    def listcontacts(self):
        print(f"\n###LISTA DE CONTATOS###\n")
        for i,contato in self.contacts.items():
            print(f"{i} - Nome: {contato.name} Numero: {contato.phone} Email: {contato.mail} \n")

    
    def searchcontacts(self):
        ctt = input("Digite o nome do contato: ")
        contato = self.contacts.get(ctt,None)
        if contato is not None:
            print(f"Nome: {contato.name} Numero: {contato.phone} Email: {contato.mail} \n")
        else:
            print("Contato não encontrado.")

    def removecontacts(self):
        remove = input("Digite o nome do contato a ser removido: ")
        if remove in self.contacts:
            del self.contacts[remove]
            print("Contato removido!")
        else:
            print("Contato não encontrado")

        return
    

