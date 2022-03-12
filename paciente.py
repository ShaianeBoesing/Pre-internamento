from usuario import Usuario
import interface

class Paciente(Usuario):
    def __init__(self, id, nome, idade, sexo, cpf, rg, cep, email,
                 dataInternacao, telefone, nomeAcompanhante, telefoneAcompnhante, pagamento, medico, quarto):
        self.dataInternacao = dataInternacao
        self.telefone = telefone
        self.nomeAcompanhante = nomeAcompanhante
        self.telefoneAcompnhante = telefoneAcompnhante
        self.pagamento = pagamento
        self.medico = medico
        self.quarto = quarto
        super().__init__(id, nome, idade, sexo, cpf, rg, cep, email)

    def ver_dados(self):
        print(f'Nome: {self.nome} \n'
              f'Idade: {self.idade} \n'
              f'Sexo: {self.sexo} \n'
              f'CPF: {self.cpf} \n'
              f'RG: {self.rg} \n'
              f'CEP: {self.cep} \n'
              f'E-mail: {self.email} \n'
              f'Internação: {self.dataInternacao} \n'
              f'Telefone: {self.telefone} \n'
              f'Acompanhante: {self.nomeAcompanhante} \n'
              f'Telefone AC: {self.telefoneAcompnhante} \n'
              f'Pagamento: {self.pagamento}')

        print(interface.linha())
        self.medico.ver_dados()
        self.quarto.ver_dados()

    def get_dataInternacao(self):
        return self.dataInternacao

    def get_telefone(self):
        return self.telefone

    def get_nomeAcompanhante(self):
        return self.nomeAcompanhante

    def get_telefoneAcompnhante(self):
        return self.telefoneAcompnhante

    def get_pagamento(self):
        return self.pagamento

    def get_medico(self):
        return self.medico

    def get_quarto(self):
        return self.quarto

    def set_dataInternacao(self, dataInternacao):
        self.dataInternacao = dataInternacao

    def set_telefone(self, telefone):
        self.telefone = telefone

    def set_nomeAcompanhante(self, nomeAcompanhante):
        self.nomeAcompanhante = nomeAcompanhante

    def set_telefoneAcompnhante(self, telefoneAcompnhante):
        self.telefoneAcompnhante = telefoneAcompnhante

    def set_pagamento(self, pagamento):
        self.pagamento = pagamento

    def set_medico(self, medico):
        self.medico = medico

    def set_quarto(self, quarto):
        self.quarto = quarto
