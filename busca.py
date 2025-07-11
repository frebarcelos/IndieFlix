from view.animacao import centralizar,limpar_terminal, input_centralizado,falar_ascii
from funcutils import valida_opcoes
from catalogo import abrir_arquivo_leitura_filmes,imprimir_tabela

def buscar_filme():
    limpar_terminal()
    resposta = valida_opcoes(opcoes=['0','1','2'], mensagem="[0] Voltar [1] Busca Simples [2] Busca Avançada",falar="Vamos encontrarar um filme então, qual busca você gostaria de fazer ?")
    if resposta == 0:
        return
    if resposta == 1:
        busca_simples()
    if resposta == 2:
        busca_avancada()
        

def busca_simples():
    print(centralizar("Busca Simples"))
    input_centralizado()
    return

def busca_avancada():
    lista_filmes = abrir_arquivo_leitura_filmes(exibir_filmes=False)
    resposta = valida_opcoes(opcoes=['0','1','2'], mensagem="[0] Voltar [1] Título [2] Diretor",falar="Por qual atibuto você voê gostaria de pesquisar ?")
    elemento_busca = ''
    if resposta == 0:
        return
    if resposta == 1:
        elemento_busca = 'titulo'
        pesquisa = "o Título"
    if resposta == 2:
        elemento_busca = 'diretor'
        pesquisa = "o nome do Diretor(a)"
          
    falar_ascii(f"Digite {pesquisa} que deseja pesquisar")
    busca = input_centralizado("").strip().lower()
    encontrados = [f for f in lista_filmes if busca in f[elemento_busca].lower()]
    if encontrados:
        falar_ascii("Estes foram os filmes que encontrei")
        imprimir_tabela(encontrados)
        input_centralizado("")
    else:
        falar_ascii("Infelizmente não encontrei nenhum filme com sua pesquisaa!") 
        input_centralizado("")
    