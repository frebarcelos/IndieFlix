import time

from view.animacao import centralizar,limpar_terminal, falar_ascii
from catalogo import exibir_filmes,adicionar_filme,editar_filme,excluir_filme
from funcutils import valida_opcoes
from filmes import Filme
from busca import buscar_filme

escolhas_str = ["1","2","3","4"]

falar_ascii("Olá, tudo bem ?")
falar_ascii("Bem vindo ao IndieFlix")
Filme.carregar()

        
    
while(True):    
    escolha = valida_opcoes(opcoes=["1","2","3","4","5","0"], mensagem="[1] Listar filmes [2] Adicionar filme [3] Editar filme  [4] Excluir filme [5] Buscar filme [0] Sair", falar="O que você deseja fazer ?")            
    if escolha == 0:
        print(centralizar("Saindo......"))
        time.sleep(1)
        limpar_terminal()
        break
    if escolha == 1:        
        exibir_filmes()                    
    if escolha == 2:        
        adicionar_filme()
    if escolha == 3:        
        editar_filme()
    if escolha == 4:        
        excluir_filme()
    if escolha ==5:
        buscar_filme()
    
