def menu():
   print("\n", "Menu", "\n")
   print(" ","LS - Listar séries alfabeticamente.")    
   print(" ","LT - Listar séries por intervalo de anos.")
   print(" ","LR - Listar séries por ranking.")
   print(" ","LG - Listar séries por género")
   print(" ","S  - Sair")


# Função que faz a leitura do ficheiro
def le_ficheiro():
    lista_series=[]
    linhas=[]
    ficheiro = open("imdb.txt", "r", encoding='utf-8')
    linhas = ficheiro.read().splitlines()
    for i in linhas:
        lista_series.append(i.split(";"))
    lista_series.pop(0)
    ficheiro.close()
    return lista_series


# Função que lista as séries por ordem alfabética
def listar_series_alf(lista):
    lista.sort()
    for i in lista:
        print(i)
   
    
# Função que ordena uma lista por ranking
def ordenar_ranking(lista):
  valor = 0
  for i in range (len(lista)):
     if(i < len(lista) -1 ):
         if(lista[i][3] < lista [i+1][3]):
             valor == lista[i][3]
             lista[i][3] == lista[i+1][3]
             lista[i+1][3] == valor           
  return lista


# Função que lista as séries por intervalo de anos
def listar_series_interval(lista,ano_inicial,ano_final):
    lista = ordenar_ranking(lista)
    for i in lista:
        if(ano_inicial <= i[2] <= ano_final):
            print(i)


# Função que lista as séries por ranking
def listar_series_ranking(lista,ranking):
    lista= ordenar_ranking(lista)
    for i in lista:
        if(float(i[3]) >= ranking):
            print(i)    
    
    
# Função que lista as séries por género    
def listar_series_gen(lista,ranking,genero):
    lista_aux = []
    for i in lista:
        if(i[1] == genero):
              lista_aux.append(i)                   
    listar_series_ranking(lista_aux,ranking)


# Função que faz as validações necessárias ao input de "anos"
def validacoes_anos(ano_inicial,ano_final):
    if(len(ano_final) != 4 or len(ano_inicial) != 4):
        return False
    elif(ano_final < ano_inicial):
        return False
    else:
        return True
    

# Função que faz as validações necessárias ao input "ranking"
def validacoes_ranking(ranking):
    if( 0 < float(ranking) < 10):
        return True
    else:
        return False


# Função que converte o input "ranking" num número com uma casa decimal
def converter_ranking(ranking):
    return round(ranking,1)



if __name__ == "__main__":
    lista_series = le_ficheiro()
    while True:
        menu()
        comando = input("Indique a opção que pretende executar: ").split()
        if(comando[0].upper() == "LS"):
            listar_series_alf(lista_series)
        elif(comando[0].upper() == "LT"):
            ano_inicial = input("Insira o ano inicial: ")
            ano_final = input("Insira o ano final: ")
            if(validacoes_anos(ano_inicial,ano_final)):
                listar_series_interval(lista_series,ano_inicial,ano_final)
            else:
                print("Ano inválido!")
        elif(comando[0].upper() == "LR"):
            ranking = converter_ranking(float(input("Indique o ranking pretendido(0.0-10.0): ")))
            if(validacoes_ranking(ranking)):
                listar_series_ranking(lista_series,ranking)
        elif(comando[0].upper() == "LG"):
            ranking_min = converter_ranking(float(input("Indique o ranking mínimo: ")))
            genero = input("Indique o género da série: ")
            if(validacoes_ranking(ranking_min)):
                listar_series_gen(lista_series,ranking_min,genero)
        elif(comando[0].upper() == "S"):
            break