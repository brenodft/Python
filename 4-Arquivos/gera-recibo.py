from fpdf import FPDF
from num2words import num2words
from datetime import date

#1 - Variaveis
cliente = input("Informe o nome do cliente: ")
valor = input("Informe o valor do recibo: ")
ref = input("Informe o serviço: ")
vlr_msg = f"{valor} reais"
vlr_extenso = num2words(float(valor),lang = 'pt_BR')
vlr_extenso_msg = f"({vlr_extenso} reais)"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

# 2-  Layout do recio
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=20)
pdf.image("rec.jpg",x=0,y=0)
pdf.text(162,45,vlr_msg)
pdf.text(80,86, cliente)
pdf.text(80,108, vlr_extenso_msg)
pdf.text(80,135,ref)
pdf.set_text_color(255,255,255)
pdf.text(30,194,str(dia))
pdf.text(50,194,str(mes))
pdf.text(70,194,str(ano))
nome_arquivo = f"{cliente.strip()}_{dia}_{mes}_{ano}"
pdf.output(f"{nome_arquivo}.pdf")
print("Recibo gerado com sucesso!")