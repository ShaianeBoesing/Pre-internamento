from medico import Medico
class Hospital:
    def __init__(self, quartos=[], medicos=[], pacientes=[]):
        self.quartos = quartos
        self.medicos = medicos
        self.pacientes = pacientes


    def ver_medicos(self):
        medicos = self.medicos
        if not medicos:
            print('Não há médicos cadastrados no sistema. Por favor, cadastre um médico. \n')
        else:
            for i in range(0, len(medicos), 1):
                medicos[i].ver_dados()


    def ver_quartos(self):
        quartos = self.quartos
        if not quartos:
            print('Não há quartos cadastrados no sistema. Por favor, cadastre um quarto. \n')
        else:
            for i in range(0, len(quartos), 1):
                quartos[i].ver_dados()


    def add_medico(self, medico):
        self.medicos.append(medico)

    def add_quarto(self, medico):
        self.quartos.append(medico)

    def add_paciente(self, paciente):
        self.pacientes.append(paciente)

    def get_medicos(self):
        return self.medicos

    def get_quartos(self):
        return self.medicos

    def get_medico(self, id):
        for medico in self.medicos:
            if medico.get_id() == id:
                return medico;

    def get_quarto(self, numero):
        for quarto in self.quartos:
            if quarto.get_numero() == numero:
                return quarto;

