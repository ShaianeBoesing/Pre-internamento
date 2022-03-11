from paciente import Paciente

class Quarto:
    def __init__(self, numero, situacao):
        self.numero = numero
        self.situacao = situacao
        self.paciente = None

    def ver_dados(self):
        if self.situacao == 'Livre':
            print (f'QUARTO {self.numero}')

    def get_numero(self):
        return self.numero

    def get_situacao(self):
        return self.situacao

    def get_paciente(self):
        return self.paciente

    def set_situacao(self, situacao):
        self.situacao = situacao

    def set_paciente(self, paciente):
        self.paciente = paciente



