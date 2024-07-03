class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__ativo = ativo
        
    def desativar(self):
        self.__ativo = False
        print("A pessoa foi desativada com sucesso")
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456", False)
    pessoa1.desativar()
    pessoa1.ativo = True
    
    print(pessoa1.ativo)
    
	# Utilizando geters e setters
    pessoa1.set_nome("José")
    print(pessoa1.get_nome())

    # Utilizando properties
    pessoa1.nome = "José"
    print(pessoa1.nome)
    
    pessoa2 = Pessoa("Roger", "F", "34987498", True )
    
    print(pessoa2.get_nome())       
