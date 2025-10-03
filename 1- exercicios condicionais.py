#####################################
### Exercícios sobre Condicionais
#####################################


'''
Exercício 1: Expressão lógica complexa
Escreva um programa que recebe três números inteiros e retorna True se exatamente dois deles forem positivos e o terceiro for negativo ou zero. Caso contrário, retorna False.
'''

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))

if num1 and num2 > 0 and num3 < 1:
    print(True)
else:
    print(False)

Exercício 2: Condicional encadeada com múltiplas variáveis
Crie um programa que recebe três strings representando cores:
"vermelho", "amarelo" ou "verde". A função deve retornar:
-"Pare" se a primeira for "vermelho",
-"Atenção" se a primeira for "amarelo" e a segunda for "vermelho",
-"Siga" se a primeira for "verde" e nenhuma das outras for "vermelho",
-"Erro" para qualquer outra combinação.

cor1, cor2, cor3 = "", "", ""

if cor1 == "vermelho":
    print('Pare')
elif cor1 == "amarelo" and cor2 == "vermelho":
    print('Atenção')
elif cor1 == "verde" and cor2 and cor3 != "vermelho":
    print('Siga')
else:
    print('Erro')


'''
Exercício 2: Condicional encadeada com múltiplas variáveis
Crie um programa que recebe três strings representando cores:
"vermelho", "amarelo" ou "verde". A função deve retornar:
-"Pare" se a primeira for "vermelho",
-"Atenção" se a primeira for "amarelo" e a segunda for "vermelho",
-"Siga" se a primeira for "verde" e nenhuma das outras for "vermelho",
-"Erro" para qualquer outra combinação.
'''

cor1, cor2, cor3 = "amarelo", "vermelho", "verde"
if cor1 == "vermelho":
    print("Pare")
elif cor1 == "amarelo" and cor2 == "vermelho":
    print("Atenção")
elif cor1 == "verde" and cor2 != "vermelho" and cor3 != "vermelho":
    print("Siga")
else:
    print("Erro")


'''
Exercício 3: Condicional com datas
Escreva um programa que recebe três inteiros representando dia, mês e
ano. A função deve verificar se a data é válida sem usar bibliotecas
externas. Desconsidere anos bissextos.

meses com 31 dias:
1, 3, 5, 7, 8, 10, 12
meses com 30 dias:
4, 6, 9, 11
mes com 28 dias:
2
'''
print('Este programa verifica se a data é válida!')
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if ano > 0 and mes > 0 and dia > 0 and mes < 13 and dia < 32:
    if mes == 2 and dia > 28:
        print('Data inválida')
        print('Fevereiro possui 28 dias.')
    elif mes in (4, 6, 9, 11) and dia > 30:
        print('Data inválida, você digitou 31 dias.')
        print(f'O mês {mes} possui apenas 30 dias.')
    else:
        print('Sucesso!')
        print(f'{dia}/{mes}/{ano} é uma data válida!')
else:
    print('Você digitou uma data inválida')


'''
Exercício 4: Decisão baseada em múltiplas condições
Crie um programa que recebe quatro notas de um aluno (entre 0 e 10).
A função deve retornar:
-"Aprovado" se a média for maior ou igual a 7 e nenhuma nota for menor que 5,
-"Recuperação" se a média estiver entre 5 e 7 ou houver pelo menos
uma nota menor que 5,
-"Reprovado" se a média for menor que 5 e houver mais de uma nota menor que 5.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1+nota2+nota3+nota4)/4
notas_insuficiente = (nota1 < 5) + (nota2 < 5) + (nota3 < 5) + (nota4 < 5)

if media >= 7 and not(notas_insuficiente):
    print('Aprovado!')
elif media >= 5:
    print('Recuperação!')
elif media < 5 and notas_insuficiente > 1:
    print('Reprovado!')
else:
    print('Conselho de classe, consulte a secretaria.')


'''
Exercício 5: Condicional com operações matemáticas
Escreva um programa que recebe dois números reais a e b. A função deve retornar:
-"Raiz real" se a equação do segundo grau ax2 + bx + c = 0 tiver raízes reais,
-"Raiz complexa" se não tiver raízes reais,
-"Equação inválida" se a == 0.
'''
a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))

delta = b**2 - 4 * a * c
if a == 0:
    print('Equação inválida.')
elif delta > 0:
    print('Raíz real.')
else:
    print('Raíz complexa.')