"""
# Questão 03

Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra.
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas
"""

def contador_anagramas(palavra):
    contador = 0

    for k in range(1, len(palavra)):
        for i in range(0, len(palavra)-k):
            for j in range(i+1, len(palavra)+1-k):
                aux1 = "".join(sorted(palavra[i:i+k]))
                aux2 = "".join(sorted(palavra[j:j+k]))
                if aux1 == aux2:
                    contador += 1
    
    return contador

if __name__ == '__main__':
    while True:
        palavra = str(input("Digite uma palavra para descobrir quantos anagramas ela possui: ")).lower()
        contador = contador_anagramas(palavra)
        print(f"\nA palavra {palavra} possui {contador} anagramas")
    
    