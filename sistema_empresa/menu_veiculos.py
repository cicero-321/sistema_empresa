from veiculos.banco_dados.repositorio import veiculos
from veiculos.regras.buscar import get_veiculo
from veiculos.regras.cadastrar import add_veiculo
from veiculos.regras.deletar import delete_veiculo
from veiculos.regras.listar import listar_veiculo
from veiculos.regras.editar import edit_veiculo

def menu_veiculos(): #MENU FUNCIONARIOS
    while True:
        print('-------------------------------------------')
        print("|                                         |")
        print("|                Opções:                  |")
        print("|  Opção 1- Cadastrar veículo             |")
        print("|  Opção 2- Listar veículos               |")
        print("|  Opção 3- Editar veículo                |")
        print("|  Opção 4- Buscar veículos               |")
        print("|  Opção 5- Deletar veículos              |")
        print("|  Opção 0- Menu Inicial                  |")
        print("|                                         |")
        print('-------------------------------------------')

        opcao = input('Digite uma opção: ')

        if opcao == '1':
            modelo = input('Digite o modelo do veículo: ')
            placa = input('Digite a placa do veículo: ')
            chassi = input('Digite o chassi do veículo: ')
            proprietario = input('Digite o proprietário do veículo: ')
            cor = input('Digite a cor do veículo: ')
            quilometragem = float(input('Digite a quilometragem: '))

            add_veiculo(modelo,placa,chassi,proprietario,cor,quilometragem)
        elif opcao == '2':
            listar_veiculo()
        elif opcao == '3': 
            placa = input('Digite a placa no veículo que vocÊ deseja editar: ')

            modelo = input('Digite o modelo: ')
            chassi = input('Digite o chassi: ')
            proprietario = input('Digite o proprietário: ')
            cor = input('Digite a cor: ')
            quilometragem = float(input('Digite a quilometragem: '))

            edit_veiculo(placa,modelo,chassi,proprietario,cor,quilometragem)
        elif opcao == '4':
            placa = input('Digite a placa: ')

            print(get_veiculo(placa))
            
        elif opcao == '5':
            placa = input('Digite a placa para deletar: ')

            delete_veiculo(placa)
        elif opcao == '0':
            print('Voltou ao menu inicial')
            break
        else:
            print('Opção inválida. Tente novamente !')