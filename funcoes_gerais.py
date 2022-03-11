import interface
from time import sleep
from hospital import Hospital
from quarto import Quarto
from medico import Medico
from paciente import Paciente



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

def criar_quartos(hospital):
    quarto1 = Quarto(1, 'Livre')
    quarto2 = Quarto(2, 'Livre')
    quarto3 = Quarto(3, 'Livre')
    quarto4 = Quarto(4, 'Ocupado')

    hospital.add_quarto(quarto1)
    hospital.add_quarto(quarto2)
    hospital.add_quarto(quarto3)
    hospital.add_quarto(quarto4)

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
    medico = hospital.get_medico(interface.leiaInt('Código do Médico desejado: '))
    print(interface.linha())
    print('Buscando Quartos... ')
    sleep(1)
    hospital.ver_quartos()
    quarto = hospital.get_quarto(interface.leiaInt('Número do Quarto desejado: '))

    paciente = Paciente(id, nome, idade, sexo, cpf, rg, cep, email,
                    dataInternacao,telefone,nomeAcompanhante,telefoneAcompnhante,pagamento,medico, quarto)

    hospital.add_paciente(paciente)

    return paciente

def consultar_cadastro_paciente(lista_pacientes):
    paciente_cpf = interface.leiaString('Informe o CPF do paciente: ')
    for paciente in lista_pacientes:
        if paciente.get_cpf() == paciente_cpf:
            paciente.ver_dados()
            break
