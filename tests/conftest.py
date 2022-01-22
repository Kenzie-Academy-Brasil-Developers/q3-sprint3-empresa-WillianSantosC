from pytest import fixture

from faker import Faker
from faker.providers.person import Provider as ProviPerson
from faker.providers.company import Provider as ProviCompany

from typing import Union

from inheritance import Funcionario, Empresa, Gerente

FAKE: Union[ProviCompany, ProviPerson] = Faker()


@fixture
def funcionario_mock():
    nome = FAKE.first_name()
    sobrenome = FAKE.last_name()

    mock = {
        "nome": nome,
        "sobrenome": sobrenome,
        "cpf": str(FAKE.random_number(digits=11, fix_len=True)),
        "salario": 3000,
        "nome_completo": nome + " " + sobrenome,
    }

    return mock


@fixture
def gerente_mock():
    nome = FAKE.first_name()
    sobrenome = FAKE.last_name()

    mock = {
        "nome": nome,
        "sobrenome": sobrenome,
        "cpf": str(FAKE.random_number(digits=11, fix_len=True)),
        "salario": 8000,
        "nome_completo": nome + " " + sobrenome,
        "funcionarios": list(),
    }

    return mock


@fixture
def empresa_mock():
    mock = {
        "nome": FAKE.company().title().replace(",", ""),
        "cnpj": str(FAKE.random_number(digits=14, fix_len=True)),
        "contratados": list(),
    }

    return mock
