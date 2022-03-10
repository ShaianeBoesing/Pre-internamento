from usuario import  Usuario

class Medico(Usuario):
    def __init__(self, id, nome, idade, sexo, cpf, rg, cep, email, crm, especialidade):
        super().__init__(id, nome, idade, sexo, cpf, rg, cep, email)
        self.crm = crm
        self.especialidade = especialidade

    def ver_medico(self):
        print (f'MÉDICO {self.id} \n'
               f'Nome: {self.nome} \n'
               f'Especialidade: {self.especialidade} \n')


