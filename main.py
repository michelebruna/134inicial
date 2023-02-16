import pytest

# Na parte de cima fica o desenvolvimento e embaixo as funções. Quando for teste pode usar direto na função.
def print_hi(name):
    print(f'Hi, {name}')

def somar (numero_a, numero_b):
    resultado = numero_a + numero_b
    return resultado


if __name__ == '__main__': # Essa linha não muda nunca, é onde indica que iniciou.
    print_hi('Michele')

    resultado = somar(5,7)
    print(f' A soma: {resultado}')


def teste_somar():
    # O teste é sempre dividido em três partes
    # 1 - Configurar
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executar
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Validar
    assert resultado_esperado == resultado_obtido

