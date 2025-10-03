#####################################
### Questões de Lógica de Programação - Loops
#####################################
'''
1. Escreva um programa que imprima todos os números primos entre 1 e 100 usando loops.
'''
for num in range(2, 101):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)


'''
2. Desenvolva um programa que gere a sequência de Fibonacci até o n-ésimo termo utilizando um loop.

A Sequência de Fibonacci é uma série de números onde cada termo, a partir do terceiro, é a soma dos dois termos anteriores, começando geralmente com 0 e 1 (0, 1, 1, 2, 3, 5, 8...)
'''
n = 10 # n-ésimo termo
i = 0 # indice
a = 0 # primeiro termo
b = 1 # segundo termo

while n > i:
    print(a)
    proximo_termo = a + b
    a = b
    b = proximo_termo
    i += 1


3. Escreva um código que verifique se uma palavra é um palíndromo utilizando loops.
4. Escreva um programa que calcule o fatorial de um número usando um loop.
5. Crie um algoritmo que simule uma calculadora simples com operações básicas em
loop até que o usuário decida sair.
6. Escreva um algoritmo que leia um número inteiro positivo e exiba todos os seus
divisores usando um loop.
7. Desenvolva um algoritmo que leia dois números inteiros e exiba todos os números
entre eles (inclusive) que são múltiplos de 3, usando um loop.