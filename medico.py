from usuario import  Usuario

class Medico(Usuario):
    def __init__(self, id, nome, idade, sexo, cpf, rg, cep, crm, especialidade):
        super().__init__(id, nome, idade, sexo, cpf, rg, cep)
        self.crm = crm
        self.especialidade = especialidade

    def ver_medico(self):
        print (f'Nome: {self.nome} \n'
               f'Idade: {self.idade} \n'
               f'Sexo: {self.sexo} \n'
               f'CPF: {self.cpf} \n'
               f'RG: {self.rg} \n'
               f'CEP: {self.cep} \n'
               f'CRM: {self.crm} \n'
               f'Especialidade: {self.especialidade} \n')


