
# Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
# 1a string: CTA
# 2a string: ABC
# 3a string: BT
# A ordem dos caracteres da terceira string não é importante.

a = input("Informe uma string de tamanho qualquer: ")
b = input("Informe outra string de tamanho qualquer: ")
c = ""

for i in a:
    if i not in b:
        c += i

for i in b:
    if i not in a:
        c += i

print(c)