import interface 
from time import sleep

while True:
    resposta= interface.menu (['Cadastrar Paciente', 'Alterar Cadastro', 'Consultar Cadastro', 'Excluir Cadastro', 'Sair' ])
    if resposta==1:
        interface.cabecalho('Cadastrar Paciente')
    elif resposta==2:
        interface.cabecalho('Alterar Cadastro')
    elif resposta==3:
        interface.cabecalho ('Consultar Cadastro')
    elif resposta==4:
        interface.cabecalho('Excluir Cadastro')
    elif resposta==5:
        interface.cabecalho('Saindo do Sistema...')
        break
    else:
        print('\033[31mErro: Digite uma opção válida!\033[m')
    sleep(2) 