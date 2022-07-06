
# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
# 1a string: AAACTBF
# 2a string: CBT
# Resultado: CBT
# A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.

a = input("Informe uma string de tamanho qualquer: ")
b = input("Informe outra string de tamanho qualquer: ")
c = ""

for i in a:
    if i in b:
        c += i

print(c)