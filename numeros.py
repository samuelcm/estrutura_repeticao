#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

numero = 0

#while numero <= 19:
#    numero += 1
#    print(numero)

lista_num = []
while numero <= 19:
    numero += 1
    lista_num.append(numero)
print(lista_num)
