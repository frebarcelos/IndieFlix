import json, time, copy
from datetime import datetime
from view.animacao import centralizar, limpar_terminal,input_centralizado,falar_ascii
from funcutils import input_data_valida, input_duracao_valida, input_genero_valido,ajusta_data_banco,valida_opcoes,input_nota_pessoal_valida,ajusta_data_salvar,retorno_data_DDMMYYYY

caminho_arquivo = 'filmes.json'

def abrir_arquivo_leitura_filmes(caminho_bd= 'filmes.json', exibir_filmes = True):
    with open(caminho_bd, 'r', encoding='utf-8') as lista_filmes_bd:
            lista_filmes = json.load(lista_filmes_bd)
            if exibir_filmes:
                lista_filmes = ajusta_data_banco(lista_filmes)
                lista_filmes.sort(key=lambda f: f['id'])                
            return lista_filmes


def abrir_arquivo_escrita_filmes(filmes, caminho_bd= 'filmes.json'):
        
    with open(caminho_bd, 'w', encoding='utf-8') as lista_filmes_bd:
        json.dump(filmes, lista_filmes_bd, ensure_ascii=False, indent=2)


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
    
def gerar_filme(id, lista_filmes):
    while(True):
        falar_ascii("Digite os dados do filme que deseja adicionar")
        filme = [{
            "id": id,
            "titulo": input_centralizado("Título: ").strip(),
            "diretor": input_centralizado("Diretor: ").strip(),
            "data_lancamento": input_data_valida(),
            "genero": input_genero_valido(),
            "duracao": input_duracao_valida(),
            "nota_pessoal": input_nota_pessoal_valida()            
        }]
        
        limpar_terminal()
        falar_ascii("Estes dados estão corretos ?")
        imprimir_tabela(filme)
        resposta = valida_opcoes(opcoes=["1","2"], mensagem="[1] Confirmar [2] Tentar Novamente [3] Voltar")       
        if resposta == 1:
            lista_filmes.append(filme[0])
            break        
        if resposta == 3:
            break
        limpar_terminal()
    
    return lista_filmes

def adicionar_filme():    
    filmes = abrir_arquivo_leitura_filmes(exibir_filmes=False)
    filmes= gerar_filme(id=(len(filmes) + 1), lista_filmes=filmes)
    abrir_arquivo_escrita_filmes(filmes=filmes)
    print(centralizar("\n✅ Filme adicionado com sucesso!"))
    time.sleep(1)
    limpar_terminal()
    
def exibir_filmes():        
    lista_filmes = abrir_arquivo_leitura_filmes()
    ordenados=""    
    while True:        
        limpar_terminal()         
        falar_ascii(f"Estes são os filmes disponiveis no seu catálogo{ordenados}")
        imprimir_tabela(lista_filmes)
        escolha = valida_opcoes(opcoes=["0","1","2"],mensagem="[0] Voltar [1] Ordenar Por [2] Editar filme") 
            
        if escolha == 0:
            break
        if escolha == 1:
            while True:
                limpar_terminal()
                escolha_ordem = valida_opcoes(opcoes=["1","2","3","4","5","6","7","8","9"],mensagem="\n[1] Título (A - Z) \n[2] Título (Z - A) \n[3] Diretor(a) \n[4] Data de lançamento ASC \n[5] Data de lançamento DESC \n[6] Duração ASC \n[7] Duração DESC\n[8] Nota Pessoal ASC\n[9] Nota Pessoal DESC", falar="Ordenar por:")
                ordenados = ", ordenados "
                escolha_ordem = int(escolha_ordem)
                if escolha_ordem == 1:
                    lista_filmes.sort(key=lambda f: f["titulo"])
                    ordenados += "por Título (A - Z)"
                    break
                if escolha_ordem == 2:
                    lista_filmes.sort(key=lambda f: f["titulo"], reverse=True)
                    ordenados += "por Título (Z - A)"
                    break
                if escolha_ordem == 3:
                    lista_filmes.sort(key=lambda f: f["diretor"])
                    ordenados += "por Diretor"                    
                    break
                if escolha_ordem == 4:
                    lista_filmes.sort(key=lambda f: datetime.strptime(f["data_lancamento"], "%d/%m/%Y"))
                    ordenados += "pelos mais antigos"                    
                    break 
                if escolha_ordem == 5:
                    lista_filmes.sort(key=lambda f: datetime.strptime(f["data_lancamento"], "%d/%m/%Y"), reverse=True)
                    ordenados += "pelos mais novos"                    
                    break
                if escolha_ordem == 6:
                    lista_filmes.sort(key=lambda f: f["duracao"])
                    ordenados += "pelos mais curtos"
                    break                     
                if escolha_ordem == 7:
                    lista_filmes.sort(key=lambda f: f["duracao"], reverse=True)
                    ordenados += "pelos mais longos"
                    break
                if escolha_ordem == 8:
                    lista_filmes.sort(key=lambda f: f["nota_pessoal"])
                    ordenados += "pelos que você menos gostou"
                    break
                if escolha_ordem == 9:
                    lista_filmes.sort(key=lambda f: f["nota_pessoal"], reverse=True)
                    ordenados += "pelos que você gostou mais"
                    break
        if escolha == 2:
               editar_filme()

def editar_filme():
    
    limpar_terminal()
    falar_ascii("Qual filme você deseja Editar ?")
    lista_filmes = abrir_arquivo_leitura_filmes()  
    imprimir_tabela(lista_filmes)
        
    ids = []
    id_print = "[ "
    for filme in lista_filmes:
        ids.append(str(filme['id']))
        if filme == lista_filmes[-1]:
                id_print += str(filme['id']) + " ]"
        else:                        
            id_print += str(filme['id']) + ", "                   
    resposta = valida_opcoes(opcoes=ids + ["0"], mensagem="Digite o id do filme: " + id_print + " ou digite 0 para sair")
    if resposta == 0:
        return                
    filme = [copy.deepcopy(f) for f in lista_filmes if f["id"] == resposta]
    while True:
        limpar_terminal()
        falar_ascii("Digite a opção que deseja editar:")                    
        imprimir_tabela(filme)        
        resposta_edicao = valida_opcoes(opcoes=["1","2","3","4","5","6","7","8"], mensagem="[1] Voltar (sem salvar) [2] Título [3] Diretor [4] Data de Lançamento [5] Gênero [6] Duração [7] Nota Pessoal [8] Salvar")
        if resposta_edicao == 1:
            break
        if resposta_edicao == 2:
                filme[0]['titulo'] = input_centralizado("Título: ").strip()
        if resposta_edicao == 3:                    
            filme[0]['diretor'] = input_centralizado("Diretor: ").strip()
        if resposta_edicao == 4:
            filme[0]['data_lancamento'] = input_data_valida()
        if resposta_edicao == 5:
            filme[0]['genero'] = input_genero_valido()
        if resposta_edicao == 6:
            filme[0]['duracao'] = input_duracao_valida(formatar_data=False)
        if resposta_edicao == 7:
            filme[0]['nota_pessoal'] = input_nota_pessoal_valida()
        if resposta_edicao == 8:
            lista_filmes[:] = [f for f in lista_filmes if f["id"] != filme[0]['id']]
            lista_filmes.append(filme[0])
            abrir_arquivo_escrita_filmes(filmes=ajusta_data_salvar(lista_filmes))
            lista_filmes.sort(key=lambda f: f['id'])
            print(centralizar("\n✅ Filme editado com sucesso!"))
            time.sleep(1)
            break

def excluir_filme():
    limpar_terminal()
    lista_filmes = abrir_arquivo_leitura_filmes()  
    ids = []
    id_print = "[ "
    for filme in lista_filmes:
        ids.append(str(filme['id']))
        if filme == lista_filmes[-1]:
                id_print += str(filme['id']) + " ]"
        else:                        
            id_print += str(filme['id']) + ", " 
    while True:
        falar_ascii("Qual filme você deseja Excluir ?")
        imprimir_tabela(lista_filmes)                       
        resposta = valida_opcoes(opcoes=ids + ["0"], mensagem="Digite o id do filme: " + id_print + " ou digite 0 para sair")
        if resposta == 0:
            break
        filme = [copy.deepcopy(f) for f in lista_filmes if f["id"] == resposta]
        limpar_terminal
        falar_ascii("Tem certeza que deseja excluir este filme ?")
        imprimir_tabela(filme)
        resposta = valida_opcoes(opcoes=["1","2"], mensagem="[1] Confirmar [2] Voltar")
        if resposta == 1:
            lista_filmes[:] = [f for f in lista_filmes if f["id"] != filme[0]['id']]
            abrir_arquivo_escrita_filmes(filmes=ajusta_data_salvar(lista_filmes))
            print(centralizar("\n✅ Filme Excluído com sucesso!"))
            time.sleep(1)
            break
    