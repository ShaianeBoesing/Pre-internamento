from usuario import Usuario

class Paciente (Usuario):
    def __init__(self, id, nome, idade, sexo, cpf, rg, cep, email,
                 dataInternacao,telefone,nomeAcompanhante,telefoneAcompnhante,pagamento, medico, quarto):
        
        self.dataInternacao=dataInternacao
        self.telefone=telefone
        self.nomeAcompanhante=nomeAcompanhante
        self.telefoneAcompnhante=telefoneAcompnhante
        self.pagamento=pagamento
        
        super().__init__(id, nome, idade, sexo, cpf, rg, cep, email)
        
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