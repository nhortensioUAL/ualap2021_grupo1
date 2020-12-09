
# Função que escreve a lista num ficheiro
def escreve_ficheiro(lista,nome_ficheiro):
    ficheiro = open (nome_ficheiro + ".txt", "w")
    for i in lista:
        for z in i:
            ficheiro.write(str(z) + ",")
        ficheiro.write("\n")
    ficheiro.close()


# Função que lê os dados de um ficheiro
def ler_ficheiro (lista,nome_ficheiro):
    ficheiro= open(nome_ficheiro + ".txt", "r")
    linhas = ficheiro.readlines()
    for row in linhas:
        row = row.split(",")
        if(row[0] != "\n" ):
            if(ja_existe(lista,row[0])):
                pass
            else:
                row.pop(-1)
                lista.append(row) 
    ficheiro.close()
    
    
def ja_existe(lista,nr_aluno):
    for i in lista:
        if(int(i[0]) == nr_aluno):
            return True
        else:
            return False
    
    
# Função que valida se aluno já foi registado
def existe_aluno (lista,r_aluno):
    for i in lista:
        if(int(i[0])==nr_aluno):
            return True
    return False
     

# Função que valida se o momento de avaliação já foi registado      
def existe_avaliacao (lista, nr_aluno, momento):
    for i in lista:
        if(int(i[0])==nr_aluno):
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
        if(int(lista[i][0])==int(nr_aluno)):
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
  for i in range(len(lista)):
      if(int(lista[i][0]) == int(nr_aluno)):
          for j in range (len(lista[i])):
              if(lista[i][j]=="T1"):
                  t1= float(lista[i][j+1])
              elif(lista[i][j]=="T2"):
                  t2= float(lista[i][j+1])
              elif(lista[i][j]=="P"):
                  proj = float(lista[i][j+1])
  return t1,t2,proj 
                                                        
        
# Função que calcula a media do aluno consoante as notas de todos os momentos de avaliação          
def calcula_media(notas):
    nota_testes = (notas [0] * 0.2) + (notas[1] * 0.2)
    nota_projeto = notas [2] * 0.6
    media = nota_testes + nota_projeto
    if(media > 20):
        media = 20
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
                print(lista_alunos)
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
            notas = get_grades(lista_alunos,nr_aluno)
            if(None in notas):
                media = calcula_media(notas)
                print("A média do aluno", nr_aluno, "é: ", media)
            else:
                print("Ainda não foram inseridos todos os momentos de avaliação.")   
        elif(comando[0] == "G"):
            nome_ficheiro = input("Indique qual o nome pretendido para o ficheiro: ")
            escreve_ficheiro(lista_alunos,nome_ficheiro)    
        elif(comando[0] == "L"):
            nome_ficheiro = input("Indique qual o nome do ficheiro: ")
            ler_ficheiro(lista_alunos,nome_ficheiro)
            print(lista_alunos)
        elif(comando[0] == "S"):
            break    
    
