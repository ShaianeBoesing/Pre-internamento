class Usuario:
    def __init__(self, id, nome, idade, sexo, cpf, rg, cep, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.cep = cep
        self.email = email


    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_sexo(self):
        return self.sexo

    def get_cpf(self):
        return self.cpf

    def get_rg(self):
        return self.rg

    def get_cep(self):
        return self.cep
    
    def get_email(self):
        return self.email

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_rg(self, rg):
        self.rg = rg

    def set_cep(self, cep):
        self.cep = cep
    
    def set_cep(self, email):
        self.email = email