
# Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
# 1a string: AATTGGAA
# 2a string: TG
# 3a string: AAAA

a = input("Informe uma string de tamanho qualquer: ")
b = input("Informe outra string de tamanho qualquer: ")
c = ""

for i in a:
    if i not in b:        
        c += i

print(c)