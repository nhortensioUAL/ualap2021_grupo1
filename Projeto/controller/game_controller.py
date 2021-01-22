import pickle
import models.game_status as mod


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
    tabuleiro = mod.obter_tabuleiro(estado_jogo)
    if(not mod.game_inprogress(estado_jogo)):
        print("Não existe jogo em curso.")
    if(nome not in mod.jogo_jogadores(estado_jogo)):
        print("Jogador não participa no jogo em curso.")
    if(not validar_pecas_especiais(estado_jogo,tamanho_peca)):
        print("Tamanho de peça não disponível.")
    if(not validar_posicao(estado_jogo,tamanho_peca,posicao,sentido)):
        print("Posição irregular.")       
    if(tamanho_peca == 1):
        tabuleiro = insere_peca(tabuleiro,nome,tamanho_peca,posicao,posicao)
    if(sentido == "E"):
        tabuleiro = insere_peca(tabuleiro,nome,tamanho_peca,posicao - tamanho_peca,posicao)
    else:
        tabuleiro = insere_peca(tabuleiro,nome,tamanho_peca,posicao,posicao + tamanho_peca) 
    if(sequencia_vencedora(tabuleiro,nome,estado_jogo["tamanho_sequencia"])):
        estado_jogo = terminar_jogo(estado_jogo,nome)
        print("Sequência conseguida. Jogo terminado.")
    else:    
        estado_jogo["tabuleiro"] = tabuleiro
    return estado_jogo
      

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
        if(posicao_final < 0 or posicao < 0):
            return False
        else:
            return True
    else:
        posicao_final = posicao + tamanho_peca
        if(posicao_final > len(tabuleiro)-1 or posicao > len(tabuleiro)-1):
            return False
        else:
            return True

def insere_peca(tabuleiro,nome,tamanho_peca,posicao_inicial,posicao_final):
    nr_pecas = tamanho_peca
    for linha in range (0, len(tabuleiro)):
      for coluna in range(posicao_inicial,posicao_final):
        if(linha == len(tabuleiro) and nr_pecas > 0):
            tabuleiro[linha][coluna] = nome
            nr_pecas -=1
        else:   
            if(mod.not_empty(tabuleiro,linha,coluna) and nr_pecas > 0):
                tabuleiro[linha-1][coluna] = nome
                nr_pecas -=1
    print("Peça colocada.")
    return tabuleiro

def sequencia_vencedora(tabuleiro,nome,tamanho_sequencia):
    lista_pecas = []
    sequencia_linha = 1
    sequencia_coluna = 1
    sequencia_diagonal_positiva = 1
    sequencia_diagonal_negativa = 1
    for linha in range (0, len(tabuleiro)):
            for coluna in range(0,len(tabuleiro[coluna])):
                if(tabuleiro[linha][coluna] == nome):
                    lista_pecas.append((linha,coluna))
    lista_pecas = lista_pecas.sort()
    for peca1 in lista_pecas:
        for peca2 in lista_pecas:
            if (peca2[0] == peca1[0]+1 and peca2[1]==peca1[1]):
                sequencia_coluna +=1
            if (peca2[0] == peca1[0] and peca2[1] == peca1[1] + 1):
                sequencia_linha +=1
            if(peca2[0] == peca1[0] +1 and peca2[1] == peca1[1] + 1 ):
                sequencia_diagonal_positiva +=1
            if(peca2[0] == peca1[0] - 1 and peca2[1] == peca1[1] - 1 ):
                sequencia_diagonal_negativa +=1
    return sequencia_linha == tamanho_sequencia or sequencia_coluna == tamanho_sequencia or sequencia_diagonal_positiva == tamanho_sequencia or sequencia_diagonal_negativa == tamanho_sequencia


def terminar_jogo(estado_jogo,nome):
    estado_jogo["jogador1"], estado_jogo["jogador2"],estado_jogo["em curso"],estado_jogo["vez"] = " "
    for jogador in estado_jogo["jogadores"]:
        if(jogador == nome):
            estado_jogo["nr_vitorias"] +=1
    return estado_jogo
