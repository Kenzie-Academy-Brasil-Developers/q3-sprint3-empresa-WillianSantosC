from inheritance import Funcionario
from pytest import fail


def test_validacao_dos_atributos_da_classe_funcionario(funcionario_mock: dict):
    funcionario = Funcionario(
        funcionario_mock["nome"],
        funcionario_mock["sobrenome"],
        funcionario_mock["cpf"],
    )

    for key in funcionario_mock.keys():
        assert hasattr(
            funcionario, key
        ), f"Verifique se o atributo `{key}` existe em sua classe."


def test_funcionario_sendo_criado_corretamente(funcionario_mock: dict):
    funcionario = Funcionario(
        funcionario_mock["nome"],
        funcionario_mock["sobrenome"],
        funcionario_mock["cpf"],
    )

    assert (
        funcionario.__dict__ == funcionario_mock
    ), "Verifique se o funcionario está sendo criado corretamente"


def test_retorno_metodos_magicos_classe_funcionario(funcionario_mock: dict):
    funcionario = Funcionario(
        funcionario_mock["nome"],
        funcionario_mock["sobrenome"],
        funcionario_mock["cpf"],
    )

    assert f"<Funcionario: {funcionario.nome_completo}>" in str(funcionario)
    assert f"<Funcionario: {funcionario.nome_completo}>" in str(funcionario.__repr__)


def test_normalizacao_dos_dados_classe_funcionario():
    esperado = {
        "nome": "Monkey",
        "sobrenome": "D. Luffy",
        "cpf": "12345678910",
        "salario": 3000,
        "nome_completo": "Monkey D. Luffy",
    }

    funcionario = Funcionario(
        nome="  monkey  ", sobrenome=" d.    luffy  ", cpf="12345678910"
    )

    assert funcionario.__dict__ == esperado
