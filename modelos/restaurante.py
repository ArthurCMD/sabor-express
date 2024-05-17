from modelos.avaliacao import Avaliacao

class Restaurante:
        restaurantes = []

        def __init__(self, nome, categoria):
            self._nome = nome.title()
            self._categoria = categoria
            self._ativo = False
            self._avaliacao = []
            Restaurante.restaurantes.append(self)
        
        def __str__(self):
            return f' {self._nome} | {self._categoria} '
        
        @classmethod 
        def listar_restaurantes(cls):
            print(f"{'Nome Restaurante'.ljust(25)} | {'Categoria Restaurante'.ljust(25)} | {'Status'.ljust(5)}")
            for restaurante in cls.restaurantes:
                print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(5)}')

        @property
        def ativo(self):
            return '☑' if self._ativo else '☐'
        
        def alternar_estado(self):
            self._ativo = not self._ativo


restaurante_oshiro = Restaurante('Oshiro Sushi','Sushi')
restaurante_oshiro.alternar_estado()
restaurante_dory = Restaurante('Dory Sushi','Sushi Gourmet')

Restaurante.listar_restaurantes()



