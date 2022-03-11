import interface
from funcoes_gerais import criar_hospital
from funcoes_gerais import cadastrar_paciente
from funcoes_gerais import consultar_cadastro_paciente

hospital = criar_hospital()

paciente = None
while True:
    resposta = interface.menu (['Cadastrar Paciente', 'Alterar Cadastro', 'Consultar Cadastro', 'Excluir Cadastro', 'Sair' ])
    if resposta==1:
        interface.cabecalho('Cadastrar Paciente')
        paciente = cadastrar_paciente(hospital)
    elif resposta==2:
        interface.cabecalho('Alterar Cadastro')
    elif resposta==3:
        interface.cabecalho ('Consultar Cadastro')
        consultar_cadastro_paciente(paciente)
    elif resposta==4:
        interface.cabecalho('Excluir Cadastro')
    elif resposta==5:
        interface.cabecalho('Saindo do Sistema...')
        break
    else:
        print('\033[31mErro: Digite uma opção válida!\033[m')
