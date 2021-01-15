# Parte 4 
# Exercício 1

lista= []
for i in range (1, 4):
    print("Insira um número", i,": " )
    num = int(input())
    lista.append(num)

print("O valor máximo é", max(lista), "e o valor mínimo é", min(lista))

# Parte 4 
# Exercício 2

def inverso (palavra):
    inverso= ""
    for char in range(len(palavra) - 1, -1, -1):
        inverso += palavra[char]
    return inverso

def conta_vogais(palavra):
    num_vogais=0
    for char in palavra:
        if char in "aeiouAEIOU":
            num_vogais += 1
    return num_vogais     
   
palavra=input("Insira uma palavra: ")
print("O inverso da palavra é", inverso(palavra), "e tem", conta_vogais(palavra), "vogais.")

# Parte 4 
# Exercício 3

def sub_caracter(texto, old_carac, new_carac):
   novo_texto =''
   for i in range (0, len(texto)):
       if(texto[i] == old_carac):
           novo_texto += new_carac
       else:
           novo_texto += texto[i]
   return novo_texto

texto=input("Escreva o texto: ")
old=input("Identifique o carater a ser alterado: ")
new=input("Identifique o carater para o qual quer alterar: ")    
    
print(sub_caracter(texto, old, new))