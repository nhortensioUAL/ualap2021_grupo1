
# Função que escreve a lista num ficheiro
def escreve_ficheiro(lista,nome_ficheiro):
    ficheiro = open (nome_ficheiro + ".txt", "w")
    for i in lista:
     ficheiro.write(str(i))
    ficheiro.close()


# Função que lÊ os dados de um ficheiro
def ler_ficheiro (lista,nome_ficheiro):
    ficheiro= open(nome_ficheiro + ".txt", "r")
    linhas = list(ficheiro)
    for i in linhas:
        lista_alunos.append(i)
    ficheiro.close()
  
    
# Função que valida se aluno já foi registado
def existe_aluno (lista,r_aluno):
    for i in lista:
        if(i[0]==nr_aluno):
            return True
    return False
     

# Função que valida se o momento de avaliação já foi registado      
def existe_avaliacao (lista, nr_aluno, momento):
    for i in lista:
        if(i[0]==nr_aluno):
            for j in i:
                if(j==momento):
                    return True
    return False


# Função que regista um aluno na lista
def registar_aluno (lista,nr_aluno,nome):
    lista_aux=[nr_aluno,nome]        
    lista.append(lista_aux)


# Função que regista a nota de um determinado momento de avaliação
def regista_nota (lista,nr_aluno,momento,valor):
    for i in range(len(lista)):
        if(lista[i][0]==nr_aluno):
            lista[i].append(momento)
            lista[i].append(valor)
            print("Nota registada com sucesso!")
            break
        else:
            print("Aluno não registado.")
        
        
# Função que faz a alteração da nota de um determinado momento de avaliação        
def alterar_nota (lista,nr_aluno,momento,valor):
        for i in range(len(lista)):
            if(lista[i][0]==nr_aluno):
                for j in range (len(lista[i])):
                    if(lista[i][j]==momento):
                        lista[i][j+1] = valor  
                        print("Nota alterada com sucesso!")
  
    
# Função que retorna as notas de todos os momentos de avaliação para um determinado aluno
def get_grades (lista,nr_aluno):
  t1 = 0
  t2 = 0
  proj = 0  
  contador_notas = 0
  for i in range(len(lista)):
      if(lista[i][0]==nr_aluno):
          for j in range (len(lista[i])):
              if(lista[i][j]=="T1"):
                  t1= lista[i][j+1]
                  contador_notas += 1
              elif(lista[i][j]=="T2"):
                  t2= lista[i][j+1]
                  contador_notas += 1
              elif(lista[i][j]=="P"):
                  proj = lista[i][j+1]
                  contador_notas += 1
  if(contador_notas != 3):
      print("Ainda não foram inseridos todos os momentos de avaliação.")
  else:
     return t1,t2,proj                                                           
        

# Função que calcula a media do aluno consoante as notas de todos os momentos de avaliação          
def calcula_media(nr_aluno,notas):
    nota_testes = (notas [0] + notas [1]) * 0.4
    nota_projeto = notas [2] * 0.6
    media = nota_testes + nota_projeto
    if(media > 21):
        media=20
    return media
   

# Menu principal                    
def menu_principal():
    print("\n", "Menu", "\n")
    print(" ","R  - Registar aluno")    
    print(" ","RM - Registar avaliação")
    print(" ","AM - Alterar avaliação")
    print(" ","CM - Calcular média")
    print(" ","G  - Guardar informação")
    print(" ","L  - Ler informação")
    print(" ","S  - Sair")
    
    
 # Menu dos momentos de avaliação   
def menu_RM():
    print(" ", "T1 - Primeiro teste")
    print(" ", "T2 - Segundo teste")
    print(" ", "P  - Projeto")
    print(" ", "S  - Menu principal")



if __name__ == "__main__":
    lista_alunos = []
    while True:
        menu_principal()
        comando = input( "Indique a instrução: ")
        comando = comando.split()
        if(comando[0] == "R"):
            nr_aluno=input("Insira o número do aluno: ")
            if(existe_aluno(lista_alunos,nr_aluno)):
                print("Aluno já registado.", "\n")
            else:    
                nome=input("Insira o nome do aluno: ")
                registar_aluno(lista_alunos,nr_aluno,nome)
                print ("Aluno registado com sucesso!", "\n")
        elif(comando[0] == "RM"):
          nr_aluno=input("Insira o número do aluno: ")
          while True:
              menu_RM()
              momento=input("Insira o momento de avaliação: ")
              if(existe_avaliacao(lista_alunos,nr_aluno,momento)):
                  print("Momento de avaliação já registado.", "\n")
              elif(momento == "S"):
                  break
              else:    
                  if(momento == "T1" or momento== "T2" or momento == "P"):
                      valor =round(float(input("Insira a nota: ")),1)
                      if(0 <= valor < 21):
                          regista_nota(lista_alunos,nr_aluno,momento,valor)
                          break
                      else:
                          print("Nota inválida. A nota terá que ser entre 0 e 20 com uma casa decimal.", "\n")
                  else:
                      print("Instrução inválida.", "\n")
        elif(comando[0] == "AM"):
            nr_aluno = input("Insira o número do aluno: ")
            momento = input("Insira o momento de avaliação: ")
            valor = round(float(input("Insira a nota: ")),1)
            alterar_nota(lista_alunos,nr_aluno,momento,valor)
        elif(comando[0] == "CM"):
            nr_aluno = input("Insira o número do aluno: ")  
            media = calcula_media(nr_aluno,get_grades(nr_aluno))
            print("A média do aluno", nr_aluno, "é: ", media)
        elif(comando[0] == "G"):
            nome_ficheiro = input("Indique qual o nome pretendido para o ficheiro: ")
            escreve_ficheiro(lista_alunos,nome_ficheiro)    
        elif(comando[0] == "L"):
            nome_ficheiro = input("Indique qual o nome do ficheiro: ")
            ler_ficheiro(lista_alunos,nome_ficheiro)
            print(lista_alunos)
        elif(comando[0] == "S"):
            break    
    
