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

