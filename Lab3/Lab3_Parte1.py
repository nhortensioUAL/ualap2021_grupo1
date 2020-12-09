def length(l):
    contador = 0
    for i in l:
        contador+=1
    return contador
    
def same_length(l1,l2):
    if(length(l1) == length(l2)):
        return True
    else:
        return False
    
def count_reps(l):
    lista_rep=[]
    for i in range(length(l)):
        for x in range(i+1,length(l)):
            if(l[i]==l[x] and l[x] not in lista_rep):
                lista_rep.append(l[x])
    return lista_rep
    
def clear_reps(l):
    lista = []
    for elemento in l:
        if(elemento not in lista):
            lista.append(elemento)
    return lista
    
    
    
