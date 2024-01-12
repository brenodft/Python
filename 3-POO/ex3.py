class Viagem:
    def __init__ (self,nome):
        self.name = nome
        self.destiny = "Nenhum"


    def options(self):
        alt = False
        while (alt != True):
            alt = False
            op = ["Cabo Frio","Rio de Janeiro","Salvador","Porto Seguro","Balneario Camboriu"]
            print(f"\nOpções de viagem: \n{op}\n")
            selecionada = input("Qual será o seu destino?: ")
            for i in op:
                if selecionada == i:
                    self.destiny = selecionada
                    alt = True
            if alt == True:
                print("Cadastro realizado com sucesso! ")
            else:
                print("Destino incorreto, deseja tentar novamente?\n1- Sim  2- Não\n")     
                opt = int(input("Selecione uma opcão: "))
                if opt == 1:
                    alt = False
                else:
                    alt = True
        print("Fim do processo.")   
breno = Viagem("breno")
print(vars(breno))
breno.options()
print(vars(breno))                