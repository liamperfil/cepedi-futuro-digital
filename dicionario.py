meu_dicionario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

meu_dicionario = dict(nome="Paulo", idade=25, cidade="Rio de Janeiro")  # Outra forma de criar um dicionário

meu_dicionario["profissão"] = "Engenheiro"  # Adicionando um novo par chave-valor

# Imprimindo chaves e valores do dicionário
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

print(list(meu_dicionario.keys()[0])) # Imprime a primeira chave
print(list(meu_dicionario.values()[0])) # Imprime o primeiro valor

if "idade" in meu_dicionario:
    print("A chave 'idade' existe no dicionário.")

if "Paulo" in meu_dicionario.values():
    print("O valor 'Paulo' existe no dicionário.")

meu_dicionario.pop("cidade") # Removendo um par chave-valor

meu_dicionario.clear() # Limpando o dicionário

#################################################################
# Métodos e funções úteis para dicionários
#################################################################
'''
list()
dict()
set()
tuple()
pop()
popitem()
clear()
items()
keys()
values()
copy()
del
'''

#################################################################
# Dicionários aninhados
#################################################################
pessoas = {
"joao": {
"sobrenome": "lima",
"cidade": "salvador",
"nascimento": 1992
},
"maria": {
"sobrenome": "maciel",
"cidade": "lauro de freitas",
"nascimento": 2000
}
}

for x, obj in pessoas.items():
    print(x)
    for chave, valor in obj.items():
        print(f"  {chave}: {valor}")