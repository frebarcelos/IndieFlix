import json, time
from datetime import datetime
from animacao import centralizar, limpar_terminal,input_centralizado
from funcutils import input_data_valida, input_duracao_valida, input_genero_valido,exibir_data_DDMMYYY,valida_opcoes,input_nota_pessoal_valida

caminho_arquivo = 'filmes.json'

def abrir_arquivo_leitura():
    with open(caminho_arquivo, 'r', encoding='utf-8') as lista_filmes:
            return json.load(lista_filmes)


def abrir_arquivo_escrita(filmes):
        
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(filmes, f, ensure_ascii=False, indent=2)


def imprimir_tabela(lista):    
    
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
    
def gerar_filme(id):
    while(True):
        titulo = input("Título: ").strip()
        diretor = input("Diretor: ").strip()
        data_lancamento = input_data_valida()
        genero = input_genero_valido()
        duracao = input_duracao_valida()
        nota_pessoal = input_nota_pessoal_valida()
        limpar_terminal()
        print(centralizar(f"Titulo: {titulo}\nDiretor: {diretor}\nData de lançamento: {exibir_data_DDMMYYY(data_lancamento)}\nGênero: {genero}\nDuração (min): {duracao}\nNota Pessoal: {nota_pessoal}\nConfirmar ? (Y/n)"))
        
        resposta = input_centralizado()
        if resposta == "Y":
            break
        print("Deseja tentar novamente: (Y/n)")
        resposta = input_centralizado()
        if resposta != "Y":
            break
        limpar_terminal()
        
    return {
        "id": id,
        "titulo": titulo,
        "diretor": diretor,
        "data_lancamento": data_lancamento,
        "genero": genero,
        "duracao": duracao,
        "nota_pessoal": nota_pessoal
    }

def adicionar_filme():
    filmes = abrir_arquivo_leitura()
    novo_filme = gerar_filme(id=(len(filmes) + 1))
    filmes.append(novo_filme)
    abrir_arquivo_escrita(filmes)
    print(centralizar("\n✅ Filme adicionado com sucesso!"))
    time.sleep(1)
    limpar_terminal()
    
def exibir_filmes():    
    lista_filmes = abrir_arquivo_leitura()
    for filme in lista_filmes:
        filme['data_lancamento'] = exibir_data_DDMMYYY(filme['data_lancamento'])
    while True:
        limpar_terminal() 
        imprimir_tabela(lista_filmes)
        escolha = valida_opcoes(opcoes=["1","2","3"],mensagem="[1] Voltar [2] Ordenar Por [3] Editar filme") 
            
        if escolha == 1:
            break
        if escolha == 2:
            while True:
                limpar_terminal()
                escolha_ordem = valida_opcoes(opcoes=["1","2","3","4","5","6","7","8","9"],mensagem="\n[1] Título (A - Z) \n[2] Título (Z - A) \n[3] Diretor \n[4] Data de lançamento ASC \n[5] Data de lançamento DESC \n[6] Duração ASC \n[7] Duração DESC\n[8] Nota Pessoal ASC\n[9] Nota Pessoal DESC", falar="Ordenar por:")
                
                escolha_ordem = int(escolha_ordem)
                if escolha_ordem == 1:
                    lista_filmes.sort(key=lambda f: f["titulo"])
                    break
                if escolha_ordem == 2:
                    lista_filmes.sort(key=lambda f: f["titulo"], reverse=True)
                    break
                if escolha_ordem == 3:
                    lista_filmes.sort(key=lambda f: f["diretor"])
                    break
                if escolha_ordem == 4:
                    lista_filmes.sort(key=lambda f: datetime.strptime(f["data_lancamento"], "%d/%m/%Y"))
                    break 
                if escolha_ordem == 5:
                    lista_filmes.sort(key=lambda f: datetime.strptime(f["data_lancamento"], "%d/%m/%Y"), reverse=True)
                    break
                if escolha_ordem == 6:
                    lista_filmes.sort(key=lambda f: f["duracao"])
                    break                     
                if escolha_ordem == 7:
                    lista_filmes.sort(key=lambda f: f["duracao"], reverse=True)
                    break
                if escolha_ordem == 8:
                    lista_filmes.sort(key=lambda f: f["nota_pessoal"])
                    break
                if escolha_ordem == 9:
                    lista_filmes.sort(key=lambda f: f["nota_pessoal"], reverse=True)
                    break
        if escolha == 3:
                ids = []
                for filme in lista_filmes:
                    ids.append(str(filme['id']))                    
                print(ids)    
                resposta = valida_opcoes(opcoes=ids, mensagem="Digite o id do filme")                
                filme = [f for f in lista_filmes if f["id"] == resposta]
                limpar_terminal()
                imprimir_tabela(filme)
                input()
                        
                    