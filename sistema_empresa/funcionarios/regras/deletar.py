from funcionarios.banco_dados.repositorio import funcionarios
from funcionarios.regras.buscar import get_funcionario

def delete_funcionario(codigo: int) -> dict | None:
    funcionario = get_funcionario(codigo)
    if funcionario:
        funcionarios.remove(funcionario)
        print('Cadastro removido !')
        return None
    print('Cadastro não encontrado !')
    return None