from inheritance import Gerente, Empresa, Funcionario
from pytest import fail


def test_validacao_dos_atributos_da_classe_gerente(gerente_mock: dict):
    gerente = Gerente(
        gerente_mock["nome"],
        gerente_mock["sobrenome"],
        gerente_mock["cpf"],
    )

    for key in gerente_mock.keys():
        assert hasattr(
            gerente, key
        ), f"Verifique se o atributo `{key}` existe em sua classe."


def test_gerente_sendo_criado_corretamente(gerente_mock: dict):
    gerente = Gerente(
        gerente_mock["nome"],
        gerente_mock["sobrenome"],
        gerente_mock["cpf"],
    )

    assert (
        gerente.__dict__ == gerente_mock
    ), "Verifique se o gerente está sendo criado corretamente"


def test_retorno_metodos_magicos_classe_gerente(gerente_mock: dict):
    gerente = Gerente(
        gerente_mock["nome"],
        gerente_mock["sobrenome"],
        gerente_mock["cpf"],
    )

    assert f"<Gerente: {gerente.nome_completo}>" in str(gerente)
    assert f"<Gerente: {gerente.nome_completo}>" in str(gerente.__repr__)


def test_normalizacao_dos_dados_classe_gerente():
    esperado = {
        "nome": "Monkey",
        "sobrenome": "D. Luffy",
        "cpf": "12345678910",
        "salario": 8000,
        "nome_completo": "Monkey D. Luffy",
        "funcionarios": list(),
    }

    gerente = Gerente(nome="  monkey  ", sobrenome=" d.    luffy  ", cpf="12345678910")

    assert gerente.__dict__ == esperado


def test_metodo_de_instancia_aumento_salarial_classe_gerente(
    gerente_mock: dict, funcionario_mock: dict, empresa_mock: dict
):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])
    gerente = Gerente(
        gerente_mock["nome"], gerente_mock["sobrenome"], gerente_mock["cpf"]
    )
    funcionario = Funcionario(
        funcionario_mock["nome"], funcionario_mock["sobrenome"], funcionario_mock["cpf"]
    )

    empresa.contratar_funcionario(gerente)
    empresa.contratar_funcionario(funcionario)

    assert (
        gerente.aumento_salarial(funcionario, empresa) is False
    ), "Verifique se o retorno do seu método está igual o enunciado."
    assert (
        gerente.aumento_salarial(gerente, empresa) is False
    ), "Verifique se o retorno do seu método está igual o enunciado."

    empresa.adicionar_funcionario_para_gerente(gerente, funcionario)

    assert (
        gerente.aumento_salarial(funcionario, empresa) is True
    ), "Verifique se o retorno do seu método está igual o enunciado."
    assert (
        funcionario.salario == 3300
    ), "Verifique se o calculo para aumento de salario está correto."

    for _ in range(10):
        assert type(funcionario.salario) is int
        gerente.aumento_salarial(funcionario, empresa)

    for contratado in empresa.contratados:
        assert (
            isinstance(contratado, Gerente) is True
        ), "Verifique se o seu método está fazendo a criação do gerente."
