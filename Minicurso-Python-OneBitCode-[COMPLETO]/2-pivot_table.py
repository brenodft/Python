import pandas as pd

# 1- Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")


#2- Selecionando colunas específicas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

#- Criando tabela pivô
pivot_table = df.pivot_table(
    index = "Ano",
    columns = "Fabricante",
    values = "ValorVenda",
    aggfunc = "sum"
)

print(pivot_table)

#4- Exportando tabela pivo em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")