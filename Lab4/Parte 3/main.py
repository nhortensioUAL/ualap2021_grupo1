from bmpmono import *

if __name__ == "__main__":
    ficheiros = input()
    ficheiros = ficheiros.split(" ")
    if(len(ficheiros) == 2):
        converter_imagem(ficheiros[0],ficheiros[1])
    else:
        print("Nº de parâmetros errado.")