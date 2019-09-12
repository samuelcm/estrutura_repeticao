#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
#taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
#uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
#necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas
#as taxas de crescimento.

pais_A = 80000
taxa_A = 0.03

pais_B = 200000
taxa_B = 0.015

anos = 0

while pais_A < pais_B:
    pais_A = pais_A + (pais_A*taxa_A)
    pais_B = pais_B + (pais_B*taxa_B)
    anos = anos +1

pais_A = round(pais_A, 2)
pais_B = round(pais_B,2)

print(f"Foi preciso {anos} anos para que o país A alcançar a população do país B")
print(f"Pais A: populacao de {pais_A} pessoas")
print(f"Pais B: populacao de {pais_B} pessoas")
