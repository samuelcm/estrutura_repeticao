#Faça um programa que leia 5 números e informe o maior número.
lista_num = []
contador = 0


while contador <5:
    numero = int(input("Digite um numero:\n"))
    lista_num.append(numero)
    contador+=1


valor_inicial = lista_num[0]

for i in lista_num:
    if valor_inicial < i:
        valor_inicial = i


print(f'O maior numero é {valor_inicial}')
