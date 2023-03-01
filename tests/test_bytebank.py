import pytest
from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  #Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When-ação

        assert resultado == esperado #Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho '  # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado #then

    def test_quando_decrescimo_salario_recebe_100000_e_sobrenome_in_sobrenomes_diretor_retornar_90000(self):
        #sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000 #Given

        funcionario_diretor = Funcionario(entrada_nome, '15/11/1965',entrada_salario)
        funcionario_diretor.decrescimo_salario() #when
        resultado = funcionario_diretor.salario

        assert resultado == esperado #Then

    def test_quando_calcular_salario_recebe_1000_retorna_100(self):
        entrada_salario = 1000
        esperado = 100  # Given

        funcionario = Funcionario('teste', '15/11/1965', entrada_salario)
        resultado = funcionario.calcular_bonus()  # when

        assert resultado == esperado  # Then

    def test_quando_calcular_salario_recebe_20000_retorna_Exception(self):
        with pytest.raises(Exception):
            entrada_salario = 20000 # Given

            funcionario = Funcionario('teste', '15/11/1965', entrada_salario)
            resultado = funcionario.calcular_bonus()  # when

            assert resultado  # Then

