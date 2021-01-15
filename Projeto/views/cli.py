import controller as con
import views as v

if __name__ == "__main__":
    estado_jogo = v.cria_estado()
    instrucao = input("Insira a instrucao:")
    instrucao = instrucao.split(" ")
    while True:
        if(instrucao[0] == "RJ"):
            con.regista_jogador(estado_jogo,instrucao[1])
        if(instrucao[0] == "EJ"):
            con.remover_jogador(estado_jogo,instrucao[1])
        if(instrucao[0] == "LJ"):
            con.listar_jogadores(estado_jogo)
        if(instrucao[0] == "IJ"):
            segunda_linha= input()
            segunda_linha = segunda_linha.split(" ")
            tamanho_pecas = input()
            tamanho_pecas = tamanho_pecas.split(" ")
            con.iniciar_jogo(estado_jogo,instrucao[1],instrucao[2],segunda_linha[0],segunda_linha[1],segunda_linha[2], tamanho_pecas)
        if(instrucao[0] == "DJ"): 
            con.detalhes_jogo(estado_jogo)
        if(instrucao[0] == "D"):
            if(instrucao[2]):
                con.desiste(estado_jogo,instrucao[1],instrucao[2])
            else:
                con.desistir(estado_jogo,instrucao[1])
        if(instrucao[0] == "CP"):
            if(instrucao[2] == "1"):
                con.coloca_peca(estado_jogo,instrucao[1],instrucao[2],instrucao[3])
            else:
                con.coloca_peca(estado_jogo,instrucao[1],instrucao[2],instrucao[3],instrucao[4])
        if(instrucao[0] == "V"):        
            con.mostra_resultado(estado_jogo)
        if(instrucao[0] == "G"):
             con.grava_ficheiro(estado_jogo,instrucao[1])
        if(instrucao[0] == "L"):
            con.le_ficheiro(estado_jogo,instrucao[1])
             