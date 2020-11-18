# import math
    
# print(math.factorial(20))


# def produtorio(n):
#     if(n==1):
#         return 1
#     else:
#         return n*produtorio(n-1)
    
    
# print(produtorio(10))


# PARTE 4 EX1
# lista= []
# for i in range (1, 4):
#     print("Insira um número", i,": " )
#     num = int(input())
#     lista.append(num)
# print("O valor máximo é", max(lista), "e o valor mínimo é", min(lista))


# PARTE 4 EX2
# def inverso (palavra):
#     inverso= ""
#     for char in range(len(palavra) - 1, -1, -1):
#          inverso += palavra[char]
#     return inverso


# def conta_vogais(palavra):
#     num_vogais=0
#     for char in palavra:
#         if char in "aeiouAEIOU":
#             num_vogais+=1
#     return num_vogais     
   
# palavra=input("Insira uma palavra: ")
# print("O inverso da palavra é",inverso(palavra),"e tem",conta_vogais(palavra),"vogais.")

# PARTE 4 EX3
# texto= input("Insira um texto: ")
# old= input("Identifique o carater a ser alterado: ")
# new= input("Identifique o carater para o qual quer alterar: ")

# print(texto.replace(old[0],new[0]))


