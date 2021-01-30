from Projeto.models.game_status import jogadores_cadastrados
import pickle
import models.game_status as mod


def regista_jogador(estado_jogo,nome):
    if(existe_jogador(estado_jogo,nome)):
        print("Jogador existente.", "\n")
    else:
        dicionario = {"nome":nome,"nr_vitorias":0,"nr_jogos":0}
        estado_jogo["jogadores"].append(dicionario)
        print ("Jogador registado com sucesso.", "\n")

def remover_jogador(estado_jogo,nome):
    if(existe_jogador(estado_jogo,nome) == False):
        print("Jogador não existente.", "\n")
    elif(mod.jogo_jogadores(["estado"]["jogador1"])==(estado_jogo,nome)) or (mod.jogo_jogadores(["estado"]["jogador2"])==(estado_jogo,nome)):
        print("Jogador participa no jogo em curso.", "\n")
    else:
        del estado_jogo["jogadores"]["nome":nome]
        print ("Jogador removido com sucesso.", "\n")

def listar_jogadores(estado_jogo):
    print(jogadores_cadastrados)
    print ("Não existem jogadores registados.", "\n")

def iniciar_jogo(estado_jogo,nome1,nome2,comprimento,altura,tamanho_sequencia,tamanho_pecas):
    if mod.game_inprogress(estado_jogo):
        print("Existe um jogo em curso.")
    elif nome1 not in mod.jogadores_cadastrados(estado_jogo) or nome2 not in mod.jogadores_cadastrados(estado_jogo):
        print("Jogador não registrado.")
    elif comprimento <= 0 or altura <= 0 or (comprimento/2) > altura or altura < comprimento:
        print("Dimensões de grelha inválidas.")
    elif tamanho_sequencia <= 0 or tamanho_sequencia > comprimento:
        print("Tamanho de sequência inválido.")
    else:
        c_peca_invalida = 0
        for peca in tamanho_pecas:
            if int(peca) <= 0 and int(peca) >= tamanho_sequencia:
                c_peca_invalida +=1
            if(c_peca_invalida > 0):
                print("Dimensões de peças especiais inválidas.")
            else:
                estado_jogo["estado"]["em_curso"] = True
                estado_jogo["estado"]["comprimento"] = comprimento
                estado_jogo["estado"]["altura"] = altura
                estado_jogo["estado"]["tamanho_sequencia"] = tamanho_sequencia
                estado_jogo["estado"]["tamanho_pecas_especiais"][0]["nome"] = nome1
                estado_jogo["estado"]["tamanho_pecas_especiais"][1]["nome"] = nome2
                estado_jogo["estado"]["jogador1"] = nome1
                estado_jogo["estado"]["jogador2"] = nome2
                estado_jogo["estado"]["tabuleiro"]= [["Vazio" for _ in range(altura)] for _ in range(comprimento)]
                for jogador in estado_jogo["estado"]["tamanho_pecas_especiais"]:
                    for peca in tamanho_pecas:
                        jogador["pecas_especiais"].append(peca)                            
                        
            print(f"Jogo iniciado entre {nome1} e {nome2}.")
    return estado_jogo

def detalhes_jogo(estado_jogo):
    if not mod.game_inprogress(estado_jogo):
        print("Não existe um jogo em curso.")
    else:
        print(str(estado_jogo["estado"]["comprimento"]) + " " + str(estado_jogo["estado"]["altura"]))
        for jogador in estado_jogo["estado"]["tamanho_pecas_especiais"]:
            pecas_esp = dict((i,jogador["pecas_especiais"].count(i)) for i in jogador["pecas_especiais"])
            print(jogador["nome"])
            c_pecas = 0
            while c_pecas < len(pecas_esp):
                key = list(pecas_esp.keys())[c_pecas]
                value = list(pecas_esp.values())[c_pecas]
                print(f"{key} {value}")
                c_pecas +=1

def desistir(estado_jogo,nome1,nome2=" "):
    jogador_desistente = " "
    jogador_vencedor = " "
    print(estado_jogo)
    if not mod.game_inprogress(estado_jogo):
        print("Não existe um jogo em curso.")
    elif nome1 not in mod.jogadores_cadastrados(estado_jogo) or (nome2 != " " and nome2 not in mod.jogadores_cadastrados(estado_jogo)):
        print("Jogador não registrado.")
    elif nome1 not in mod.jogo_jogadores(estado_jogo) or (nome2 != " " and nome2 not in mod.jogo_jogadores(estado_jogo)):
        print("Jogador não participa do jogo em curso.")
    else:
        if(nome2 == " "):
            if (nome1 == estado_jogo["estado"]["jogador1"]):
                jogador_desistente = estado_jogo["estado"]["jogador1"]
                jogador_vencedor = estado_jogo["estado"]["jogador2"]
            else:
                jogador_desistente = estado_jogo["estado"]["jogador2"]
                jogador_vencedor = estado_jogo["estado"]["jogador1"]
            for jogador_registado in estado_jogo["jogadores"]:
                if (jogador_registado["nome"] == jogador_desistente):
                    estado_jogo["jogadores"]["nr_jogos"]+=1
                if (jogador_registado["nome"] == jogador_vencedor): 
                    estado_jogo["jogadores"]["nr_vitorias"]+=1
                    estado_jogo["jogadores"]["nr_jogos"]+=1
        else: 
            for jogador_registado in estado_jogo["jogadores"]:
                if (jogador_registado["nome"] == nome1 or jogador_registado["nome"] == nome2):
                    estado_jogo["jogadores"]["nr_jogos"]+=1
        estado_jogo["estado"]["em_curso"] = False
        print("Desistência com sucesso. Jogo terminado.")
    return estado_jogo

def coloca_peca(estado_jogo,nome,tamanho_peca,posicao,sentido="E"):
    tabuleiro = mod.obter_tabuleiro(estado_jogo)
    if(not mod.game_inprogress(estado_jogo)):
        print("Não existe jogo em curso.")
    elif(nome not in mod.jogo_jogadores(estado_jogo)):
        print("Jogador não participa no jogo em curso.")
    elif(not validar_pecas_especiais(estado_jogo,tamanho_peca)):
        print("Tamanho de peça não disponível.")
    elif(not validar_posicao(estado_jogo,tamanho_peca,posicao,sentido)):
        print("Posição irregular.")      
    else: 
        if(tamanho_peca == 1):
            tabuleiro = insere_peca(tabuleiro,nome,tamanho_peca,posicao,posicao)
        elif(sentido == "E"):
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


def existe_jogador(estado_jogo,nome):
   for jogador in estado_jogo["jogadores"]:
        if(jogador["nome"] == nome):
            return True
   return False

def validar_pecas_especiais(estado_jogo,tamanho_peca):
    pecas = mod.obter_pecas_especiais(estado_jogo)
    if(tamanho_peca == 1):
        return True
    elif(tamanho_peca in pecas):
        return True
    else:
        return False

def validar_posicao(estado_jogo,tamanho_peca,posicao,sentido):
    tabuleiro = mod.obter_tabuleiro(estado_jogo)
    if(sentido == "E"):
        posicao_inicial = posicao - tamanho_peca
        if(posicao_inicial < 0 or posicao < 0):
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
    for linha in range (0, len(tabuleiro)):
      for coluna in range(posicao_inicial,posicao_final):
        if(mod.not_empty(tabuleiro,linha,coluna)):
            tabuleiro[linha-1][coluna] = nome
        elif(linha == len(tabuleiro)):
            tabuleiro[linha][coluna] = nome
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
            if(peca2[0] == peca1[0] +1 and peca2[1] == peca1[1] + 1):
                sequencia_diagonal_positiva +=1
            if(peca2[0] == peca1[0] - 1 and peca2[1] == peca1[1] - 1):
                sequencia_diagonal_negativa +=1
    return sequencia_linha == tamanho_sequencia or sequencia_coluna == tamanho_sequencia or sequencia_diagonal_positiva == tamanho_sequencia or sequencia_diagonal_negativa == tamanho_sequencia


def terminar_jogo(estado_jogo,nome):
    estado_jogo["jogador1"], estado_jogo["jogador2"],estado_jogo["em curso"],estado_jogo["vez"] = " "
    for jogador in estado_jogo["jogadores"]:
        if(jogador == nome):
            estado_jogo["nr_vitorias"] +=1
    return estado_jogo
