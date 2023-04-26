class relatorio:
    def __init__(self, autor, titulo, template='cabeçalho.tex') -> None:
        self.template = template
        self.autor = autor
        self.titulo = titulo
        self.cabecalho = None
        self.inicializa()
    
    def inicializa(self):
        with open(os.path.join(self.template_dir,'..dados/cabecalho.tex')) as f:
            self.cabecalho = f.read()