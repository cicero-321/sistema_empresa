from veiculos.banco_dados.repositorio import veiculos

def get_veiculo(placa: int) -> dict | None:
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            return veiculo
    print('Veículo não encontrado !')
    return None