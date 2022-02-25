valid_menu_option = False
menu_option = None
while not valid_menu_option:
    try:
        menu_option = int(input('''
1- ADMINISTRATIVO
2- PACIENTE
_:'''))
        if menu_option in [1, 2]:
            valid_menu_option = True
        else:
            print('Valor Inválido \n')

    except:
        print('Valor Inválido \n')

if menu_option == 1:
    valid_adm_menu_option = False
    adm_menu_option = None
    while not valid_adm_menu_option:
        try:
            adm_menu_option = int(input('''
1- Cadastrar hospital
2- Cadastrar médico
3- Cadastrar quarto 
4- Ver médicos
5- Ver quartos
6- Excluir médicos
7- Excluir quarto
8- Alterar médico
_:'''))
            if adm_menu_option in [1, 2, 3, 4, 5, 6, 7, 8]:
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
    while not valid_paciente_menu_option:
        try:
            paciente_menu_option = int(input('''
1- Realizar pré-internação
2- Ver meu pré check-in
3- Cancelar internação
4- Concluir internação
5- Ver médicos disponíveis
6- Ver quartos disponíveis
_:'''))
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
