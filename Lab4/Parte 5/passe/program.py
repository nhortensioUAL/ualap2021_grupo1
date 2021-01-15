from datetime import date
from dateutil.relativedelta import *   

def existe_escalao(escalao):
    escaloes = ["Normal", "Social B", "Social A", "Sub23"]
    if((escalao.capitalize()) in escaloes):
        return True
    else:
        return False

def existe_tipo_passe(tipo_passe):
    tipos_passe = ["Metropolitano", "Municipal Lisboa", "Municipal Amadora",
                "Municipal Odivelas","-12","+65"]
    if((tipo_passe.capitalize()) in tipos_passe):
        return True
    else:
        return False
    

def regista_cliente(clientes, nome,nif,idade,escalao,saldo_disponivel):
    tmp = {"nome": nome, "nif": nif, "idade":idade, "escalao":escalao,
           "saldo_disponivel":saldo_disponivel,"tipo_passe":"Nenhum", "validade":date(2999,12,31)}
    clientes.append(tmp)
    print("Cliente registado com sucesso!")
    return clientes

def adquirir_passe(clientes,nif,tipo_passe,precos):
    validade_temporal = obter_validade_temporal(precos,tipo_passe)
    validade_espacial = obter_validade_espacial(precos,tipo_passe)
    for cliente in clientes:
        if(cliente["nif"] == nif):
            preco = obter_preco(precos, tipo_passe, cliente["escalao"])
            if(tipo_passe == "-12"):
                if (int(cliente["idade"]) > 12):
                    print("Não apresenta os requisitos necessários para adquirir este passe.")
            elif(tipo_passe == "+65"):
                if(int(cliente["idade"]) < 65):
                    print("Não apresenta os requisitos necessários para adquirir este passe.")
            else:
                if(int(cliente["saldo_disponivel"]) - preco < 0):
                    print("Saldo insuficiente.")
                else:
                    cliente["saldo_disponivel"] = int(cliente["saldo_disponivel"]) - preco
                    cliente["tipo_passe"] = tipo_passe
                    cliente["validade"] = date.today() + dateutil.relativedelta(months=validade_temporal)
                    print(preco, validade_espacial, cliente["validade"])

def ver_validade(clientes,nif):
    for cliente in clientes:
        if(cliente["nif"] == nif):
            if(cliente["validade"] <= date.today()):
                return cliente["tipo_passe"], cliente["validade"]
            else:
                print("Data de validade expirada.")

def guardar_ficheiro(clientes,ficheiro):
    file = open(ficheiro, "w")
    for cliente in clientes:
        for value in cliente:
            file.write(str(cliente.get(value)))
            file.write(";")
    file.close()        

def ler_ficheiro(clientes,ficheiro):
    file = open(ficheiro, "r", encoding = 'utf-8')
    rows = file.readlines()
    for line in rows:
        line = line.split(";")
        tmp ={"nome": line[0], "nif": int(line[1]), "idade":int(line[2]), "escalao":line[3],
           "saldo_disponivel":float(line[4]),"tipo_passe":line[5], "validade":line[6]}
        clientes.append(tmp)
    file.close()
    return clientes

