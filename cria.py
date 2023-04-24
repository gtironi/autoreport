class relatorio:
    def __init__(self, autor, titulo) -> None:
        self.autor = autor
        self.titulo = titulo
        self.cabecalho = None
    
    def inicializacao(self):
        with open('..dados/cabecalho.tex') as f:
            self.cabecalho = f.read()