from veiculos.banco_dados.repositorio import veiculos
from veiculos.regras.buscar import get_veiculo

def delete_veiculo(placa: str) -> dict | None:
    placa = get_veiculo(placa)
    if placa:
        veiculos.remove(placa)
        print('Veículo removido !')
        return None
    print('Veículo não encontrado !')
    return None