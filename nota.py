#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
#valor seja inválido e continue pedindo até que o usuário informe um valor válido.

notas = [0,1,2,3,4,5,6,7,8,9,10]
nota= None

while nota not in notas:
    nota = int(input("Digite uma nota entre zero e dez:\n"))

print("ok")
