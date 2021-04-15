import itertools

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
    
login = input(str("Nome de Usuario: "))
password = input(str("Senha: "))

while password == login:
    print("\nERRO")
    print("Seu nome de usuario nao pode ser igual a sua senha.\n")
    login = input(str("Nome de Usuario: "))
    password = input(str("Senha: "))

    
