class relatorio:
    def __init__(self) -> None:
        self.cabecalho=None
    
    def inicializacao(self):
        with open('..dados/cabecalho.tex')
            self.cabecalho = f.read()