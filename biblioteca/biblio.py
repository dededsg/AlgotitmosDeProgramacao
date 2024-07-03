class Biblioteca:
    def __init__(self, titulo, codigo, autor, classe, num_pag):
        self.titulo = titulo
        self.codigo = codigo
        self.autor = autor
        self.classe = classe
        self.num_pag = num_pag
  
if __name__ == "__main__":
    livro = Biblioteca("Cosmos", 1562793, "Carl Segan", "Ciencias", 209)
    
    print(livro.titulo)
