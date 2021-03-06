"""
# Questão 01

Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
A base e altura da escada devem ser iguais ao valor de n. 
A última linha não deve conter nenhum espaço.
"""

def cria_escada(numero):
    """Recebe um inteiro e monta uma escada com a mesma proporção para base e altura,
    com espaços no lado esquerdo"""

    for i in range(0, numero):
        for j in range(0, numero):
            if i < j:
                print(" ", end="")
        print("*" * (i + 1))
    print()

if __name__ == '__main__':
    while True:
        try:
            numero = int(input('Digite o número de linhas:'))
        except ValueError:
            print("Digite um número inteiro")
        cria_escada(numero)
