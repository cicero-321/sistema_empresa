from funcionarios.banco_dados.repositorio import funcionarios

def listar_funcionario() -> None:
    print('---- FUNCIONÁRIOS CADASTRADOS ----')
    for funcionario in funcionarios:
        print(f'Nome : {funcionario['nome']}')
        print(f'Cargo : {funcionario['cargo']}')
        print(f'Codigo : {funcionario['codigo']}')
        print(f'Telefone : {funcionario['telefone']}')
        print(f'CPF : {funcionario['CPF']}')
        print(f'Status : {funcionario['status']}')
        print(f'Salario : {funcionario['salario']}')
        print('-'*70)