def only_string(l):
    lista = []
    for elemento in l:
        if(isinstance(elemento,str)):
            lista.append(elemento)
    return lista


def int_average(l):
    soma = 0
    nr_elementos = 0
    for elemento in l:
        if(isinstance(elemento,int)):
            soma += elemento
            nr_elementos +=1
    return (soma/nr_elementos)

def round_floats(l):
    for i in range (len(l)):
        if(isinstance(l[i],float)):
            l[i] = int(l[i])
    return l
            
