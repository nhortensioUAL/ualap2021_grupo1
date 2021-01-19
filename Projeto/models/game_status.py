def cria_estado():
    return {
        "jogadores": [
            {
            "nome": str,
            "nr_vitorias": int,
            "nr_jogos": int,
             }
                    ],
        "estado":[
            {
            "em curso":str,
            "jogador1":str,
            "jogador2":str,
            "vez":str,
            "comprimento":int,
            "altura":int,
            "tamanho_sequencia":int,
            "tamanho_peças_especiais": [],
            "tabuleiro":[],
            "vencedor":str,      
            }
            ]     
        }

# Devolve o tabuleiro do jogo
def obter_tabuleiro(estado_jogo):
    return estado_jogo["tabuleiro"]
# Devolve "True" se houver um jogo em curso
def game_inprogress(estado_jogo):
    return estado_jogo["em_curso"] == "True"
#Devolve o nome do jogador que tem a vez
def quem_vez(estado_jogo):
    return estado_jogo["vez"]
#Devolve uma lista  com os nomes dos jogadores que estão a participar no jogo em curso
def jogo_jogadores(estado_jogo):
    return estado_jogo["jogador1"],estado_jogo["jogador2"]