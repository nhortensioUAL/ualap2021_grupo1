from bmplib import *

def converter_imagem(ficheiro, ficheiro_mono):
    imagem_mono = []
    imagem = ler_imagem(ficheiro)
    for tuplo in imagem:
           if(tuplo.count(255) == 3):
               imagem_mono.append((255,255,255))
           else:
               imagem_mono.append((0,0,0))
    escrever_imagem(ficheiro,ficheiro_mono,imagem_mono)


if __name__ == "__main__":
    ficheiros = input()
    ficheiros = ficheiros.split(" ")
    if(len(ficheiros) == 2):
        converter_imagem(ficheiros[0],ficheiros[1])
    else:
        print("Parâmetros insuficientes")
        
        
        

    