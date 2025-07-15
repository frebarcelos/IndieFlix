import json, time, copy
from datetime import datetime
from view.animacao import centralizar, limpar_terminal,input_centralizado,falar_ascii
from funcutils import input_data_valida, input_duracao_valida, input_genero_valido,valida_opcoes,input_nota_pessoal_valida
from filmes import Filme


def imprimir_tabela(filmes=Filme.lista):

    if not isinstance(filmes, list):
        filmes = [filmes]
    else:
        filmes= filmes

    if not filmes:
        print(centralizar("Nenhum dado para exibir."))
        return

    # Usa o primeiro objeto para extrair os nomes das colunas
    colunas = list(vars(filmes[0]).keys())

    # Calcula a largura máxima para cada coluna
    larguras = {coluna: len(coluna) for coluna in colunas}
    for filme in filmes:
        for coluna in colunas:
            valor = str(getattr(filme, coluna, ""))
            larguras[coluna] = max(larguras[coluna], len(valor))

    # Monta linha de separação
    def linha_horizontal():
        return "+" + "+".join("-" * (larguras[col] + 2) for col in colunas) + "+"

    # Monta linha de dados (título ou valores)
    def linha_dados(dados_dict):
        return "|" + "|".join(f" {str(dados_dict.get(col, '')).ljust(larguras[col])} " for col in colunas) + "|"

    # Imprime a tabela
    print("\n\n")
    print(centralizar(linha_horizontal()))
    print(centralizar(linha_dados({col: col for col in colunas})))  # cabeçalho
    print(centralizar(linha_horizontal()))
    for filme in filmes:
        dados = vars(filme)  
        print(centralizar(linha_dados(dados)))
    print(centralizar(linha_horizontal()))
    print("\n\n")

    
def gerar_filme():
    while(True):
        falar_ascii("Digite os dados do filme que deseja adicionar")
        novo_filme = Filme(titulo= input_centralizado("Título: ").strip(),
            diretor= input_centralizado("Diretor(a): ").strip(),
            data_lancamento= input_data_valida(),
            genero= input_genero_valido(),
            duracao= input_duracao_valida(),
            nota_pessoal= input_nota_pessoal_valida()  )      
        limpar_terminal()
        falar_ascii("Estes dados estão corretos ?")
        imprimir_tabela(novo_filme)
        resposta = valida_opcoes(opcoes=["1","2"], mensagem="[1] Confirmar [2] Tentar Novamente [3] Voltar")       
        if resposta == 1:
            Filme.salvar(novo_filme)  
            break        
        if resposta == 3:
            break
        limpar_terminal()   

def adicionar_filme(): 
    gerar_filme()    
    print(centralizar("\n✅ Filme adicionado com sucesso!"))
    time.sleep(1)
    limpar_terminal()
    
def exibir_filmes():      
    ordenados=""
    Filme.ordenar_lista()
    while True:        
        limpar_terminal()         
        falar_ascii(f"Estes são os filmes disponíveis no seu catálogo{ordenados}")
        imprimir_tabela()
        escolha = valida_opcoes(opcoes=["0","1","2","3"],mensagem="[0] Voltar [1] Ordenar Por [2] Editar filme [3] Excluir Filme") 
            
        if escolha == 0:
            break
        if escolha == 1:            
            limpar_terminal()
            escolha_ordem = valida_opcoes(opcoes=["1","2","3","4","5","6","7","8","9"],mensagem="\n[1] Título (A - Z) \n[2] Título (Z - A) \n[3] Diretor(a) \n[4] Data de lançamento ASC \n[5] Data de lançamento DESC \n[6] Duração ASC \n[7] Duração DESC\n[8] Nota Pessoal ASC\n[9] Nota Pessoal DESC", falar="Ordenar por:")
            ordenados = ", ordenados "
            ordenados = ", ordenados " + Filme.ordenar_lista(opcao=escolha_ordem)                
        if escolha == 2:
               editar_filme()
        if escolha == 3:
                excluir_filme()

def editar_filme():
    
    limpar_terminal()
    falar_ascii("Qual filme você deseja Editar ?")
    imprimir_tabela()

    ids = []
    id_print = "[ "
    for filme in Filme.lista:
        ids.append(str(filme.id))
        if filme == Filme.lista[-1]:
                id_print += str(filme.id) + " ]"
        else:                        
            id_print += str(filme.id) + ", "                   
    resposta = valida_opcoes(opcoes=ids + ["0"], mensagem="Digite o id do filme: " + id_print + " ou digite 0 para sair")
    if resposta == 0:
        return                
    filme = Filme.find_by_id(resposta)
    while True:
        limpar_terminal()
        falar_ascii("Digite a opção que deseja editar:")                    
        imprimir_tabela(filme)        
        resposta_edicao = valida_opcoes(opcoes=["1","2","3","4","5","6","7","8"], mensagem="[1] Voltar (sem salvar) [2] Título [3] Diretor [4] Data de Lançamento [5] Gênero [6] Duração [7] Nota Pessoal [8] Salvar")
        if resposta_edicao == 1:
            break
        if resposta_edicao == 2:
                filme.titulo = input_centralizado("Título: ").strip()
        if resposta_edicao == 3:                    
            filme.diretor = input_centralizado("Diretor(a): ").strip()
        if resposta_edicao == 4:
            filme.data_lancamento = input_data_valida()
        if resposta_edicao == 5:
            filme.genero = input_genero_valido()
        if resposta_edicao == 6:
            filme.duracao = input_duracao_valida(formatar_data=False)
        if resposta_edicao == 7:
            filme.nota_pessoal = input_nota_pessoal_valida()
        if resposta_edicao == 8:
            Filme.editar_filme(filme)
            print(centralizar("\n✅ Filme editado com sucesso!"))
            time.sleep(1)
            break

def excluir_filme():
    limpar_terminal()
    ids = []
    id_print = "[ "
    for filme in Filme.lista:
        ids.append(str(filme.id))
        if filme == Filme.lista[-1]:
                id_print += str(filme.id) + " ]"
        else:                        
            id_print += str(filme.id) + ", " 
    while True:
        falar_ascii("Qual filme você deseja Excluir ?")
        imprimir_tabela()                       
        resposta = valida_opcoes(opcoes=ids + ["0"], mensagem="Digite o id do filme: " + id_print + " ou digite 0 para sair")
        if resposta == 0:
            break
        filme = Filme.find_by_id(resposta)
        limpar_terminal
        falar_ascii("Tem certeza que deseja excluir este filme ?")
        imprimir_tabela(filme)
        resposta = valida_opcoes(opcoes=["1","2"], mensagem="[1] Confirmar [2] Voltar")
        if resposta == 1:
            Filme.excluir_filme(filme.id)
            print(centralizar("\n✅ Filme Excluído com sucesso!"))
            time.sleep(1)
            break
    