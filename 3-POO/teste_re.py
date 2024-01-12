import re

def from_text(string):
    item = re.findall("é \w ",string)
    return item

from_text("Meu videogame é WiiU e o preço é 1000 reais")