#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
#taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
#uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
#necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas
#as taxas de crescimento.
#Altere o programa anterior (populacao.py - est_repeticao) permitindo ao usuário informar as populações
# e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

pais_A = float(input("Digite a populacao atual do país A: \n"))

while pais_A <=0:
    print("A populacao precisa ser maior que zero")
    pais_A = float(input("Digite a populacao atual do país A: \n"))

taxa_A = float(input("Qual o percenutual de taxa de crescimento do país A? Digite sem o '%''\n"))
while taxa_A <=0:
    print("A taxa precisa ser maior que zero")
    taxa_A = float(input("Qual o percenutual de taxa de crescimento do país A? Digite sem o '%''\n"))

pais_B = float(input("Digite a populacao atual do país B: \n"))

while pais_B <=0:
    print("A populacao precisa ser maior que zero")
    pais_B = float(input("Digite a populacao atual do país B?\n"))

taxa_B = float(input("Qual o percenutual de taxa de crescimento do país B? Digite sem o '%''\n"))
while taxa_B <=0:
    print("A taxa precisa ser maior que zero")
    taxa_B = float(input("Qual o percenutual de crescimento do país B? Digite sem o '%'\n"))


taxa_A= taxa_A/100
taxa_B = taxa_B/100

if taxa_A < taxa_B:
    print("O país A nunca alcancará a populacao do país B, pois sua taxa de crescimento é menor")
    quit()


anos = 0
while pais_A < pais_B:
    pais_A = pais_A + (pais_A*taxa_A)
    pais_B = pais_B + (pais_B*taxa_B)
    anos += 1


pais_A = round(pais_A, 2)
pais_B = round(pais_B,2)

futuro = 2019 + anos

print(f"O país A alcancará a populacao do país B em {anos} anos.")
print(f"País A: {pais_A} pessoas em {futuro}")
print(f"País A: {pais_B} pessoas em {futuro}")
