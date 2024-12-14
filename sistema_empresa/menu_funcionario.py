from funcionarios.banco_dados.repositorio import funcionarios
from funcionarios.regras.buscar import get_funcionario
from funcionarios.regras.cadastrar import add_funcionario
from funcionarios.regras.deletar import delete_funcionario
from funcionarios.regras.listar import listar_funcionario
from funcionarios.regras.editar import edit_funcionario

def menu_funcionarios(): #MENU FUNCIONARIOS
    while True:
        print('-------------------------------------------')
        print("|                                         |")
        print("|                Opções:                  |")
        print("|  Opção 1- Cadastrar funcionário         |")
        print("|  Opção 2- Listar funcionários           |")
        print("|  Opção 3- Editar funcionário            |")
        print("|  Opção 4- Buscar funcionários           |")
        print("|  Opção 5- Deletar funcionários          |")
        print("|  Opção 0- Menu Inicial                  |")
        print("|                                         |")
        print('-------------------------------------------')

        opcao = input('Digite uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome do funcionário: ')
            cargo = input('Digite o cargo do funcionário: ')
            telefone = input('Digite o telefone do funcionário: ')
            cpf = input('Digite o CPF do funcionário: ')
            status = input('Digite o status do funcionário: ')
            salario = float(input('Digite o salário do funcionário: '))

            add_funcionario(nome,cargo,telefone,cpf,status,salario)
        elif opcao == '2':
            listar_funcionario()
        elif opcao == '3': 
            codigo = int(input('Digite o código do funcionário que deseja editar: '))
            nome = input('Digite o novo nome do funcionário: ')
            cargo = input('Digite o novo cargo do funcionário: ')
            telefone = input('Digite o novo telefone do funcionário: ')
            status = input('Digite o novo status do funcionário: ')
            salario = float(input('Digite o novo salário do funcionário: '))

            edit_funcionario(codigo,nome,cargo,telefone,status,salario)
        elif opcao == '4':
            codigo = int(input('Digite o código do funcionário que deseja buscar: ')) 

            print(get_funcionario(codigo))
        elif opcao == '5':
            codigo = int(input('Digite o código do funcionário que deseja deletar: '))

            delete_funcionario(codigo)
        elif opcao == '0':
            print('Voltou ao menu inicial')
            break
        else:
            print('Opção inválida. Tente novamente !')