
# Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira.
# 1a string: AATTCGAA
# 2a string: TG
# 3a string: AC
# Resultado: AAAACCAA

a = input("Informe a primeira string de tamanho qualquer: ")
b = input("Informe a segunda string de tamanho qualquer: ")
c = input("Informe a terceira string de tamanho qualquer: ")
d = ""

for i in a:    
    posicao = b.find(i)
    if posicao != -1:
        d += c[posicao]
    else:
        d += i

print(d)