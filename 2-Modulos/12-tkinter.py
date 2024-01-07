import tkinter as tk
from PIL import ImageTk,Image

#1 - Criando a janela

window = tk.Tk()
window.geometry("350x600")
window.title("Surprise")
window.iconbitmap("icon.ico")


#2 - Adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10,pady=10,fill='x',expand=True)


#3- Adicionando o label
label = tk.Label(frame,text = "Press the button to see...")
label.pack(fill='x',expand=True)


#4 - Adicionando o input text
frase_lab = tk.Label(frame,text = "Press...")
frase_lab.pack(fill='x',expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x',expand=True)

img = ImageTk.PhotoImage(Image.open("content.png"))


#5 funcao para alterar o texto do label

def click():
    label.config(text = frase_inp.get())
    label.config(image=img)

#6 - Adicionando botao
button = tk.Button(frame, text = "THE BUTTON!",command=click)
button.pack()

window.mainloop()