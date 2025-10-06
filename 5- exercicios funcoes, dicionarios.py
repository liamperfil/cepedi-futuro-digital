'''
1. Crie uma função chamada 'contar_chaves' que receba um
dicionário como parâmetro e retorne o número de chaves que
ele possui.
Exemplo:
contar_chaves({'a': 1, 'b': 2})
deve retornar 2.
'''

def contar_chaves(dicionario):
    print(len(dicionario.keys()))
    return len(dicionario.keys())
contar_chaves({'a': 1, 'b': 2})


'''
2. Crie uma função chamada 'valor_maximo' que receba um
dicionário com valores numéricos e retorne o maior valor.
Exemplo:
valor_maximo({'a': 10, 'b': 25, 'c': 7})
deve retornar 25.
'''
def valor_maximo(dicionario):
    print(max(dicionario.values()))
    return max(dicionario.values())
valor_maximo({'a': 10, 'b': 25, 'c': 7})


'''
3. Crie uma função chamada 'inverter_dicionario' que receba
um dicionário e retorne um novo dicionário com as chaves e
valores invertidos.
Exemplo:
inverter_dicionario({'a': 1, 'b': 2})
deve retornar {1: 'a', 2: 'b'}.
'''
def inverter_dicionario(dicionario):
    invertido = {valor: chave for chave, valor in dicionario.items()}
    print(invertido)
inverter_dicionario({'a': 1, 'b': 2})


'''
4. Crie uma função chamada 'agrupar_por_valor' que receba
uma lista de dicionários e agrupe os dicionários por valor de
uma chave comum.
Exemplo:
agrupar_por_valor([{'nome': 'Ana', 'grupo': 'A'}, {'nome':
'João', 'grupo': 'B'}, {'nome': 'Maria', 'grupo': 'A'}])

Deve retornar {'A': ['Ana', 'Maria'], 'B': ['João']}
'''
def agrupar_por_valor(lista):
    agrupado = {}
    for item in lista:
        valor_chave = item.get("grupo")
        
        valor_a_agrupar = item.get('nome')
    
        if valor_chave in agrupado:
            agrupado[valor_chave].append(valor_a_agrupar)
        else:
            agrupado[valor_chave] = [valor_a_agrupar]
    print(agrupado)

dados = [
    {'nome': 'Ana', 'grupo': 'A'}, 
    {'nome': 'João', 'grupo': 'B'}, 
    {'nome': 'Maria', 'grupo': 'A'}
]
agrupar_por_valor(dados)