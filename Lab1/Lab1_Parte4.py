#(A)
#if 4 > 5:
#print("Correto")
"""A condição 4 > 5 nunca será verdade pois 4 nunca será maior que 5."""
if 4 < 5:
    print("Correto")

#(B)
#for i in range(10
#print i+1
"""Existem erros de sintaxe: falta de parentesis na expressão 'print',
na expressão 'for' falta fechar parentesis e acrescentar dois pontos ao final."""
for i in range(10):
    print (i+1)

#(C)
#a = 0
#while a < 10):
#    a = 1
"""De modo que 'a' sempre será igual a 1, a condição a < 10 nunca será verdade
Também há erro de sintaxe pois falta abrir parentesis na expressão 'while'."""
a = 0
while (a < 10):
    a += 1

#(D)
#a = 1
#b = 5
#while true:
#   if a = b
#       a =+ 1
#   else:
#       print{"Feito"}
"""Existem erros de sintaxe: o indicador booleano 'True' deve ser escrito
com a letra inicial maiúscula. A expressão 'if' deve ter dois pontos ao
final. O argumento da expressão 'print' é delimitado por '()' em vez de '{}'.
Existe uma redundância no if e no else que dão origem a um ciclo infinito, portanto
devemos por a instrução 'break' no 'else' para indicar que queremos parar o ciclo assim que
acharmos um a==b."""
a = 1
b = 5
while True:
   if a == b:
       a =+ 1
   else:
        print("Feito")
        break


#(E)
#Soma dois números inteiros.
#def sum(a b):
#Return a + b
"""Existem erros de sintaxe: a função soma deve ter dois valores separados
por vírgula. A expressão 'return' deverá ser escrita toda em letras minúsculas."""
def sum(a,b):
    return (a + b)


#(F)
# Compara dois número inteiros.
#Def compare(a, b)
#if[a == b]
#return TRUE
"""Existem erros de sintaxe: a expressão 'def' deverá ser sempre escrita toda
em letras minúsculas. Faltam ':' ao final da função 'def compare' e do 'if'
A expressão 'if' deverá ser delimitado por parentesis. A expressão 'True' não
deve ser escrita toda em letras maiúsculas."""
def compare(a,b):
    if (a == b):
        return True