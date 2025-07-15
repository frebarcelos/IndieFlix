
from datetime import datetime
from view.animacao import centralizar, limpar_terminal, input_centralizado,falar_ascii


#Lista dos Generos de filme validos
GENEROS_VALIDOS = ["documentario", "curta", "filme independente"]


def input_data_valida(formatar_data = True):    
    while True:
        entrada = input_centralizado("Data de lançamento (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, "%d/%m/%Y")
            if(formatar_data):
                return data.strftime("%d/%m/%Y")
            return data  
        except ValueError:
            print("⚠️  Data inválida. Use o formato DD/MM/AAAA (ex: 01/07/2025).")

def input_genero_valido():    
    generos = "[ "
    for genero in GENEROS_VALIDOS:
        if genero == GENEROS_VALIDOS[-1]:
            generos += str(genero) + " ]"
        else:
            generos += str(genero) + ", "
    print(centralizar(f"\nGêneros permitidos: {generos}"))
    while True:
        entrada = input_centralizado("Gênero: ").strip().lower()
        if entrada in GENEROS_VALIDOS:
            return entrada
        print("⚠️  Gênero inválido. Escolha um dos permitidos.")

def input_duracao_valida():    
    while True:
        entrada = input_centralizado("Duração (em minutos): ").strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("⚠️  Duração inválida. Digite um número inteiro positivo.")
        
def input_nota_pessoal_valida():
    while True:
        entrada = input_centralizado("Nota Pessoal (1-5): ").strip()
        if entrada.isdigit() and int(entrada) > 0 and int(entrada) < 6:
            return int(entrada)
        print("⚠️  Nota Pessoal. Digite um número inteiro entre 1 e  5.")
        
def retorno_data_DDMMYYYY(data):
    return datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")

def retorno_data_YYYYMMDD(data):
    return datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")

def valida_opcoes(opcoes, mensagem="Digite uma opção:",falar=None):
    
    while True:
        if falar != None:
            falar_ascii(falar)
        print(f"\n" + centralizar(mensagem))
        escolha = input_centralizado()        
        if not escolha in opcoes:
                print("\n" + centralizar("Digite uma entrada valida!"))
                input()
                limpar_terminal()
        else:
            return int(escolha)