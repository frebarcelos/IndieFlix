import json
from datetime import datetime
from funcutils import retorno_data_DDMMYYYY,retorno_data_YYYYMMDD
import re


class Filme:
    caminho_bd = 'filmes.json'
    lista = []
    id = 0
    def __init__(self,titulo, diretor, data_lancamento,genero,duracao,nota_pessoal, id=None):
        self.id = id if id != None else Filme.id
        self.titulo = titulo
        self.diretor = diretor
        self.data_lancamento = data_lancamento
        self.genero = genero
        self.duracao = duracao
        self.nota_pessoal = nota_pessoal
        Filme.id = id + 1 if id != None else Filme.id + 1                  

    @classmethod
    def find_by_id(cls,id):
        for filme in cls.lista:
            if filme.id == id:
                return filme
    @classmethod
    def find_all_by_attributes(cls,atributos: dict):
        resultados = []
        for filme in cls.lista:
            if all(
            str(valor).strip().lower() in str(getattr(filme, chave, "")).strip().lower()
            for chave, valor in atributos.items()
            ):
                resultados.append(filme)
        return resultados
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'diretor': self.diretor,
            'data_lancamento': self.data_lancamento,
            'genero': self.genero,
            'duracao': self.duracao,
            'nota_pessoal': self.nota_pessoal
        }
    @classmethod
    def salvar(cls, filme_salvar=None):
        if(filme_salvar != None):
            cls.lista.append(filme_salvar)
        cls.ajuste_data_salvar_banco()
        cls.ordenar_lista()
        filmes_dict = [filme.to_dict() for filme in cls.lista]
        with open(cls.caminho_bd, 'w', encoding='utf-8') as f:
            json.dump(filmes_dict, f, ensure_ascii=False, indent=2)
        cls.ajusta_data_banco()                           
    @classmethod
    def carregar(cls):
        with open(cls.caminho_bd, 'r', encoding='utf-8') as lista:
            lista_filmes = json.load(lista)
            if len(lista_filmes) > 0:
                lista_filmes.sort(key=lambda f: f['id'])
                for filme in lista_filmes:
                    novo_filme = Filme(id=filme['id'],titulo=filme['titulo'],diretor=filme['diretor'],data_lancamento=filme['data_lancamento'],genero=filme['genero'],duracao=filme['duracao'],nota_pessoal=filme['nota_pessoal'])
                    Filme.lista.append(novo_filme) 
            cls.ajusta_data_banco()
    @classmethod
    def ajusta_data_banco(cls):
        for filme in cls.lista:
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", filme.data_lancamento):
                filme.data_lancamento = retorno_data_DDMMYYYY(filme.data_lancamento)   
   
    @classmethod
    def ajuste_data_salvar_banco (cls):
        for filme in cls.lista:
            if re.fullmatch(r"\d{2}/\d{2}/\d{4}", filme.data_lancamento):
                filme.data_lancamento = retorno_data_YYYYMMDD(filme.data_lancamento)
     
    @classmethod       
    def ordenar_lista(cls, opcao = 0):
        opcoes = {
            0: {
                "key": lambda f: f.id,
                "reverse": False,
                "descricao": ""
            },
            1: {
                "key": lambda f: f.titulo,
                "reverse": False,
                "descricao": "por Título (A - Z)"
            },
            2: {
                "key": lambda f: f.titulo,
                "reverse": True,
                "descricao": "por Título (Z - A)"
            },
            3: {
                "key": lambda f: f.diretor,
                "reverse": False,
                "descricao": "por Diretor"
            },
            4: {
                "key": lambda f: datetime.strptime(f.data_lancamento, "%d/%m/%Y"),
                "reverse": False,
                "descricao": "pelos mais antigos"
            },
            5: {
                "key": lambda f: datetime.strptime(f.data_lancamento, "%d/%m/%Y"),
                "reverse": True,
                "descricao": "pelos mais novos"
            },
            6: {
                "key": lambda f: f.duracao,
                "reverse": False,
                "descricao": "pelos mais curtos"
            },
            7: {
                "key": lambda f: f.duracao,
                "reverse": True,
                "descricao": "pelos mais longos"
            },
            8: {
                "key": lambda f: f.nota_pessoal,
                "reverse": False,
                "descricao": "pelos que você menos gostou"
            },
            9: {
                "key": lambda f: f.nota_pessoal,
                "reverse": True,
                "descricao": "pelos que você gostou mais"
            }
        }

        conf = opcoes[opcao]
        cls.lista.sort(key=conf["key"], reverse=conf["reverse"])
        return conf["descricao"]  
    @classmethod
    def excluir_filme(cls,id_filme_excluido):
        cls.list = [filme for filme in cls.lista if filme.id != id_filme_excluido]
        cls.salvar()
    @classmethod
    def editar_filme(cls,filme_editar):
        cls.excluir_filme(filme_editar.id)
        cls.salvar(filme_editar)    
    
    @classmethod
    def busca_simples(cls,termo_busca):
        termo = termo_busca.strip().lower()
        resultados = []

        for filme in cls.lista:
            if any(
                termo in str(getattr(filme, campo, "")).lower()
                for campo in ["titulo", "diretor", "genero"]
            ):
                resultados.append(filme)
        
        return resultados