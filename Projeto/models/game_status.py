def cria_estado():
    return {
        "jogadores": [],
        "estado":
            {
            "em_curso":bool,
            "jogador1":str,
            "jogador2":str,
            "vez":str,
            "comprimento":int,
            "altura":int,
            "tamanho_sequencia":int,
            "tamanho_pecas_especiais": [],
            "tabuleiro":[],      
            }     
        }

# Devolve o tabuleiro do jogo
def obter_tabuleiro(estado_jogo):
    return estado_jogo["estado"]["tabuleiro"] 


# Devolve "True" se houver um jogo em curso
def game_inprogress(estado_jogo):
    return estado_jogo["estado"]["em_curso"] == True


#Devolve o nome do jogador que tem a vez
def quem_vez(estado_jogo):
    return estado_jogo["estado"]["vez"]


#Devolve uma lista com os jogadores inscritos
def jogadores_cadastrados(estado_jogo):
    jogadores = []
    for jogador in estado_jogo["jogadores"]: 
        jogadores.append(jogador["nome"])
    return jogadores


#Devolve uma lista com os nomes dos jogadores que estão a participar no jogo em curso
def jogo_jogadores(estado_jogo):
    return estado_jogo["estado"]["jogador1"],estado_jogo["estado"]["jogador2"]


#Valida se uma certa posição do tabuleiro está preenchida
def not_empty(tabuleiro,linha,coluna):
    return tabuleiro[linha][coluna] != "Vazio"


#Devolve o tamanho da sequência vencedora
def obter_tamanho_sequencia(estado_jogo):
    return estado_jogo["estado"]["tamanho_sequencia"]


#Devolve uma lista com a quantidade e tamanho de peças especiais
def obter_pecas_especiais(estado_jogo, nome):
    for jogador in estado_jogo["estado"]["tamanho_pecas_especiais"]:
        if (nome == jogador["nome"]):
            return jogador["pecas_especiais"]