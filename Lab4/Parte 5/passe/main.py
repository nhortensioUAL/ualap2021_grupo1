from program import *
from tab_precos import *

if __name__ == "__main__":
    clientes = []
    tabela_precos = cria_tabela_precos()
    while True:
        instrucoes = input()
        instrucoes = instrucoes.split(" ")
        if(instrucoes [0] == "R"):
            if(existe_escalao(instrucoes[4])):
                regista_cliente(clientes,instrucoes[1],instrucoes[2],instrucoes[3],
                            instrucoes[4],instrucoes[5])
            else:
                print("Escalão inexistente, insira um escalão válido.")
        if(instrucoes[0] == "EP"):
           if(existe_tipo_passe(instrucoes[2])):
            adquirir_passe(clientes,instrucoes[1],instrucoes[2],tabela_precos)
        if(instrucoes[0] == "CV"):
           ver_validade(clientes,instrucoes[1])
        if(instrucoes[0] == "G"):
            guardar_ficheiro(clientes,instrucoes[1])
        if(instrucoes[0] == "L"):
            ler_ficheiro(clientes,instrucoes[1])
        if(instrucoes[0] == "S"):
            break

