#Faça um programa que leia 5 números e informe o maior número.

lista_num = []
contador = 0


while contador <5:
    numero = int(input("Digite um numero:\n"))
    lista_num.append(numero)
    contador+=1

print ("O maior valor é", max(lista_num))

#valor_inicial = None

#for i in lista_num:
#    if valor_inicial is None:
#        valor_inicial = i
#    else:
#        if valor_inicial < i:
#            valor_inicial = i
#        elif valor_inicial>i:
#            valor_inicial = valor_inicial
#
#print(f'O maior numero é {valor_inicial}')
