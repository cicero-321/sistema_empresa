from veiculos.banco_dados.repositorio import veiculos

def add_veiculo(modelo: str,placa: str,chassi: str,proprietario: str,cor: str,km: float):
    novo_veiculo = {
        'modelo' : modelo,
        'placa' : placa,
        'chassi': chassi,
        'proprietario': proprietario,
        'cor' : cor,
        'quilometragem' : km
    }

    veiculos.append(novo_veiculo)
    print('Veiculo cadastrado com sucesso! ')