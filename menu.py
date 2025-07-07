import time

from animacao import centralizar,falar_ascii,input_centralizado,limpar_terminal
from catalogo import exibir_filmes,adicionar_filme
from funcutils import valida_opcoes

escolhas_str = ["1","2","3","4"]

#falar_ascii("Olá, tudo bem ?")
#falar_ascii("Bem vindo ao IndieFlix")

        
    
while(True):
    
    escolha = valida_opcoes(opcoes=["1","2","3","4"], mensagem="[1] Listar filmes [2] Adicionar filme [3] Buscar filme [4] Sair", falar="O que você deseja fazer ?") 
           
    escolha = int(escolha)
    if escolha == 4:
        print(centralizar("Saindo......"))
        time.sleep(1)
        limpar_terminal()
        break
    if escolha == 1:
        limpar_terminal()
        exibir_filmes()
                    
    if escolha == 2:
        limpar_terminal()
        adicionar_filme()
    
