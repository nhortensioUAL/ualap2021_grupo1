# Parte 1


l=["Ana", 2, 3, 4, 5, 5, 4, "Ana"]
l2=["Ricardo", 2, 3, 4, 5, 5, 4, 3]


def length(l):
    contador = 0
    for i in l:
        contador += 1
    return contador

print("O tamanho da lista é", length(l))
    

def same_length(l, l2):
    if(length(l) == length(l2)):
        return True
    else:
        return False
    
print("As listas têm o mesmo tamanho: ", same_length(l, l2))


def count_reps(l):
    lista_rep=[]
    for i in range(length(l)):
        for x in range(i + 1, length(l)):
            if(l[i] == l[x] and l[x] not in lista_rep):
                lista_rep.append(l[x])
    return lista_rep

print("A lista tem as seguintes repetições: ", count_reps(l))


def clear_reps(l):
    lista = []
    for elemento in l:
        if(elemento not in lista):
            lista.append(elemento)
    return lista

print("Os valores da lista sem repetições são: ", clear_reps(l))