from controller import game_controller as con
from models import game_status as mod

def cli():
    estado_jogo = mod.cria_estado()
    while True:
        try:
            instrucao = input()
            instrucao = instrucao.split(" ")
        except EOFError as e1:
            break
        if(instrucao[0] == "RJ"):
            con.regista_jogador(estado_jogo,instrucao[1])
        elif(instrucao[0] == "EJ"):
            con.remover_jogador(estado_jogo,instrucao[1])
        elif(instrucao[0] == "LJ"):
            con.listar_jogadores(estado_jogo)
        elif(instrucao[0] == "IJ"):
            segunda_linha = input()
            segunda_linha = segunda_linha.split(" ")
            tamanho_pecas = input()
            tamanho_pecas = tamanho_pecas.split(" ")
            estado_jogo = con.iniciar_jogo(estado_jogo,instrucao[1],instrucao[2],int(segunda_linha[0]),int(segunda_linha[1]),int(segunda_linha[2]), tamanho_pecas)
        elif(instrucao[0] == "DJ"): 
            con.detalhes_jogo(estado_jogo)
        elif(instrucao[0] == "D"):
            if(len(instrucao) == 3):
                estado_jogo = con.desistir(estado_jogo,instrucao[1],instrucao[2])
            else:
                estado_jogo = con.desistir(estado_jogo,instrucao[1])
        elif(instrucao[0] == "CP"):
            if(instrucao[2] == "1"):
                con.coloca_peca(estado_jogo,instrucao[1],int(instrucao[2]),int(instrucao[3]))
            else:
                con.coloca_peca(estado_jogo,instrucao[1],int(instrucao[2]),int(instrucao[3]),instrucao[4])
        elif(instrucao[0] == "V"):        
            con.mostra_resultado(estado_jogo)
        elif(instrucao[0] == "G"):
            con.grava_ficheiro(estado_jogo,instrucao[1])
        elif(instrucao[0] == "L"):
            estado_jogo = con.le_ficheiro(instrucao[1])
        else:
            print ("Instrução inválida.")