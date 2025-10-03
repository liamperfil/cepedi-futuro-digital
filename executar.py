'''
A Sequência de Fibonacci é uma série de números onde cada 
termo, a partir do terceiro, é a soma dos dois termos anteriores, começando geralmente com 0 e 1 (0, 1, 1, 2, 3, 5, 8...)

0, 1, 

1. Escreva um programa que imprima todos os números primos entre 1 e 100 usando loops.
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