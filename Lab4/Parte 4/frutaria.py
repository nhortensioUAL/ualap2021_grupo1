import random

def cria_cesto():
    return   {
     "produtos": [
        {
            "nome": str,
            "quantidade": int,
            "preco_unitario": float
        }
    ],
     "total": float
}

def atualiza_total (cesto):
    cesto["total"] = 0
    for produtos in cesto["produtos"]:
        cesto["total"] += produtos["preço_unitario"]
    return cesto

def gerar_cesto(stock, min_produtos, max_produtos):
    cesto = cria_cesto()
    tipos_fruta = random.randrange(min_produtos,max_produtos)
    for i in range(1,tipos_fruta + 1):
        if(i <= len(stock)-1):
            if(min_produtos < stock[i]["quantidade"] <= max_produtos):
                cesto["produtos"].append(stock[i])
    cesto["produtos"].pop(0)
    cesto = atualiza_total(cesto)
    return cesto
    
def ler_stock(ficheiro):
    stock = []
    ficheiro = open(ficheiro , "r", encoding='utf-8')
    linhas = ficheiro.read().splitlines()
    linhas.pop(0)
    ficheiro.close()   
    for row in linhas:
        row = row.split(";")
        dicionario = {"nome":row[0],"quantidade":int(row[1]),"preço_unitario":float(row[2])}
        stock.append(dicionario)
    return stock


def atualizar_stock(stock, cestos):
    for produto in cestos["produtos"]:
        # for produto in cesto["produtos"]:
        for i in stock:
                if(produto["nome"] == i["nome"]):
                    i["quantidade"] -= produto["quantidade"]
                    if(i["quantidade"] <= 0):
                        stock.remove(produto)
    return stock


if __name__ == "__main__":
    stock = ler_stock("stock.csv")
    cestos = gerar_cesto(stock,10,45)
    print("cestos: ",cestos,"\n")
    print(atualizar_stock(stock,cestos))