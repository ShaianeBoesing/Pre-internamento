import interface
from time import sleep
from hospital import Hospital
from quarto import Quarto
from medico import Medico
from paciente import Paciente

medicos_disponiveis = []
quartos_existentes = []

def criar_hospital():
    hospital = Hospital()
    criar_medicos(hospital)
    criar_quartos(hospital)

    return hospital

def criar_medicos(hospital):
    id = 1
    medico1 = Medico(id, 'João', '45', 'M', '14785296312', '123456789', '99705488', 'joao@email.com',
                         '987654321', 'pediatria')
    id += 1
    medico2 = Medico(id, 'Paulo', '33', 'M', '98756423125', '856789654', '99705488', 'paulo@email.com',
                             '369852147', 'cardiologia')

    id += 1
    medico3 = Medico(id, 'Fernanda', '29', 'F', '753951486', '159789523', '99705488',
                             'fernanda@email.com', '321654987', 'ortopedia')
    id += 1
    hospital.add_medico(medico1)
    hospital.add_medico(medico2)
    hospital.add_medico(medico3)
    medicos_disponiveis.append(medico1.get_id())
    medicos_disponiveis.append(medico2.get_id())
    medicos_disponiveis.append(medico3.get_id())

def criar_quartos(hospital):
    quarto1 = Quarto(1, 'Livre')
    quarto2 = Quarto(2, 'Livre')
    quarto3 = Quarto(3, 'Livre')
    quarto4 = Quarto(4, 'Ocupado')

    hospital.add_quarto(quarto1)
    hospital.add_quarto(quarto2)
    hospital.add_quarto(quarto3)
    hospital.add_quarto(quarto4)
    quartos_existentes.append(quarto1.get_numero())
    medicos_disponiveis.append(quarto2.get_numero())
    medicos_disponiveis.append(quarto3.get_numero())
    medicos_disponiveis.append(quarto4.get_numero())

def cadastrar_paciente(hospital):
    nome = interface.leiaString('Nome: ')
    idade = interface.leiaInt('Idade: ')
    sexo = interface.leiaString('Sexo: ')
    cpf = interface.leiaString('CPF: ')
    rg = interface.leiaString('RG: ')
    cep = interface.leiaString('CEP: ')
    email = interface.leiaString('E-mail: ')
    dataInternacao = interface.leiaString('Data de Internação: ')
    telefone = interface.leiaString('Telefone: ')
    nomeAcompanhante = interface.leiaString('Nome do Acompanhante: ')
    telefoneAcompnhante = interface.leiaString('Telefone do Acompanhante: ')
    pagamento = interface.leiaString('Particular ou Convênio: ')
    print(interface.linha())

    print('Buscando Médicos... ')
    sleep(1)
    hospital.ver_medicos()
    codigoMedico = interface.leiaInt('Código do Médico desejado: ')
    while codigoMedico not in medicos_disponiveis:
        print('\033[31mERRO: Código de médico inválido!\033[m')
        codigoMedico = interface.leiaInt('Código do Médico desejado: ')

    medico = hospital.get_medico(codigoMedico)    
    print(interface.linha())
    
    print('Buscando Quartos... ')
    sleep(1)
    hospital.ver_quartos()

    for p in hospital.pacientes:
        if p.cpf == cpf:
            print('\033[31mERRO: Erro! Já existe um cadastro neste CPF. Certifique-se de que não deseja apenas alterar seus dados.\033[m')

    while True:
        numeroQuarto = interface.leiaInt('Número do Quarto desejado: ')
        if numeroQuarto not in quartos_existentes:
            print('\033[31mERRO: Número do quarto inválido!\033[m')
        else:
            quarto = hospital.get_quarto(numeroQuarto)
            while quarto.situacao != "Livre":
                print('\033[31mERRO: Quarto ocupado!\033[m')
            else:
                quarto.set_situacao("Ocupado")
                break

    paciente = Paciente(id, nome, idade, sexo, cpf, rg, cep, email,
                    dataInternacao,telefone,nomeAcompanhante,telefoneAcompnhante,pagamento,medico, quarto)
    hospital.add_paciente(paciente)
    quarto.set_paciente(paciente)

    print('\033[32mPré-Internamento realizado com sucesso! \033[m')
    return paciente

def buscar_paciente(lista_pacientes):
    paciente_cpf = interface.leiaString('Informe o CPF do paciente: ')
    for paciente in lista_pacientes:
        if paciente.get_cpf() == paciente_cpf:
            return paciente
    else:
        print('Nenhum registro encontrado neste CPF')
        return False

def consultar_cadastro_paciente(paciente):
    paciente.ver_dados()
    sleep(1)

def atualizar_cadastro_paciente(hospital, paciente):
    while True:
        opcao = interface.menu (['Dados Pessoais', 'Dados de Acompanhante', 'Informações de Contato', 'Dados da Internação', 'Sair'], 'O QUE DESEJA ALTERAR?')
        if opcao==5:
            interface.cabecalho('Voltando ao menu inicial...')
            break
        if opcao==1:
            nome = interface.leiaString('Nome: ')
            idade = interface.leiaInt('Idade: ')
            sexo = interface.leiaString('Sexo: ')

            paciente.set_nome(nome)
            paciente.set_idade(idade)
            paciente.set_sexo(sexo)
            print(len(hospital.pacientes))
        elif opcao==2:
            nomeAcompanhante = interface.leiaString('Nome do Acompanhante: ')
            telefoneAcompnhante = interface.leiaString('Telefone do Acompanhante: ')

            paciente.set_nomeAcompanhante(nomeAcompanhante)
            paciente.set_telefoneAcompnhante(telefoneAcompnhante)
        elif opcao==3:
            cep = interface.leiaString('CEP: ')
            telefone = interface.leiaString('Telefone: ')
            email = interface.leiaString('E-mail: ')

            paciente.set_cep(cep)
            paciente.set_telefone(telefone)
            paciente.set_email(email)
        elif opcao==4:
            dataInternacao = interface.leiaString('Data de Internação: ')
            pagamento = interface.leiaString('Particular ou Convênio: ')
            print(interface.linha())
            print('Buscando Médicos... ')
            sleep(1)
            hospital.ver_medicos()
            medico = hospital.get_medico(interface.leiaInt('Código do Médico desejado: '))
            print(interface.linha())
            print('Buscando Quartos... ')
            sleep(1)
            hospital.ver_quartos()
            quarto = hospital.get_quarto(interface.leiaInt('Número do Quarto desejado: '))

            paciente.set_dataInternacao(dataInternacao)
            paciente.set_pagamento(pagamento)
            paciente.set_medico(medico)
            paciente.set_quarto(quarto)

        sleep(1)

def excluir_cadastro_paciente(hospital, paciente):
    while True:
        opcao = interface.menu (['Sim', 'Não'], 'Deseja mesmo excluir o cadastro do paciente?')
        sleep(1)
        if opcao==1:
            pacientes = hospital.pacientes
            cpf = paciente.cpf
            for i, p in enumerate(pacientes):
                if cpf == p.get_cpf():
                    pacientes.pop(i)
                    print("Exclusão efetuada com sucesso!")
            interface.cabecalho('Voltando ao menu inicial...')
            break  
        if opcao==2:
            interface.cabecalho('Voltando ao menu inicial...')
            break            
        sleep(1)
