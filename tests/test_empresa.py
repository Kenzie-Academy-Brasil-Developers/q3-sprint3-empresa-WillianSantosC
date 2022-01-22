from inheritance import Empresa, Funcionario, Gerente
from pytest import fail


def test_validacao_dos_atributos_da_classe_empresa(empresa_mock: dict):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])

    for key in empresa_mock.keys():
        assert hasattr(
            empresa, key
        ), f"Verifique se o atributo `{key}` existe em sua classe."


def test_empresa_sendo_criada_corretamente(empresa_mock: dict):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])

    assert (
        empresa.__dict__ == empresa_mock
    ), "Verifique se o empresa está sendo criado corretamente"


def test_retorno_metodos_magicos_da_classe_empresa(empresa_mock: dict):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])

    assert f"<Empresa: {empresa.nome}>" in str(empresa)
    assert f"<Empresa: {empresa.nome}>" in str(empresa.__repr__)


def test_normalizacao_dos_dados_classe_empresa():
    esperado = {
        "nome": "Uma Empresa Qualquer",
        "cnpj": "12345678910124",
        "contratados": list(),
    }

    empresa = Empresa(nome="  uma    Empresa qualquer  ", cnpj=12345678910124)

    assert empresa.__dict__ == esperado


def test_metodo_de_instancia_contratar_funcionario_classe_empresa(
    empresa_mock: dict, funcionario_mock: dict
):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])
    funcionario = Funcionario(
        funcionario_mock["nome"], funcionario_mock["sobrenome"], funcionario_mock["cpf"]
    )

    esperado = [
        "funcionário contratado!",
        "funcionario contratado!",
        "funcionario contratado",
    ]

    recebido = empresa.contratar_funcionario(funcionario).lower()

    assert recebido in esperado
    assert funcionario in empresa.contratados


def test_metodo_de_instancia_contratar_funcionarios_mesmo_cpf_classe_empresa(
    empresa_mock: dict, funcionario_mock: dict
):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])
    funcionario = Funcionario(
        funcionario_mock["nome"], funcionario_mock["sobrenome"], funcionario_mock["cpf"]
    )

    esperado = [
        "funcionário com esse cpf já foi contratado.",
        "funcionário com esse cpf ja foi contratado.",
        "funcionario com esse cpf já foi contratado.",
        "funcionário com esse cpf já foi contratado",
        "funcionário com esse cpf ja foi contratado",
        "funcionario com esse cpf já foi contratado",
    ]

    empresa.contratar_funcionario(funcionario)
    recebido = empresa.contratar_funcionario(funcionario).lower()

    assert recebido in esperado
    assert empresa.contratados.count(funcionario) == 1


def test_metodo_de_instancia_contratar_funcionarios_email_correto_funcionario_classe_empresa():
    empresa = Empresa("Empresa LTDA", "11223344556677")
    funcionario = Funcionario("Roberto", "Santiago", "11122233344")

    empresa.contratar_funcionario(funcionario)
    esperado = "roberto.santiago@empresaltda.com"
    recebido = funcionario.email

    assert (
        esperado == recebido
    ), f"Verifique se o email está sendo salvo da forma correta.\nEsperado -> {esperado}\nRecebido -> {recebido}"


def test_metodo_estatico_adicionar_funcionario_para_gerente(
    gerente_mock: dict, funcionario_mock: dict
):
    gerente = Gerente(
        gerente_mock["nome"], gerente_mock["sobrenome"], gerente_mock["cpf"]
    )
    funcionario = Funcionario(
        funcionario_mock["nome"], funcionario_mock["sobrenome"], funcionario_mock["cpf"]
    )

    nao_gerente = Empresa.adicionar_funcionario_para_gerente(gerente, gerente)
    nao_funcionario = Empresa.adicionar_funcionario_para_gerente(
        funcionario, funcionario
    )

    esperado = [
        "funcionário adicionado à lista do gerente!",
        "funcionario adicionado a lista do gerente!",
        "funcionário adicionado a lista do gerente!",
        "funcionario adicionado à lista do gerente!",
        "funcionário adicionado à lista do gerente",
        "funcionario adicionado a lista do gerente",
        "funcionário adicionado a lista do gerente",
        "funcionario adicionado à lista do gerente",
    ]

    try:
        recebido = Empresa.adicionar_funcionario_para_gerente(
            gerente, funcionario
        ).lower()

    except AttributeError:
        fail(
            "Verifique se a ordem dos parâmetros está seguindo o enunciado da entrega."
        )

    assert (
        nao_gerente is False
    ), f"Verifique se o método de classe está com o retorno certo.\nEsperado -> False\nRecebido -> {nao_gerente}"

    assert (
        nao_funcionario is False
    ), f"Verifique se o método de classe está com o retorno certo.\nEsperado -> False\nRecebido -> {nao_funcionario}"

    assert (
        recebido in esperado
    ), f"Verifique se a resposta está conforme o enunciado da entrega pede."

    assert (
        funcionario in gerente.funcionarios
    ), "Verifique se o `Funcionario` está realmente sendo adicionado a lista de funcionarios do `Gerente`"


def test_metodo_estatico_adicionar_funcionario_para_gerente_duas_vezes(
    gerente_mock: dict, funcionario_mock: dict
):
    gerente = Gerente(
        gerente_mock["nome"], gerente_mock["sobrenome"], gerente_mock["cpf"]
    )
    funcionario = Funcionario(
        funcionario_mock["nome"], funcionario_mock["sobrenome"], funcionario_mock["cpf"]
    )

    esperado = [
        "funcionario já está na lista de funcionarios desse gerente.",
        "funcionario ja está na lista de funcionarios desse gerente.",
        "funcionario já esta na lista de funcionarios desse gerente.",
        "funcionario ja esta na lista de funcionarios desse gerente.",
        "funcionario já está na lista de funcionarios desse gerente",
        "funcionario ja está na lista de funcionarios desse gerente",
        "funcionario já esta na lista de funcionarios desse gerente",
        "funcionario ja esta na lista de funcionarios desse gerente",
    ]

    Empresa.adicionar_funcionario_para_gerente(gerente, funcionario)
    recebido = Empresa.adicionar_funcionario_para_gerente(gerente, funcionario).lower()

    assert (
        gerente.funcionarios.count(funcionario) == 1
    ), "Verifique se o seu método está adicionando funcionarios repetidos à lista de funcionarios."
    assert (
        recebido in esperado
    ), "Verifique se a mensagem de retorno está seguindo o enuciado."


def test_metodo_de_instancia_demissao_gerente_classe_empresa(
    empresa_mock: dict, gerente_mock: dict
):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])
    gerente = Gerente(
        gerente_mock["nome"], gerente_mock["sobrenome"], gerente_mock["cpf"]
    )

    empresa.contratar_funcionario(gerente)

    esperado = ["gerente demitido!", "gerente demitido"]

    recebido = empresa.demissao(gerente).lower()

    assert (
        recebido in esperado
    ), "Mensagem de retorno para demissão do `Gerente` não segue o pedido na entrega."
    assert gerente not in empresa.contratados, "`Gerente` não foi removido da empresa."


def test_metodo_de_instancia_demissao_funcionario_classe_empresa(
    empresa_mock: dict, gerente_mock: dict, funcionario_mock: dict
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
    empresa.adicionar_funcionario_para_gerente(gerente, funcionario)

    esperado = [
        "funcionário demitido!",
        "funcionario demitido!",
        "funcionário demitido",
        "funcionario demitido",
    ]

    recebido = empresa.demissao(funcionario).lower()

    assert recebido in esperado, "Verifique se sua mensagem está seguindo o enunciado."
    assert (
        funcionario not in empresa.contratados
    ), "Verifique se o funcionario está sendo removido da lista de contratados da empresa."
    assert (
        funcionario not in gerente.funcionarios
    ), "Verifique se o funcionario está sendo removida da lista de funcionarios do gerente."


def test_metodo_estatico_promocao_classe_empresa(
    empresa_mock: dict, gerente_mock: dict, funcionario_mock: dict
):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])
    funcionario = Funcionario(
        funcionario_mock["nome"], funcionario_mock["sobrenome"], funcionario_mock["cpf"]
    )

    empresa.contratar_funcionario(funcionario)

    gerente_mock["nome"] = funcionario_mock["nome"]
    gerente_mock["sobrenome"] = funcionario_mock["sobrenome"]
    gerente_mock["cpf"] = funcionario_mock["cpf"]
    gerente_mock["nome_completo"] = funcionario_mock["nome_completo"]
    gerente_mock["email"] = funcionario.email

    esperado = True
    recebido = empresa.promocao(empresa, funcionario)

    contratados = [contratado.__dict__ for contratado in empresa.contratados]

    assert (
        esperado == recebido
    ), "Verifique se o retorno desse método segue o enunciado."
    assert gerente_mock == contratados[0]


def test_metodo_estatico_promocao_funcionario_nao_contartado_nao_funcionario(
    empresa_mock: dict, gerente_mock: dict, funcionario_mock: dict
):
    empresa = Empresa(empresa_mock["nome"], empresa_mock["cnpj"])
    gerente = Gerente(
        gerente_mock["nome"], gerente_mock["sobrenome"], gerente_mock["cpf"]
    )
    funcionario = Funcionario(
        funcionario_mock["nome"], funcionario_mock["sobrenome"], funcionario_mock["cpf"]
    )

    esperado = False
    recebido = empresa.promocao(empresa, funcionario)

    assert (
        esperado == recebido
    ), "Verifique se o retorno desse método segue o enunciado."

    recebido = empresa.promocao(empresa, gerente)

    assert (
        esperado == recebido
    ), "Verifique se o retorno desse método segue o enunciado."
