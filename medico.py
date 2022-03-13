from usuario import  Usuario

class Medico(Usuario):
    def __init__(self, id, nome, idade, sexo, cpf, rg, cep, email, crm, especialidade):
        super().__init__(id, nome, idade, sexo, cpf, rg, cep, email)
        self.crm = crm
        self.especialidade = especialidade

    def ver_dados(self):
        print (f'MÉDICO {self.id} \n'
               f'Nome: {self.nome} \n'
               f'Especialidade: {self.especialidade} \n')

    def get_crm(self):
        return self.crm

    def get_especialidade(self):
        return self.especialidade

    def set_crm(self, crm):
        self.crm = crm

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade