from funcionarios.banco_dados.repositorio import funcionarios
codigo_atual = 1

def add_funcionario(nome: str,cargo: str,telefone: str,cpf: str,status: str,salario: float):
    global codigo_atual
    codigo_atual += 1
    novo_funcionario = {
        'nome' : nome,
        'cargo' : cargo,
        'codigo' : codigo_atual,
        'telefone' : telefone,
        'CPF' : cpf,
        'status' : status,
        'salario' : salario
    }

    funcionarios.append(novo_funcionario)
    print('Funcionário cadastrado com sucesso! ')