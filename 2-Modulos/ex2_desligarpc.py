import os

def desligarpc1hora():
    print("Daqui a uma hora o seu PC será desligado.")
    return os.system("shutdown -s -t 3600")

def desligarpc30min():
    return os.system("shutdown -s -t 1800")

def cancelardesligar():
    print("Cancelando operacao...")
    return os.system("shutdown -a")