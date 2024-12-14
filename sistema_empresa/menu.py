from menu_funcionario import menu_funcionarios
from menu_veiculos import menu_veiculos

while True:
        print('-------------------------------------------')
        print("|                                         |")
        print("|                Opções:                  |")
        print("|  Opção 1- Área funcionários             |")
        print("|  Opção 2- Área veículos                 |")
        print("|  Opção 0- Encerra programa              |")
        print("|                                         |")
        print('-------------------------------------------')

        opcao = input('Digite uma opção: ')

        if opcao == '1':
            menu_funcionarios()
        elif opcao == '2':
            menu_veiculos()
        elif opcao == '0':
            break
        else:
            print('Opção inválida. Tente novamente !')