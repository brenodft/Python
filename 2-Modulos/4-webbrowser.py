import webbrowser

feito = False

while not feito:
    print("O que voce deseja fazer?")
    print("1. Aprender Python")
    print("2. Aprender sobre modulos")
    print("3. Aprender Python, Javascript,Ingles e No-code")

    choice = input(">")
    if choice == "1":
        webbrowser.open("http://www.python.org")
    elif choice == "2":
        webbrowser.open("https://docs.python.org/3/py-modindex.html")
    elif choice == "3":
        webbrowser.open("https://pages.onebitcode.com/")
    elif choice == "4":
        feito = True