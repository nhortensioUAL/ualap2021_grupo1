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
        cesto["total"] += (produtos["preco_unitario"]*produtos["quantidade"])
    return cesto

def ler_stock(ficheiro):
    stock = []
    ficheiro = open(ficheiro , "r", encoding='utf-8')
    linhas = ficheiro.read().splitlines()
    linhas.pop(0)
    ficheiro.close()   
    for row in linhas:
        row = row.split(";")
        dicionario = {"nome":row[0],"quantidade":int(row[1]),"preco_unitario":float(row[2])}
        stock.append(dicionario)
    return stock

def gerar_cesto(stock, min_produtos, max_produtos):
    cesto = cria_cesto()
    tipos_fruta = random.randrange(min_produtos,max_produtos)
    for i in range(0,tipos_fruta + 1):
        if(i <= len(stock)-1):
            tmp = {}
            qtd_fruta = random.randrange(min_produtos,max_produtos)
            tmp["nome"] = stock[i]["nome"]   
            tmp["quantidade"] = qtd_fruta
            tmp["preco_unitario"] = stock[i]["preco_unitario"]   
            cesto["produtos"].append(tmp)
    cesto["produtos"].pop(0)
    cesto = atualiza_total(cesto)
    return cesto

def atualizar_stock(stock, cestos):
    for produto in cestos["produtos"]:
        for i in stock:
                if(produto["nome"] == i["nome"]):
                    i["quantidade"] -= produto["quantidade"]
                    if(i["quantidade"] <= 0):
                        stock.remove(produto)
    return stock
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    