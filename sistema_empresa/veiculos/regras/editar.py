from veiculos.banco_dados.repositorio import veiculos
from veiculos.regras.buscar import get_veiculo

def edit_veiculo(placa: str,modelo: str,chassi: str,proprietario: str,cor: str,quilometragem: float):
    veiculo = get_veiculo(placa)
    if veiculo:
        veiculo['modelo'] = modelo
        veiculo['chassi'] = chassi
        veiculo['proprietario'] = proprietario
        veiculo['cor'] = cor
        veiculo['quilometragem'] = quilometragem
        print('Veículo editado com sucesso !')
        return None
    print('Veículo não encontrado !')
    return None