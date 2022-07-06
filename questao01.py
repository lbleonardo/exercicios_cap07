
# Questão 01

#Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
# 1a string: AABBEFAATT
# 2a string: BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT

a = input("Informe uma string de tamanho qualquer: ")
b = input("Informe outra string de tamanho qualquer: ")

if a.find(b) != -1:
    print(b, "Encontrado na posição", a.find(b), "de", a)
else:
    print("A String", b, "não está contida em", a, "ou as strings são diferentes entre minúsculas e maiúsculas.")



