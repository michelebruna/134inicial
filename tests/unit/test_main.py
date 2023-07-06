import csv

import pytest

from main import somar, subtrair, multiplicar, dividir


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:   # o newline é o que ignora a primeira linha, o cabeçalho
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


def teste_somar():
    # O teste é sempre dividido em três partes
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido  # assert é o comando para comparar os dados


def teste_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    # Não utilizar o try exception no def principal, utilizar no def teste
    numero_a = 27
    numero_b = 3

    # 1.2 = Resultados Esperados
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


# No mercardo atual estão separando os testes, igual foi feito com o dividir_positivo e dividir_negativo
def teste_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    # Não utilizar o try exception no def principal, utilizar no def teste
    numero_a = 27
    numero_b = 0

    # 1.2 = Resultados Esperados
    resultado_esperado = 'Não dividirás por zero'

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


# lista para uso como massa de teste. Essa lista se chama de tupla
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # O teste é sempre dividido em três partes
    # 1 - Configura
    # Utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido  # assert é o comando para comparar os dados


@pytest.mark.parametrize('numero_a,numero_b,resultado_esperado',ler_csv('C:\\Users\\miche\\PycharmProjects\\pythonProject\\134inicial\\vendors\\csv\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # O teste é sempre dividido em três partes
    # 1 - Configura
    # Utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)  # assert é o comando para comparar os dados

# TDD - Teste Driven tedelopment
#       Desenvolvimento Direcionado por Teste
#
# - Criar todos os testes de unidade no começo
# - Executar todos os testes pelo menos 1 vez por dia
#
# Imagine que você no 1º dia (nada pronto)
# Você execute todos os testes -  o que acontece?
# Dia 01 - Falhou 100 - Passou 000
# Dia 02 - Falhou 095 - Passou 005
# Dia 03 - Falhou 090 - Passou 010
# dia 04 - Falhou 088 - Passou 012
# dia 05 - Falhou 081 - Passou 019
# Dia 06 - Falhou 075 - Passou 025
# Informação sobre o progresso
# Insistir mais um dia      1 + 1 = 2?
# Pedir ajuda               1 + 2 = 3
# Devolver e pegar outra    1 + 1 = 2!
# TDD: Teste é uma medida de progresso


# CI: Continuous Integration
# IC: Integração Contínua

# (Build) --> Suite de Testes ----> (Build)
#             Automatizada Passou
# Ambiente de Desenvolvimento       Então, move >> Ambiente de Teste


# CD: Continuous Delivery
# EC: Entrega Contínua

# (Build) --> Suite de Teste -- > (Build)
# Dev          Muitos Testes      Produção


# Eu vi este comentário
