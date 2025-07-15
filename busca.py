from view.animacao import centralizar,limpar_terminal, input_centralizado,falar_ascii
from funcutils import valida_opcoes, input_data_valida, input_genero_valido
from catalogo import imprimir_tabela
from filmes import Filme

attribute_labels = {
    "titulo": "Título",
    "diretor": "Diretor(a)",
    "data_lancamento": "Data de Lançamento",
    "genero": "Gênero",
    "nota": "Nota Pessoal",
    "duracao": "Duração (min)"
}
def buscar_filme():
    while True:
        limpar_terminal()
        resposta = valida_opcoes(opcoes=['0','1','2'], mensagem="[0] Voltar [1] Busca Simples [2] Busca Avançada",falar="Vamos encontrarar um filme então, qual busca você gostaria de fazer ?")
        if resposta == 0:
            break
        if resposta == 1:
            busca_simples()
        if resposta == 2:
            busca_avancada()
        

def busca_simples():
    falar_ascii("Vamos fazer então uma busca simples, digite o que deseja buscar")
    busca = input_centralizado()
    encontrados = Filme.busca_simples(busca)
    resultado_escontrado(encontrados)

def busca_avancada():
    filtros = {}
    while True:
        pesquisando = ''
        if filtros:
            pesquisando = "\nPesquisando por:"
            for chave, valor in filtros.items():
                nome = attribute_labels.get(chave, chave.capitalize())
                pesquisando += '\n- ' + nome + ': ' + valor  
        resposta = valida_opcoes(opcoes=['0','1','2','3','4','5'], mensagem="[0] Voltar [1] Título [2] Diretor [3] Data de lançamento [4] Gênero [5] Pesquisar",falar="Por qual atributo você  gostaria de pesquisar (pode adicionar mais de um) ?" + pesquisando)
            
        if resposta == 0: 
            break
        if resposta == 1:        
            informa_pesquisa("o Título")
            filtros['titulo'] = input_centralizado("").strip().lower()
        if resposta == 2:
            informa_pesquisa("o nome do Diretor(a)")
            filtros['diretor'] = input_centralizado("").strip().lower()
        if resposta == 3:
            informa_pesquisa("a Data de lançamento")
            filtros['data_lancamento'] = input_data_valida()
        if resposta == 4:
            informa_pesquisa("o Gênero")
            filtros['genero'] = input_genero_valido()
        if resposta == 5:    
            encontrados = Filme.find_all_by_attributes(filtros)
            resultado_escontrado(encontrados)
            break            
            

def informa_pesquisa(texto_pesquisa):
    falar_ascii(f"Digite {texto_pesquisa} que deseja pesquisar")

def resultado_escontrado(resultado):
    if resultado:
                falar_ascii("Estes foram os filmes que encontrei")
                imprimir_tabela(resultado)
                input_centralizado("")
    else:
        falar_ascii("Infelizmente não encontrei nenhum filme com sua pesquisa!") 
        input_centralizado("")
            