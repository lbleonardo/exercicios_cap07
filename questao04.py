
# Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
# String: TTAAC
# Resultado:
# T: 2x
# A: 2x
# C: 1x

a = input("Informe uma string de tamanho qualquer: ")
b = ""

for i in a:
    if i not in b:
        b += i        
        print(i, "-", a.count(i),"x")



