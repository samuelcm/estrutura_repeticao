#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

print("Precisamos realizar seu cadastro.")
nome = input("Digite um nome com mais de 3 caracteres\n")

#VERIFICANDO O NOME
while len(nome)<=3:
    print("O nome precisa ter mais de 3 caracteres.")
    nome = input("Digite um nome com mais de 3 caracteres\n")

#VERIFICANDO A IDADE
idade = int(input("Digite sua idade:\n"))
while idade <0 or idade>150:
    print("A idade precisa ser entre 0 e 150.")
    idade = int(input("Digite sua idade:\n"))

#VERIFICANDO O SALARIO
salario = float(input("Digite seu salário: \n"))
while salario <=0:
    print("O salário nao pode igual ou menor que zero")
    salario = float(input("Digite seu salário: \n"))

#VERIFICANDO O SEXO
sexo = input("Qual seu sexo?\n")
lista_sexo = ['m', 'f']
while sexo not in lista_sexo:
    print("Sexo nao valido")
    sexo = input("Qual seu sexo?\n")


#VERIFICANDO O ESTADO CIVIL
Estado_civil = input("Qual seu estado civil? Digite s-solteiro, c-casado, v-viuvo ou d-divorciado:\n")
lista_estado = ['s', 'c', 'v', 'd']
while Estado_civil not in lista_estado:
    print("Para Estado Civil digite: 's', 'c', 'v', 'd'")
    Estado_civil = input("Qual seu estado civil?Digite s-solteiro, c-casado, v-viuvo ou d-divorciado:\n")

print("Cadastro realizado com sucesso!")
