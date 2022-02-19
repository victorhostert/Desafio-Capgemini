"""
# Questão 02

Débora se inscreveu em uma rede social para se manter em contato com seus amigos.
A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. 
O site considera uma senha forte quando ela satisfaz os seguintes critérios:
●	Possui no mínimo 6 caracteres.
●	Contém no mínimo 1 digito.
●	Contém no mínimo 1 letra em minúsculo.
●	Contém no mínimo 1 letra em maiúsculo.
●	Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+
Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte.
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados
para uma string qualquer ser considerada segura.
"""

def valida_senha(string):
    """Valida a senha garantindo que cumpra os requisitos"""

    numero = 0
    maiusculo = 0
    minusculo = 0
    especial = 0

    for i in range(0, len(string)):
        if string[i].isnumeric():
            numero += 1
            break

    for i in range(0, len(string)):
        if string[i].isupper():
            maiusculo += 1
            break

    for i in range(0, len(string)):
        if string[i].islower():
            minusculo += 1
            break

    simbolos = '!@#$%^&*()-+'
    for caractere in string:
        if caractere in simbolos:
            especial += 1
            break

    if len(string) < 6:
        falta = 6 - len(string)

        print("\nUma senha forte possui ao menos 6 caracteres")
        if len(string) == 1:
            print(f"Sua senha possui apenas um caractere, faltam {falta} para ser uma senha forte\n")
        else:
            print(f"Sua senha possui apenas {len(string)} caracteres, faltam {falta} para ser uma senha forte\n")

    else:
        if (numero == 0) or (maiusculo == 0) or (minusculo == 0) or (especial == 0):
            print("\nSua senha deve conter:")
            if numero == 0:
                print("Pelo menos 1 número.")
            if maiusculo == 0:
                print("Pelo menos 1 caractere em maiúsculo.")
            if minusculo == 0:
                print("Pelo menos 1 caractere em minúsculo.")
            if especial == 0:
                print("Pelo menos 1 caractere especial.")
            print()
        else:
            return True

if __name__ == '__main__':
    print("\nUma senha segura deve conter 6 caracteres, sendo estes 1 número, 1 letra maíuscula, 1 letra minúscula, e 1 símbolo")
    senha = input("\nDigite sua senha segura: ")


    while True:
        if valida_senha(senha):
            print("Sua senha é forte!\n")
            break
        else:
            senha = input("\nDigite uma nova senha: ")