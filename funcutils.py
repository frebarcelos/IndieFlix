
from datetime import datetime
from animacao import centralizar, limpar_terminal, input_centralizado,falar_ascii


#Lista dos Generos de filme validos
GENEROS_VALIDOS = {"documentario", "curta", "filme independente"}


def input_data_valida():
    # Solicita e valida a data no formato DD/MM/AAAA e retorna como YYYY-MM-DD.
    while True:
        entrada = input("Ano de lançamento (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, "%d/%m/%Y")
            return data.strftime("%Y-%m-%d")  # formato ISO
        except ValueError:
            print("⚠️  Data inválida. Use o formato DD/MM/AAAA (ex: 01/07/2025).")

def input_genero_valido():
    # Solicita e valida o gênero.
    print("Gêneros permitidos:", ', '.join(GENEROS_VALIDOS))
    while True:
        entrada = input("Gênero: ").strip().lower()
        if entrada in GENEROS_VALIDOS:
            return entrada
        print("⚠️  Gênero inválido. Escolha um dos permitidos.")

def input_duracao_valida():
    # Solicita e valida a duração como número inteiro positivo.
    while True:
        entrada = input("Duração (em minutos): ").strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("⚠️  Duração inválida. Digite um número inteiro positivo.")
        
def input_nota_pessoal_valida():
    while True:
        entrada = input("Nota Pessoal (1-5): ").strip()
        if entrada.isdigit() and int(entrada) > 0 and int(entrada) < 6:
            return int(entrada)
        print("⚠️  Nota Pessoal. Digite um número inteiro entre 1 e  5.")
        
def exibir_data_DDMMYYY(data):
    return datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")

def valida_opcoes(opcoes, mensagem="Digite uma opção:",falar=None):
    
    while True:
        if falar != None:
            falar_ascii(falar)
        print("\n" + centralizar(mensagem))
        escolha = input_centralizado()        
        if not escolha in opcoes:
                print("\n" + centralizar("Digite uma entrada valida!"))
                input()
                limpar_terminal()
        else:
            return int(escolha)