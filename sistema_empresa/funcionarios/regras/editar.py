from funcionarios.banco_dados.repositorio import funcionarios
from funcionarios.regras.buscar import get_funcionario

def edit_funcionario(codigo: int,nome: str,cargo: str,telefone: str,status: str,salario: float):
    funcionario = get_funcionario(codigo)
    if funcionario:
        funcionario['nome'] = nome
        funcionario['cargo'] = cargo
        funcionario['telefone'] = telefone
        funcionario['status'] = status
        funcionario['salario'] = salario
        print('Funcionário editado com sucesso !')
        return None
    print('Funcionário não encontrado !')
    return None