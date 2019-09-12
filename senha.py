#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

login = input("Digite o login: \n")
senha = input("Digite uma senha: \n")

while login == senha:
    senha = input("A senha nao pode ser igual ao login. Digite uma nova senha: \n")

print("Senha cadastrada com sucesso!")
