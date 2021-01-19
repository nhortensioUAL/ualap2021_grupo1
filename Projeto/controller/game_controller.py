import pickle
from models import game_status as mod


def regista_jogador(estado_jogo,nome):
    pass

def remover_jogador(estado_jogo,nome):
    pass

def listar_jogadores(estado_jogo):
    pass

def iniciar_jogo(estado_jogo,nome1,nome2,comprimento,altura,tamanho_sequencia,tamanho_pecas):
    pass

def detalhes_jogo(estado_jogo):
    pass

def desistir(estado_jogo,nome1,nome2=" "):
    pass

def coloca_peca(estado_jogo,nome,tamanho_peca,posicao,sentido="E"):
    pass

def mostra_resultado(estado_jogo):
    if(mod.game_inprogress(estado_jogo)):
        tabuleiro = mod.obter_tabuleiro(estado_jogo)
        for coluna in range (0, len(tabuleiro)):
            for linha in range(0,len(tabuleiro[coluna])):
                print (coluna+1,linha+1,tabuleiro[coluna][linha], sep = " ")
    else:
        print("Não existe jogo em curso")

def grava_ficheiro(estado_jogo,nome_ficheiro):
    try:
        with open("file.save", "wb") as f:
            pickle.dump(estado_jogo, f)
            print ("Jogo gravado.")
    except Exception as e:
        print("Ocorreu um erro na gravação.")

def le_ficheiro(nome_ficheiro):
    estado_jogo = None
    try:
        with open("file.save", "rb") as f:
            estado_jogo = pickle.load(f)
            print ("Jogo carregado.")
    except Exception as e:
        print("Ocorreu um erro no carregamento.")
    return estado_jogo