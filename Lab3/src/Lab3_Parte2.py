# Parte 2


l=[20, 10, 8, 7, 6, 5, 4, 1]
l2=[1, 4, 5, 6, 7, 8, 10, 20]


def sum_extremes(l):
    return l[0] + l[-1]

print("A soma do primeiro e último elemento da lista é", sum_extremes(l))


def print_list(l):
    print("Os valores da lista são:", end="\n")
    for elemento in l:
        print(elemento, end="\n")

print_list(l)


def sort_list(l, descend=False):
    lista = l.copy()
    if(descend == False):
     for i in range (len(lista)-1):
      for j in range (len(lista)-1-i):
         if(lista[j] > lista [j+1]):
             tmp = lista[j]
             lista[j] = lista[j+1]
             lista[j+1] = tmp    
    else:
     for i in range (len(lista)-1):
      for j in range (len(lista)-1-i):
         if(lista[j] < lista [j+1]):
             tmp = lista[j]
             lista[j] = lista[j+1]
             lista[j+1] = tmp   
    return lista

print("A lista ordenada é:", sort_list(l))


def min_max(l):
    print(l)
    minimo = l[0]
    maximo = l[0]
    lista = []
    for elemento in l:
        if(elemento < minimo):
            minimo = elemento
        elif(elemento > maximo):
            maximo = elemento
    lista.append(minimo)
    lista.append(maximo)
    return lista

print("Os valores mínimo e máximo da lista são:", min_max(l))


def sum_positions(l, l2):
   lista_soma = []
   nr_iteracoes = 0
   if(len(l) < len(l2)):
       nr_iteracoes= len(l)
   else:
        nr_iteracoes= len(l2)   
   for i in range(nr_iteracoes):
       lista_soma.append(l[i] + l2[i])
   return lista_soma    
       
print("O valor da soma das listas para cada posição é:", sum_positions(l, l2))    


def append_positions(l, l2):
   lista_intercala = []
   lista = []
   nr_iteracoes = 0
   if(len(l) < len(l2)):
       nr_iteracoes = len(l)
   else:
        nr_iteracoes = len(l2) 
   for i in range(nr_iteracoes):
        lista.append(l[i])
        lista.append(l2[i])
   for i in range(nr_iteracoes):
        lista_intercala.append(lista[i])
   return lista_intercala
        
print("O resultado das listas intercalado é:", append_positions(l, l2))    