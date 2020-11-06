import math,sys

def menu():
    print("Menu")
    print("Selecione 1 - Formula Resolvente")
    print("Selecione 2 - Valor de Fibonacci de 2020")
    print("Selecione 9 - exit")
    o=str(input("Selecione uma opcao: "))
    menuoptions(o)
    
def menuoptions(o):
    if o == "1":
        print("Formula Resolvente")
        a=int(input("Insira o valor do a: "))
        b=int(input("Insira o valor do b: "))
        c=int(input("Insira o valor do c: "))
        fresolvente(a,b,c)
    if o == "2":
        print("Valor de Fibonacci de 2020: ")
        fibonacci_value(2020)
    if o == "9":
        return sys.exit(0)
    print("")
    return menu()

#Parte 5
#Exercicio 1
def fresolvente(a,b,c):
    delta=(math.pow(b,2)-(4*a*c))
    if(delta<0):
        print("Não se pode fazer raizes de números negativos")
        return menuoptions(1)
    else:
        positivo= (-b + math.sqrt(delta))/(2*a)
        negativo= (-b - math.sqrt(delta))/(2*a)
        if(positivo==negativo):
            print("O zero da função é: ",positivo)
        else:
           print("Os zeros da função são: ", positivo, " e ", negativo)
       
#Exercicio 2 (a) e (b)
#   Valor de Fibonacci de um número é a soma do valor de Fibonacci do número anterior com o
#valor de Fibonacci do penultimo número, matematicamente F(n)=F(n-1)+F(n-2)
#   Usando a fórmula acima podemos escrever F(n+1)= F(n) + F(n-1)
#   Isto serve para mostrar que para calcularmos o termo seguinte vamos usar os valores do termo
#anterior. Desta forma vamos precisar de 3 variáveis: 
#   Uma variável que contém o valor do último termo (ultimo_termo), outra que contém o valor
#do penultimo termo(penultimo_termo) e uma que contém o valor do termo atual(termo_atual)
#   Usando as formulas acima obtemos os cálculos que devemos fazer a cada iteração:
#   1. Calcular o termo atual com a soma dos dois ultimos termos
#   2. O penultimo termo do cálculo do próximo termo irá ser igual ao valor do ultimo termo
#       do cálculo do termo atual. 
#   3. O ultimo termo do cálculo do próximo termo irá ser igual ao valor do termo atual
#   Estes passos devem ser executados n vezes para obtermos o valor de F(n).
#   Uma vez que a formula matemática só funciona para n > 1 (pois F(0) e F(1) dão origem a n's 
#negativos) fizémos uma validação para se o n < 1 retorna o valor tabelado que é 1
#   Para os restantes n's > 1, como já foi dito, temos de fazer um ciclo que execute os
#passos 1,2 e 3 descritos acima. Este ciclo irá começar no n=2 que é o primeiro n acima de um
#e irá até n.
#   Como F(2)= F(0) + F(1) = 1+1, então iniciamos as variáveis ultimo_termo e penultimo_termo
#com o valor 1.
#

def fibonacci_value(n):
 ultimo_termo=1
 penultimo_termo=1
 if (n==0) or (n==1):
    print("1")
 else:
    for i in range(2,n):
        # Ponto 1
        termo_atual = ultimo_termo + penultimo_termo
        # Ponto 2
        penultimo_termo = ultimo_termo
        # Ponto 3
        ultimo_termo = termo_atual
    print(termo_atual)

menu()
