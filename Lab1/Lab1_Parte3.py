# -*- coding: utf-8 -*-
import sys,math

def menu():
    print("Menu")
    print("Selecione 1 - Area do rectangulo")
    print("Selecione 2 - Area do Trapezio")
    print("Selecione 3 - Area do Triangulo")
    print("Selecione 9 - exit")
    o=str(input("Selecione uma opcao: "))
    menuoptions(o)
    
def menuoptions(o):
    if o == "1":
        print("Area do Rectangulo")
        base=int(input("Insira o valor da base: "))
        altura=int(input("Insira o valor da altura: "))
        print("Area: ",arearect(base,altura))
    if o == "2":
        print("Area do Trapezio")
        base=int(input("Insira o valor da base maior: "))
        basemenor=int(input("Insira o valor da base menor: "))
        altura=int(input("Insira o valor da altura: "))
        print("Area: ",areatrapezio(base,basemenor,altura))
    if o == "3":
        print("Area do Triangulo Escaleno")
        a=int(input("Insira o valor de um dos lado 1: "))
        b=int(input("Insira o valor de um dos lado 2: "))
        c=int(input("Insira o valor de um dos lado 3: "))

        print("Area: ",areatriangulo(a,b,c))
    if o == "9":
        return sys.exit(0)
    print("")
    return menu()

def areatrapezio(base,basemenor,altura):
	area=(base+basemenor)*altura/2
	return area

def arearect(base,altura):
	area=base*altura
	return area

def areatriangulo(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

menu()
