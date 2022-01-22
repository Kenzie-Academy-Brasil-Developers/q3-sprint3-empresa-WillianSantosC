class Funcionario:
    
    funcao = "Funcionario"
    
    def __init__(self, nome: str, sobrenome: str, cpf: str, salario: str = 3000) -> None:
        self.nome = nome.strip().capitalize()
        self.sobrenome = " ".join(sobrenome.title().split())
        self.cpf = cpf
        self.salario = salario
        self.nome_completo = f'{self.nome} {self.sobrenome}'.title()
        
    def __str__(self):
        return f'<{self.funcao}: {self.nome_completo}>'

    def __repr__(self):
        return f'<{self.funcao}: {self.nome_completo}>'

class Gerente(Funcionario):

    funcao = "Gerente"
    
    def __init__(self, nome: str, sobrenome: str, cpf: str) -> None:
        super().__init__(nome, sobrenome, cpf, 8000)
        self.funcionarios = []
        
    def __str__(self):
        return f'<{self.funcao}: {self.nome_completo}>'

    def __repr__(self):
        return f'<{self.funcao}: {self.nome_completo}>'
    
    def aumento_salarial(self, funcionario, empresa):
        aumento = int(funcionario.salario * 1.1)

        if not type(funcionario) is Funcionario or funcionario not in self.funcionarios:
            return False

        if aumento > 8000:
            empresa.promocao(empresa, funcionario)

        else:
            funcionario.salario = aumento
        return True
        
class Empresa():
    
    def __init__(self, nome: str, cnpj: str) -> None:
        self.nome = " ".join(nome.strip().split()).title()
        self.cnpj = str(cnpj)
        self.contratados = []
        
    def __str__(self):
        return f'<Empresa: {self.nome}>'

    def __repr__(self):
        return f'<Empresa: {self.nome}>'
    
    def contratar_funcionario(self, funcionario) -> str:
        if funcionario in self.contratados:
            return "Funcionário com esse CPF já foi contratado."

        self.contratados.append(funcionario)
        nome_completo_tratado = ".".join(funcionario.nome_completo.lower().split())
        nome_empresa_tratado = "".join(self.nome.lower().split())
        funcionario.email = f"{nome_completo_tratado}@{nome_empresa_tratado}.com"

        return "Funcionário contratado!"
        
    @staticmethod
    def adicionar_funcionario_para_gerente(gerente, funcionario):
        if not type(gerente) == Gerente or not type(funcionario) == Funcionario:
            return False

        if funcionario in gerente.funcionarios:
            return 'Funcionario já está na lista de funcionarios desse gerente.'

        gerente.funcionarios.append(funcionario)
        return 'Funcionário adicionado à lista do gerente!'
    
    def demissao(self, funcionario):
        self.contratados.remove(funcionario)

        if type(funcionario) is Gerente:
            return "Gerente demitido!"

        for x in self.contratados:
            if x.funcao == "Gerente":
                if funcionario in x.funcionarios:
                    x.funcionarios.remove(funcionario)

        return "Funcionário demitido!"
        
        
    @staticmethod
    def promocao(empresa, funcionario):
        if type(funcionario) != Funcionario or funcionario not in empresa.contratados:
            return False

        empresa.contratados.remove(funcionario)
        
        funcionario_promovido = Gerente(funcionario.nome, funcionario.sobrenome, funcionario.cpf)
        empresa.contratar_funcionario(funcionario_promovido)

        return True