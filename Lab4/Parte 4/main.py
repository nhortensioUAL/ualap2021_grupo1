from frutaria import *

if __name__ == "__main__":
    stock = ler_stock("stock.csv")
    print("stock inicial", stock, "\n")
    cesto = gerar_cesto(stock,1,6)
    print("Cesto:", cesto, "\n")    
    stock = atualizar_stock(stock,cesto)
    print("Stock atualizado", stock, "\n")