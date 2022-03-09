class Hospital:
    def __init__(self, nome, quartos=[], medicos=[], pacientes=[]):
        self.nome = nome
        self.quartos = quartos
        self.medicos = medicos
        self.pacientes = pacientes


    def ver_medicos(self):
        medicos = self.medicos
        if not medicos:
            print('Não há médicos cadastrados no sistema. Por favor, cadastre um médico. \n')
        else:
            for i in range(len(medicos)):
                print(f'MÉDICO {i+1}: ')
                medicos[i].ver_medico()

    def ver_quartos(self):
        quartos = self.quartos
        if not quartos:
            print('Não há quartos cadastrados no sistema. Por favor, cadastre um quarto. \n')
        else:
            for i in range(len(quartos)):
                print(f'Quarto {i}: {quartos[i]}')

    def add_medicos(self, medico):
        self.medicos.append(medico)

    def get_medicos(self):
        return self.medicos

    def get_quartos(self):
        return self.quartos

    def get_name(self):
        return self.nome

    def set_name(self, nome):
        self.nome = nome