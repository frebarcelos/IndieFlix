import json
from animacao import centralizar, limpar_terminal,input_centralizado

caminho_arquivo = 'filmes.json'

def abrir_arquivo_leitura():
    with open(caminho_arquivo, 'r', encoding='utf-8') as lista_filmes:
            return json.load(lista_filmes)


def imprimir_tabela():

    lista = abrir_arquivo_leitura()
    
    # Pega os nomes das colunas (chaves do primeiro item)
    colunas = list(lista[0].keys())

    # Descobre a largura maxima de cada coluna
    larguras = {coluna: len(coluna) for coluna in colunas}
    for item in lista:
        for coluna in colunas:
            larguras[coluna] = max(larguras[coluna], len(str(item.get(coluna, ""))))

    # Monta linha de separação
    def linha_horizontal():
        return "+" + "+".join("-" * (larguras[col] + 2) for col in colunas) + "+"

    # Monta linha com dados (título ou valores)
    def linha_dados(dados):
        return "|" + "|".join(f" {str(dados.get(col, '')).ljust(larguras[col])} " for col in colunas) + "|"

    # Imprime tudo
    print("\n\n")
    print(centralizar(linha_horizontal()))
    print(centralizar(linha_dados({col: col for col in colunas})))  # cabeçalho
    print(centralizar(linha_horizontal()))
    for item in lista:
        print(centralizar(linha_dados(item)))
    print(centralizar(linha_horizontal()))
    print("\n\n")
    print("\n\n")

def adicionar_filme():
    while(True):        
        titulo = input_centralizado("Digite um titulo: " )
        diretor = "Digite um titulo"("Digite o nome do diretor: ")
        ano_lancamento = input("Digite o ano de lançamento")
        genero = input("selecione um genero")
        duracao = input("digite a duração (em min)")
             