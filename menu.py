import time, json

from animacao import centralizar,falar_ascii,input_centralizado,limpar_terminal
from catalogo import imprimir_tabela,adicionar_filme

#falar_ascii("Olá, tudo bem ?")
#falar_ascii("Bem vindo ao IndieFlix")

        
    
while(True):
    falar_ascii("O que você deseja fazer ?")
    print("\n" + centralizar(f" [1] Listar filmes [2] Adicionar filme [3] Buscar filme [4] Sair"))
    escolha = input_centralizado()
    if not escolha.isdigit():
        print("\n" + centralizar("Digite uma entrada valida!"))
        input()
    else:        
        escolha = int(escolha)
        if escolha == 4:
            print(centralizar("Saindo......"))
            time.sleep(1)
            limpar_terminal()
            break
        if escolha == 1:
            limpar_terminal()
            imprimir_tabela()
            print(centralizar("Clique qualquer tecla para voltar!"))
            input_centralizado()
        if escolha == 2:
            limpar_terminal()
            adicionar_filme()
    
