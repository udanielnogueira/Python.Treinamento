'''
Faça um programa
que leia a largura e a
altura de uma parede
em metros, calcule a
sua área e a
quantidada de tinta
necessária para
pintá-la. Sabendo que
cada litro de tinta,
pinta uma área de 2m
quadrados.
'''

l = float(input('Digite o valor da largura: '))
h = float(input('Digite o valor da altura: '))

a = l * h

t = a / 2

print(f'Área da parede: {a}')
print(f'Litro(s) de tinta necessário(s): {t:.2f}')
