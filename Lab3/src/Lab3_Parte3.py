# Parte 3

l=[20, "Nuno", 8.3, 7, "Ricardo", 5.6, 4, "Ana"]


def only_string(l):
    lista = []
    for elemento in l:
        if(isinstance(elemento, str)):
            lista.append(elemento)
    return lista

print("A lista contém as seguintes strings:", only_string(l))


def int_average(l):
    soma = 0
    nr_elementos = 0
    for elemento in l:
        if(isinstance(elemento, int)):
            soma += elemento
            nr_elementos += 1
    return (soma / nr_elementos)

print("A média dos valores inteiros da lista é:", int_average(l))


def round_floats(l):
    for i in range (len(l)):
        if(isinstance(l[i], float)):
            l[i] = int(l[i])
    return l
            
print("A lista com valores decimais arredondados é:", round_floats(l))