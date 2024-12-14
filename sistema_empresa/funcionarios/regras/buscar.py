from funcionarios.banco_dados.repositorio import funcionarios

def get_funcionario(codigo: int) -> dict | None:
    for funcionario in funcionarios:
        if funcionario['codigo'] == codigo:
            return funcionario
    print('Funcionário não encontrado !')
    return None