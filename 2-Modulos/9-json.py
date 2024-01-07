import json

#1 - Strings para Dicionarios
person = '{"name": "Breno", "languages": ["C","Python"]}'
person_dict = json.loads(person)
print(person_dict)

#2 - Convertendo para JSON
person_json = json.dumps(person_dict)
print(person_json)

#3 - Formatando JSON
print(json.dumps(person_dict, indent = 4, sort_keys = True))

#4 - Salvando JSON em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict,json_file)

#5 - Lendo JSON externo
with open("iris.json", "r") as f:
    data = json.load(f)
    print(data)