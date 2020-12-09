def sum_extremes(l):
    return l[0] + l[-1]

def print_list(l):
    for elemento in l:
        print(elemento, end="\n")
        
def sort_list(l, descend=False):
    lista = []
    if(descend==False):
        for i in range (len(l)):
            lista.append(min(l))
            l.remove(min(l))
    else:
        for i in range(len(l)):
            lista.append(max(l))
            l.remove(max(l))
    return lista

def min_max(l):
    lista = []
    minimo = l[0]
    maximo = l[0]
    for elemento in l:
        if(elemento < minimo):
            minimo = elemento
        elif(elemento > maximo):
            maximo = elemento
    lista.append(minimo)
    lista.append(maximo)
    return lista

def sum_positions(l1, l2):
   lista_soma = []
   nr_iteracoes = 0
   if(len(l1) < len(l2)):
       nr_iteracoes= len(l1)
   else:
        nr_iteracoes= len(l2)   
   for i in range(nr_iteracoes):
       lista_soma.append(l1[i] + l2[i])
   return lista_soma    
       
def append_positions(l1, l2):
   lista_intercala = []
   lista = []
   nr_iteracoes = 0
   if(len(l1) < len(l2)):
       nr_iteracoes = len(l1)
   else:
        nr_iteracoes = len(l2) 
   for i in range(nr_iteracoes):
        lista.append(l1[i])
        lista.append(l2[i])
   for i in range(nr_iteracoes):
        lista_intercala.append(lista[i])
   return lista_intercala
        
