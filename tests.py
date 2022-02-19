# Optei por não usar nenhuma framework para testes para tornar o programa mais simples de ser executado
# Evitando assim o incômodo de ter que baixar e instalar bibliotecas externas

from questao2 import valida_senha
from questao3 import contador_anagramas


def test_valida_senha():
    """Testa se uma senha é válida, conforme exemplos dados na questão 02"""
    if not valida_senha('Ya3'):
        if valida_senha('Ya3&ab'):
            return True

def test_contador_anagramas():
    """Testa se o contador de anagramas funciona, conforme os exemplos dados na questão 03"""
    anagramas = contador_anagramas('ifailuhkqq')
    if anagramas == 3:
        return True
    
if __name__ == '__main__':
    passou_no_teste = 0
    if test_valida_senha():
        passou_no_teste += 1
    if test_contador_anagramas():
        passou_no_teste += 1
        
    print(f"Resultados dos testes: {passou_no_teste}/2 ")