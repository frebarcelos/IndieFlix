import os
import time
from view.lapras import boca_aberta, boca_fechada

def centralizar(texto):
    
    linhas = texto.split('\n')
    largura_terminal = os.get_terminal_size().columns
    largura_bloco = max(len(linha) for linha in linhas)
    margem_esquerda = (largura_terminal - largura_bloco) // 2

    return '\n'.join(' ' * margem_esquerda + linha for linha in linhas)

def input_centralizado(mensagem="", margem_perc=0.05):
    largura = os.get_terminal_size().columns
    centro = largura // 2
    margem = int(largura * margem_perc)

    coluna = max(centro - margem, 1)

    # Move o cursor horizontalmente, mas mantém a linha atual
    print("\n" + f"\033[{coluna}G", end='', flush=True)  # \033[{col}G = vai pra coluna {col}
    return input(mensagem)

def centralizar_ascii(arte):
    linhas = arte.strip('\n').split('\n')
    return '\n'.join(centralizar(linha) for linha in linhas)

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def falar_ascii(fala: str, velocidade: float = 0.08):
    
    texto_em_progresso = ""
    boca = True  

    for letra in fala:
        texto_em_progresso += letra
        limpar_terminal()
        print(centralizar_ascii(boca_aberta if boca else boca_fechada))
        print("\n")
        print(centralizar(f"🗣️ {texto_em_progresso}_"))  # Linha de fala
        boca = not boca
        time.sleep(velocidade)

   
    limpar_terminal()
    print(centralizar_ascii(boca_fechada))
    print("\n\n" + centralizar(f"🗣️ {texto_em_progresso}"))