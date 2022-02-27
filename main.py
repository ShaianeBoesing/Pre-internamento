from hospital import Hospital
from usuario import Usuario
from medico import Medico

# Creating 'my_hospital' object from Hospital: required and unique
while True:
    nome_hospital = input('Informe o nome do hospital: ').strip()
    if nome_hospital:
        my_hospital = Hospital(nome_hospital)
        break
    else:
        print('Nome inválido! \n')

# Select first Menu option
valid_menu_option = False
menu_option = None
while not valid_menu_option:
    try:
        menu_option = int(input(' 1- ADMINISTRATIVO \n 2- PACIENTE \n_:'))

        if menu_option in [1, 2]:
            valid_menu_option = True
        else:
            print('Valor Inválido \n')

    except:
        print('Valor Inválido \n')

# Verifying selected Menu Option
usuario_id = 1

if menu_option == 1:
    adm_continuar = True
    while adm_continuar:
        valid_adm_menu_option = False
        adm_menu_option = None
        while not valid_adm_menu_option:
            try:
                adm_menu_option = int(input('1- Cadastrar médico \n'+
                                            '2- Cadastrar quarto \n' +
                                            '3- Ver médicos \n' +
                                            '4- Ver quartos \n' +
                                            '5- Excluir médicos \n' +
                                            '6- Excluir quarto \n' +
                                            '7- Alterar médico \n' +
                                            '8- Alterar nome do hospital \n'+
                                            '9- Ver nome do hospital \n'
                                            '_:'))

                if adm_menu_option in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    valid_adm_menu_option = True
                else:
                    print('Valor Inválido \n')

            except:
                print('Valor Inválido \n')

    if adm_menu_option == 1:
        print('opção 1')
    elif adm_menu_option == 2:
        print('opção 2')
    elif adm_menu_option == 3:
        print('opção 3')
    elif adm_menu_option == 4:
        print('opção 4')
    elif adm_menu_option == 5:
        print('opção 5')
    elif adm_menu_option == 6:
        print('opção 6')
    elif adm_menu_option == 7:
        print('opção 7')
    else:
        print('opção 8')


elif menu_option == 2:
    valid_paciente_menu_option = False
    paciente_menu_option = None
    paciente_continuar = True
    while paciente_continuar:
        while not valid_paciente_menu_option:
            try:
                paciente_menu_option = int(input('1- Realizar pré-internação \n'+
                                                 '2- Ver meu pré check-in \n'+
                                                 '2- Cancelar internação \n' +
                                                 '2- Concluir internação \n' +
                                                 '2- Ver médicos disponíveis \n' +
                                                 '2- Ver quartos disponíveis \n'))


                if paciente_menu_option in [1, 2, 3, 4, 5, 6]:
                    valid_paciente_menu_option = True
                else:
                    print('Valor Inválido \n')

            except:
                print('Valor Inválido \n')

        if paciente_menu_option == 1:
            print('opção 1')
        elif paciente_menu_option == 2:
            print('opção 2')
        elif paciente_menu_option == 3:
            print('opção 3')
        elif paciente_menu_option == 4:
            print('opção 4')
        elif paciente_menu_option == 5:
            print('opção 5')
        else:
            print('opção 6')
