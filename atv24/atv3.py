'''
3. Crie uma agenda de contatos, ou seja, um registro chamado Contato, contendo nome e telefone. Crie um
algoritmo que permite cadastrar, remover e buscar contatos. A busca deve ser baseada no nome da pessoa. Para
implementar essa coleção de registros, utilize um vetor de 50 posições (capacidade máxima de contatos). Questão
a se perguntar antes de implementar: Como saber se determinado contato do vetor está livre pra receber um novo
contato?
'''
ordem = True

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

agenda = [None] * 50

def cadastrar_contato(nome, telefone):
    for i in range(len(agenda)):
        if agenda[i] is None:
            agenda[i] = Contato(nome, telefone)
            print(f"Contato '{nome}' cadastrado com sucesso!")
            return
    print("A agenda está cheia! Não é possível adicionar novos contatos.")
    ordem = True
    return ordem

def remover_contato(nome):
    for i in range(len(agenda)):
        if agenda[i] is not None and agenda[i].nome == nome:
            agenda[i] = None
            print(f"Contato '{nome}' removido com sucesso!")
            return
    print(f"Contato '{nome}' não encontrado na agenda.")
    ordem = True
    return ordem

def buscar_contato(nome):
    for i in range(len(agenda)):
        if agenda[i] is not None and agenda[i].nome == nome:
            print(f"Contato encontrado: Nome: {agenda[i].nome}, Telefone: {agenda[i].telefone}")
            return
    print(f"Contato '{nome}' não encontrado na agenda.")
    ordem = True
    return ordem



while ordem == True:
    print("Digite a operação que deseja ultilizar:")
    print("Digite [1] para cadastrar")
    print("Digite [2] para buscar")
    print("Digite [3] para excluir")
    print("Digite [4] para sair")
    disc = int(input("Digite a operação: "))
    
    if disc == 1:
        print("++++++++ CADASTRAR CONTATO ++++++++")
        nome, telefone = input("Digite o nome: "), int(input("Digite o telefone: "))
        print(cadastrar_contato(nome, telefone))
        
    elif disc == 2:
        print("++++++++ BUSCAR CONTATO ++++++++")
        nome = input("Digite o nome: ")
        print(buscar_contato(nome))
        
    elif disc == 3:
        print("++++++++ EXCLUIR CONTATO ++++++++")
        print(remover_contato(input("Digite o nome do contao a excluir: ")))
        
    elif disc == 4:
        print("++++++++ SAIR ++++++++")
        ordem = False
    else:
        print("Operação inválida")


