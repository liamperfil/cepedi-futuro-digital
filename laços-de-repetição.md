# Laços de repetição

## sintaxe for (para)
```py
for item in sequencia:
  print(x)
```
Onde:
- for: A palavra-chave que inicia o laço.
- item: Uma variável temporária que recebe, a cada repetição do laço, um dos elementos da sequencia. O nome dessa variável pode ser qualquer um que você queira (por exemplo, letra, numero, elemento, etc.).
- in: A palavra-chave que indica que a iteração ocorrerá dentro da sequencia.
- sequencia: A coleção de itens sobre a qual você quer iterar. Pode ser uma lista, uma string, uma tupla, etc.

> O laço continua executando o bloco de código indentado para cada item na sequencia até que todos os itens tenham sido processados.

## Exemplos Práticos

1. Iterando sobre uma lista de números
```py
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
  print(numero)
```

2. Iterando sobre uma string
```py
palavra = "Python"

for letra in palavra:
  print(letra)
```

3. Usando range() para gerar sequências de números
```py
for i in range(5):
  print(i)
```

4. Usando enumerate, cria pares indice-valor
```py
yourlist = ['joao', 'maria', 'jose']
for i, x in enumerate(yourlist):
  if x == 'jose':
    print(f'jose é o numero {i} da lista')
```

```py
for i, x in enumerate("jean lima"):
  print(f'i = {i}, x = {x}')
```

```py
def primo(num):
  divisores = []
  for x in range(1, num+1):
    if num % x == 0:
      divisores.append(x)
  print(f'Os divisores de {num}, são: {divisores}')
primo(10)
```