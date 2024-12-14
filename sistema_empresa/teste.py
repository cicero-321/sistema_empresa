from funcionarios.banco_dados.repositorio import funcionarios
from funcionarios.regras.buscar import get_funcionario
from funcionarios.regras.cadastrar import add_funcionario
from funcionarios.regras.deletar import delete_funcionario
from funcionarios.regras.listar import listar_funcionario
from funcionarios.regras.editar import edit_funcionario

from veiculos.banco_dados.repositorio import veiculos
from veiculos.regras.buscar import get_veiculo
from veiculos.regras.cadastrar import add_veiculo
from veiculos.regras.listar import listar_veiculo
from veiculos.regras.deletar import delete_veiculo
from veiculos.regras.editar import edit_veiculo

add_veiculo('fan','XLR-8B10','1273863HAJAU1291832','JOAOZIN DO GRAU','preta',5923.3)
listar_veiculo()

print('-'*100)

edit_veiculo('XLR-8B10','CG','AAAAAA122222223AS','EMPRESA','branco',7000)
listar_veiculo()