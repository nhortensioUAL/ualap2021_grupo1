def ler_nomes(nome_ficheiro):
    nomes = []
    file = open(nome_ficheiro, "r", encoding = 'utf-8')
    data = file.readlines()
    data.pop(0)
    file.close()
    for row in data:
        row = row.split(";")
        d = {"nome":row[0],"registos":int(row[1]),"genero":row[2].replace("\n","")}
        nomes.append(d)    
    return nomes


def listar_nomes(nomes):
    for nome in nomes:
        print(nome["nome"])
        
        
def listas_nomes_genero(nomes,genero):
    for nome in nomes:
        if(nome["genero"] == genero):
            print(nome["nome"])


def listas_nomes(nomes,min_registo):
    for nome in nomes:
        if(nome["registos"] >= min_registo):
            print(nome["nome"])
            
