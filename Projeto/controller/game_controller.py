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
    if(not mod.game_inprogress(estado_jogo)):
        print("Não existe jogo em curso.")
    if(nome not in mod.jogo_jogadores):
        print("Jogador não participa no jogo em curso.")
    if(not validar_pecas_especiais(estado_jogo,tamanho_peca)):
        print("Tamanho de peça não disponível.")
    if(not validar_posicao(estado_jogo,tamanho_peca,posicao,sentido)):
        print("Posição irregular")       
    tabuleiro = mod.obter_tabuleiro(estado_jogo)
    if(sentido == "E"):
        insere_peca(tabuleiro,tamanho_peca,posicao,posicao - tamanho_peca)
    else:
        insere_peca(tabuleiro,tamanho_peca,posicao,posicao + tamanho_peca) 
      

def mostra_resultado(estado_jogo):
    if(mod.game_inprogress(estado_jogo)):
        tabuleiro = mod.obter_tabuleiro(estado_jogo)
        for linha in range (0, len(tabuleiro)):
            for coluna in range(0,len(tabuleiro[coluna])):
                print (linha+1,coluna+1,tabuleiro[coluna][linha], sep = " ")
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

def validar_pecas_especiais(estado_jogo,tamanho_peca):
    pecas = mod.obter_pecas_especiais(estado_jogo)
    if(tamanho_peca == 1):
        return True
    if(tamanho_peca in pecas):
        return True
    else:
        return False

def validar_posicao(estado_jogo,tamanho_peca,posicao,sentido):
    tabuleiro = mod.obter_tabuleiro(estado_jogo)
    if(sentido == "E"):
        posicao_final = posicao - tamanho_peca
        if(posicao_final < 0):
            return False
        else:
            return True
    else:
        posicao_final = posicao + tamanho_peca
        if(posicao_final > len(tabuleiro)-1):
            return False
        else:
            return True

def insere_peca(tabuleiro,tamanho_peca,posicao_inicial,posicao_final):
    pass

def sequencia_vencedora(estado_jogo,tamanho_sequencia):
    tabuleiro = mod.obter_tabuleiro(estado_jogo)
    for linha in range (0, len(tabuleiro)):
            for coluna in range(0,len(tabuleiro[coluna])):