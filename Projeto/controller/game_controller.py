import pickle
import models.game_status as mod

## Instrução RJ. Regista um jogador na lista de jogadores caso este já não tenha sido registado.
def regista_jogador(estado_jogo,nome):
    if(existe_jogador(estado_jogo,nome)):
        print("Jogador existente.")
    else:
        dicionario = {"nome":nome,"nr_vitorias":0,"nr_jogos":0}
        estado_jogo["jogadores"].append(dicionario)
        print ("Jogador registado com sucesso.")

## instrução EJ. Elimina um jogador da lista de jogadores caso este esteja contido na mesma e
##  não participe em nenhum jogo.
def remover_jogador(estado_jogo,nome):
    jogadores = estado_jogo["jogadores"]
    if(not existe_jogador(estado_jogo,nome)):
        print("Jogador não existente.")
    elif((estado_jogo["estado"]["jogador1"]==nome) or (estado_jogo["estado"]["jogador2"]==nome)):
        print("Jogador participa no jogo em curso.")
    else:
        for i in range(len(jogadores)): 
            if jogadores[i]["nome"] == nome: 
                jogadores.pop(i) 
        print ("Jogador removido com sucesso.")
        estado_jogo["jogadores"] = jogadores
        return estado_jogo

## Instrução LJ. Imprime o nome,número de jogos jogados e número de vitórias
##  dos jogadores inscritos por ordem alfabetica 
def listar_jogadores(estado_jogo):
    jogadores = ordena_nome(estado_jogo["jogadores"])
    if (len(jogadores) < 1):
        print ("Não existem jogadores registados.")
    else:
        for jogador in jogadores:
            print(jogador["nome"], str(jogador["nr_jogos"]), str(jogador["nr_vitorias"]))

## Instrução IJ. Inicia um jogo entre dois jogadores com o comprimento, altura, nº sequencia vencedora e
##  quantidade de peças especiais
def iniciar_jogo(estado_jogo,nome1,nome2,comprimento,altura,tamanho_sequencia,tamanho_pecas):
    if (mod.game_inprogress(estado_jogo)):
        print("Existe jogo em curso.")
    elif (nome1 not in mod.jogadores_cadastrados(estado_jogo)) or (nome2 not in mod.jogadores_cadastrados(estado_jogo)):
        print("Jogador não registado.")
    elif (comprimento <= 0) or (altura <= 0) or (altura < (comprimento / 2)) or (altura > comprimento):
        print("Dimensões de grelha inválidas.")
    elif (tamanho_sequencia <= 0) or (tamanho_sequencia > comprimento):
        print("Tamanho de sequência inválido.")
    else:
        c_peca_invalida = 0
        if(tamanho_pecas[0] == ""):
            tamanho_pecas[0] = 0           
        for peca in tamanho_pecas:
            if((int(peca) < 0) or (int(peca) >= tamanho_sequencia)):
                c_peca_invalida +=1
        if(c_peca_invalida > 0):
            print("Dimensões de peças especiais inválidas.")
        else:
            pecas_esp = dict((i,tamanho_pecas.count(i)) for i in tamanho_pecas)
            estado_jogo["estado"]["em_curso"] = True
            estado_jogo["estado"]["comprimento"] = comprimento
            estado_jogo["estado"]["altura"] = altura
            estado_jogo["estado"]["tamanho_sequencia"] = tamanho_sequencia
            estado_jogo["estado"]["jogador1"] = nome1
            estado_jogo["estado"]["jogador2"] = nome2
            estado_jogo["estado"]["tabuleiro"]= [["Vazio" for _ in range(comprimento)] for _ in range(altura)]
            dicionario = {"nome":nome1,"pecas_especiais":pecas_esp}
            estado_jogo["estado"]["tamanho_pecas_especiais"].append(dicionario)
            dicionario = {"nome":nome2,"pecas_especiais":pecas_esp.copy()}
            estado_jogo["estado"]["tamanho_pecas_especiais"].append(dicionario)
            estado_jogo["estado"]["tamanho_pecas_especiais"] = ordena_nome(estado_jogo["estado"]["tamanho_pecas_especiais"])
            print("Jogo iniciado entre", estado_jogo["estado"]["tamanho_pecas_especiais"][0]["nome"], "e", estado_jogo["estado"]["tamanho_pecas_especiais"][1]["nome"] + ".")
    return estado_jogo


## Instrução DJ. Imprime os detalhes(comprimento,altura,jogadores e pecas especiais) do jogo em curso
def detalhes_jogo(estado_jogo):
    if (not mod.game_inprogress(estado_jogo)):
        print("Não existe jogo em curso.")
    else:
        print(str(estado_jogo["estado"]["comprimento"]), str(estado_jogo["estado"]["altura"]))
        for jogador in estado_jogo["estado"]["tamanho_pecas_especiais"]:
            print(jogador["nome"])
            c_pecas = 0
            for item in estado_jogo["estado"]["tamanho_pecas_especiais"]:
                while c_pecas < len(item["pecas_especiais"]):
                    if (item["nome"] == jogador["nome"]):
                        key = list(item["pecas_especiais"].keys())[c_pecas]
                        value = list(item["pecas_especiais"].values())[c_pecas]
                        print(f"{key} {value}")
                    c_pecas +=1
                c_pecas = 0


## Instrução D. Termina o jogo em curso tendo em conta que o jogador que desiste é o perdedor e o outro
## jogador é o vencedor
def desistir(estado_jogo,nome1,nome2=" "):
    if (not mod.game_inprogress(estado_jogo)):
        print("Não existe jogo em curso.")
    elif (nome1 not in mod.jogadores_cadastrados(estado_jogo)) or (nome2 != " " and nome2 not in mod.jogadores_cadastrados(estado_jogo)):
        print("Jogador não registado.")
    elif (nome1 not in mod.jogo_jogadores(estado_jogo)) or (nome2 != " " and nome2 not in mod.jogo_jogadores(estado_jogo)):
        print("Jogador não participa do jogo em curso.")
    else:
        if(nome2 == " "):
            if (nome1 == estado_jogo["estado"]["jogador1"]):
                estado_jogo = terminar_jogo(estado_jogo,estado_jogo["estado"]["jogador2"],estado_jogo["estado"]["jogador1"])
            else:
                estado_jogo = terminar_jogo(estado_jogo,estado_jogo["estado"]["jogador1"],estado_jogo["estado"]["jogador2"])
        else: 
            estado_jogo = terminar_jogo(estado_jogo,estado_jogo["estado"]["jogador1"],estado_jogo["estado"]["jogador2"],True)
        estado_jogo["estado"]["em_curso"] = False
        print("Desistência com sucesso. Jogo terminado.")
    return estado_jogo


## Instrução CP. Coloca a peça indicada no tabuleiro de jogo
def coloca_peca(estado_jogo,nome,tamanho_peca,posicao,sentido="E"):
    tabuleiro = mod.obter_tabuleiro(estado_jogo)
    if(not mod.game_inprogress(estado_jogo)):
        print("Não existe jogo em curso.")
    elif(nome not in mod.jogo_jogadores(estado_jogo)):
        print("Jogador não participa no jogo em curso.")
    elif(not validar_pecas_especiais(estado_jogo,nome,tamanho_peca)):
        print("Tamanho de peça não disponível.")
    elif(not validar_posicao(estado_jogo,tamanho_peca,posicao,sentido)):
        print("Posição irregular.")      
    else: 
        if(tamanho_peca == 1):
            tabuleiro = insere_peca(tabuleiro,nome,tamanho_peca,posicao,posicao)
        elif(sentido == "E"):
            tabuleiro = insere_peca(tabuleiro,nome,tamanho_peca,(posicao - tamanho_peca) + 1,posicao)
            estado_jogo = retira_pecas_especiais(estado_jogo,nome,tamanho_peca)
        else:
            tabuleiro = insere_peca(tabuleiro,nome,tamanho_peca,posicao,(tamanho_peca + posicao) - 1) 
            estado_jogo = retira_pecas_especiais(estado_jogo,nome,tamanho_peca)
        if(sequencia_vencedora(tabuleiro,nome,estado_jogo["estado"]["tamanho_sequencia"])):
            if(estado_jogo["estado"]["jogador1"] == nome):
                estado_jogo = terminar_jogo(estado_jogo,nome,estado_jogo["estado"]["jogador2"])
            else:
                 estado_jogo = terminar_jogo(estado_jogo,nome,estado_jogo["estado"]["jogador1"])
            print("Sequência conseguida. Jogo terminado.")
        else:    
            estado_jogo["tabuleiro"] = tabuleiro
            print("Peça colocada.")
    return estado_jogo
      

## Instrução V. Imprime o tabuleiro de jogo no formato "Altura" "Comprimento" "Conteúdo"
def mostra_resultado(estado_jogo):
    if(mod.game_inprogress(estado_jogo)):
        tabuleiro = mod.obter_tabuleiro(estado_jogo)
        for linha in range (0,len(tabuleiro)): 
            for coluna in range(0,len(tabuleiro[0])):
                print (linha+1,coluna+1,tabuleiro[linha][coluna], sep = " ")
    else:
        print("Não existe jogo em curso.")


## Instrução G. Grava o estado de jogo num ficheiro
def grava_ficheiro(estado_jogo,nome_ficheiro):
    try:
        with open(nome_ficheiro, "wb") as f:
            pickle.dump(estado_jogo, f)
            print ("Jogo gravado.")
    except Exception as e:
        print("Ocorreu um erro na gravação.")


## Instrução L. Lê o estado do jogo de um ficheiro
def le_ficheiro(nome_ficheiro):
    estado_jogo = None
    try:
        with open(nome_ficheiro, "rb") as f:
            estado_jogo = pickle.load(f)
            print ("Jogo carregado.")
    except Exception as e:
        print("Ocorreu um erro no carregamento.")
    return estado_jogo


## Valida se um jogador já está registado.
def existe_jogador(estado_jogo,nome):
   for jogador in estado_jogo["jogadores"]:
        if(jogador["nome"] == nome):
            return True
   return False
   

## Ordena uma lista de jogadores por ordem alfabetica
def ordena_nome(jogadores):
    for i in range(len(jogadores)):
        for j in range(len(jogadores)-i-1):
            if (jogadores[j]["nome"] > jogadores[j+1]["nome"]):
                tmp = jogadores[j+1]
                jogadores[j+1] = jogadores[j]
                jogadores[j] = tmp
    return jogadores


## Valida se o jogador tem a peca especial disponivel para jogar
def validar_pecas_especiais(estado_jogo,nome,tamanho_peca):
    pecas = mod.obter_pecas_especiais(estado_jogo,nome)
    if(tamanho_peca == 1):
        return True
    elif(pecas[str(tamanho_peca)] > 0):
        return True
    else:
        return False


## Valida se alguma das peças que estamos a tentar colocar fica fora do tabuleiro
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
        if((posicao_final > len(tabuleiro[0])-1) or (posicao > len(tabuleiro[0])-1)):
            return False
        else:
            return True


## Função auxiliar de coloca_peca. Dado um tabuleiro,o tamanho da peça e as posição inicial e posição final,
##  coloca a peça no tabuleiro e retorna o tabuleiro modificado
def insere_peca(tabuleiro,nome,tamanho_peca,posicao_inicial,posicao_final):
    for linha in range (0,len(tabuleiro)):
        if(tamanho_peca == 1):
            if(mod.not_empty(tabuleiro,linha,posicao_inicial-1)):
                tabuleiro[linha-1][posicao_inicial-1] = nome
            elif(linha == len(tabuleiro)-1):
                tabuleiro[linha][posicao_inicial-1] = nome
        else:
            for coluna in range(posicao_inicial-1,posicao_final):
                if(mod.not_empty(tabuleiro,linha,coluna) and (not mod.not_empty(tabuleiro,linha-1,coluna))):
                    tabuleiro[linha-1][coluna] = nome
                elif(linha == len(tabuleiro)-1) and (not mod.not_empty(tabuleiro,linha,coluna)):
                    tabuleiro[linha][coluna] = nome
    return tabuleiro


## Valida se existe uma sequência vencedora no tabuleiro
def sequencia_vencedora(tabuleiro,nome,tamanho_sequencia):
    if(sequencia_linha(tabuleiro,nome,tamanho_sequencia)):
        return True
    elif(sequencia_coluna(tabuleiro,nome,tamanho_sequencia)):
        return True
    elif(sequencia_diagonal(tabuleiro,nome,tamanho_sequencia)):
        return True
    else:
        return False


## Valida se existe uma sequência vencedora em linha
def sequencia_linha(tabuleiro,nome,tamanho_sequencia):
    for linha in tabuleiro:
        for item in range(0, len(tabuleiro)-1):
            if(linha[item] == linha[item+1] and linha[item] != "Vazio"):
                sequencia_linha +=1
            else: 
                sequencia_linha = 1
            if(sequencia_linha == tamanho_sequencia):
                return True
    return False


## Valida se existe uma sequência vencedora em coluna
def sequencia_coluna(tabuleiro,nome,tamanho_sequencia):
    lista_pecas = [(-1,-1),(-1,-1)]
    sequencia_coluna = 1
    for coluna in range (0, len(tabuleiro[0])):
            for linha in range(0,len(tabuleiro)):
                if(tabuleiro[linha][coluna] == nome):
                    lista_pecas.pop(0)
                    lista_pecas.append((linha,coluna))
                    if((lista_pecas[1][0] == lista_pecas[0][0] + 1) and (lista_pecas[1][1] == lista_pecas[0][1])):
                        sequencia_coluna +=1
                    else:
                        sequencia_coluna = 1
    return sequencia_coluna == tamanho_sequencia


## Valida se existe uma sequência vencedora na diagonal
def sequencia_diagonal(tabuleiro,nome,tamanho_sequencia):
    lista_pecas = []
    sequencia_diagonal_positiva = 1
    sequencia_diagonal_negativa = 1
    for linha in range (0, len(tabuleiro)):
        for coluna in range(0,len(tabuleiro[0])):
            if(tabuleiro[linha][coluna] == nome):
                lista_pecas.append((linha,coluna))
    if (lista_pecas == None):
        return False
    for peca1 in lista_pecas:
        for peca2 in lista_pecas:
            if((peca2[0] == peca1[0] + 1) and (peca2[1] == peca1[1] + 1)):
                sequencia_diagonal_positiva +=1
            if((peca2[0] == peca1[0] - 1) and (peca2[1] == peca1[1] - 1)):
                 sequencia_diagonal_negativa +=1
    return (sequencia_diagonal_negativa == tamanho_sequencia) or (sequencia_diagonal_positiva==tamanho_sequencia)



## Faz o fecho do jogo corrente atribuindo uma vitória ao jogador vencedor e atualizando o número de jogos
##  jogados para cada jogador que fazia parte do jogo
def terminar_jogo(estado_jogo,vencedor,derrotado,desistencia=False):
    for jogador in estado_jogo["jogadores"]:
        if(desistencia == True):
            if(jogador["nome"] == vencedor):
                jogador["nr_jogos"] +=1
            elif(jogador["nome"] == derrotado):
                jogador["nr_jogos"] +=1
        elif(jogador["nome"] == vencedor):
            jogador["nr_vitorias"] +=1
            jogador["nr_jogos"] +=1
        elif(jogador["nome"] == derrotado):
            jogador["nr_jogos"] +=1
    estado_jogo["estado"]["jogador1"] = " " 
    estado_jogo["estado"]["jogador2"] = " "
    estado_jogo["estado"]["em_curso"] = False
    estado_jogo["estado"]["vez"] = " "
    estado_jogo["estado"]["altura"] = 0
    estado_jogo["estado"]["comprimento"] = 0
    estado_jogo["estado"]["tamanho_pecas_especiais"] = []
    return estado_jogo


## Dada uma peca especial e um jogador, retira a peça especial da posse do jogador caso este a tenha jogado
def retira_pecas_especiais(estado_jogo,nome,tamanho_peca):
    for jogador in estado_jogo["estado"]["tamanho_pecas_especiais"]:
        if (jogador["nome"] == nome) and (jogador["pecas_especiais"][str(tamanho_peca)] > 0):
           jogador["pecas_especiais"][str(tamanho_peca)] -= 1
    return estado_jogo