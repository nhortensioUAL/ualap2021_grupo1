# Parte 2
# Exercício 1

def factorial(numero):
    resultado_factorial = 1 
    for i in range(1, numero + 1):
        resultado_factorial = resultado_factorial * i
    return resultado_factorial
    
print("O factorial é", factorial(20))
# Parte 2
# Exercício 2

def produtorio(numero):
    if(numero == 1):
        return 1
    else:
        return numero * produtorio(numero - 1)
   
print("O produtório é", produtorio(50))