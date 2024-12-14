from veiculos.banco_dados.repositorio import veiculos

def listar_veiculo() -> None:
    print('---- VEÍCULOS CADASTRADOS ----')
    for veiculo in veiculos:
        print(f'Modelo : {veiculo['modelo']}')
        print(f'Placa : {veiculo['placa']}')
        print(f'Chassi : {veiculo['chassi']}')
        print(f'Proprietário : {veiculo['proprietario']}')
        print(f'Cor : {veiculo['cor']}')
        print(f'Quilometragem : {veiculo['quilometragem']}')
        print('-'*70)