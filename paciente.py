from usuario import Usuario

class Paciente (Usuario):
    def __init__(self, id, nome, idade, sexo, cpf, rg, cep, email, dataInternacao, dataNascimento,alergia,nacionalidade,naturalidade,nomePai,nomeMae,endereco,numEndereco,complemento,bairro,cidade,estado,pais,telefone,nomeAcompanhante,telefoneAcompnhante,estadocivil,religiao,profissao,empresa,pagamento):
        
        self.dataInternacao=dataInternacao
        self.dataNascimento=dataNascimento
        self.alergia=alergia
        self.nacionalidade=nacionalidade
        self.naturalidade=naturalidade
        self.nomePai=nomePai
        self.nomeMae=nomeMae
        self.endereco=endereco
        self.numEndereco=numEndereco
        self.complemento=complemento
        self.bairro=bairro
        self.cidade=cidade
        self.estado=estado
        self.pais=pais
        self.telefone=telefone
        self.nomeAcompanhante=nomeAcompanhante
        self.telefoneAcompnhante=telefoneAcompnhante
        self.estadocivil=estadocivil
        self.religiao=religiao
        self.profissao=profissao
        self.empresa=empresa
        self.pagamento=pagamento
        
        super().__init__(id, nome, idade, sexo, cpf, rg, cep, email)
        
        def get_dataInternacao(self):
            return self.dataInternacao
        
        def get_dataNascimento(self):
            return self.dataNascimento
        
        def get_alergia(self):
            return self.alergia
        
        def get_nacionalidade(self):
            return self.nacionalidade
        
        def get_naturalidade(self):
            return self.naturalidade
        
        def get_nomePai(self):
            return self.nomePai
        
        def get_nomeMae(self):
            return self.nomeMae
        
        def get_endereco(self):
            return self.endereco
        
        def get_numEndereco(self):
            return self.numEndereco
        
        def get_complemento(self):
            return self.complemento
        
        def get_bairro(self):
            return self.bairro
        
        def get_cidade(self):
            return self.cidade
    
        def get_cidade(self):
            return self.cidade
        
        def get_pais(self):
            return self.pais
        
        def get_telefone(self):
            return self.telefone
        
        def get_nomeAcompanhante(self):
            return self.nomeAcompanhante
        
        def get_telefoneAcompnhante(self):
            return self.telefoneAcompnhante
        
        def get_estadocivil(self):
            return self.estadocivil
        
        def get_estadocivil(self):
            return self.estadocivil
        
        def get_profissao(self):
            return self.profissao
        
        def get_empresa(self):
            return self.empresa
        
        def get_pagamento(self):
            return self.pagamento
        
        
        def set_dataInternacao(self, dataInternacao):
            self.dataInternacao = dataInternacao
        
        def set_dataNascimento(self, dataNascimento):
            self.dataNascimento = dataNascimento
        
        def set_alergia(self, alergia):
            self.alergia = alergia
            
        def set_nacionalidade(self, nacionalidade):
            self.nacionalidadee = nacionalidade
        
        def set_naturalidade(self, naturalidade):
            self.naturalidade = naturalidade
        
        def set_nomePai(self, nomePai):
            self.nomePai = nomePai
            
        def set_nomeMae(self, nomeMae):
            self.nomeMae = nomeMae
        
        def set_endereco(self, endereco):
            self.endereco = endereco
        
        def set_numEndereco(self,numEndereco):
            self.numEndereco = numEndereco
            
        def set_complemento(self, complemento):
            self.complemento = complemento
        
        def set_bairro(self, bairro):
            self.bairro = bairro
            
        def set_cidade(self,cidade):
            self.cidade = cidade
        
        def set_estado(self,estado):
            self.estado = estado
        
        def set_pais(self,pais):
            self.pais = pais
        
        def set_telefone(self, telefone):
            self.telefone = telefone
            
        def set_nomeAcompanhante(self, nomeAcompanhante):
            self.nomeAcompanhante = nomeAcompanhante
        
        def set_telefoneAcompnhante(self, telefoneAcompnhante):
            self.telefoneAcompnhante = telefoneAcompnhante
        
        def set_estadocivil(self, estadocivil):
            self.estadocivil = estadocivil
            
        def set_religiao(self, religiao):
            self.religiao = religiao
            
        def set_profissao(self, profissao):
            self.profissao = profissao
            
        def set_empresa(self, empresa):
            self.empresa = empresa
            
        def set_pagamento(self, pagamento):
            self.pagamento = pagamento