from jinja2 import Environment, PackageLoader
import os

class relatorio:
    template_dir = "dados" #os.pat.join("..", "/dados")
    def __init__(self, autor, titulo, template='cabeçalho.tex') -> None:
        env = Environment(loader=PackageLoader("relatorio"))
        self.template_file = os.path.join(self.template_dir, template)
        self.template = env.get_template(self.template_file)
        self.autor = autor
        self.titulo = titulo
        self.cabecalho = None
        #self.inicializa()
    
    def inicializa(self):
        with open(os.path.join(self.template_dir,'..dados/cabecalho.tex')) as f:
            self.cabecalho = f.read()