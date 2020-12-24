def ler_jogo(ficheiro):
    jogo=[]
    file = open (ficheiro , "r")
    rows = file.read().splitlines()
    file.close()
    for row in rows:
        row = row.split(";")
        jogo.append(row)
    return jogo    

def contar_bombas(m):
    nr_bombas = 0
    for i in m:
        for z in i:
            if(int(z) == -1):
                nr_bombas += 1
    return nr_bombas
    
def contar_bombas_adjacentes(m,x,y):
    nr_bombas = 0
    if((0 < x <= len(m) - 2) & (0 < y <= len(m[x]) - 2)):
        for linha in range (x - 1,x + 2):
            print("linha: ", linha , "  ", x)
            for coluna in range (y - 1, y + 2):
                print("coluna:" , coluna , "   ", y)
                if((linha != x) or (coluna != y)):
                     if(int(m[linha][coluna]) == -1):
                        nr_bombas = nr_bombas + 1
                        print (nr_bombas)

                   
    else:
        pass                    
    return nr_bombas
    
if __name__ == "__main__":
    jogo = ler_jogo("minefield.csv")
    print(jogo)
    print(contar_bombas(jogo))
    print("AQUI" ,contar_bombas_adjacentes(jogo,3,3))