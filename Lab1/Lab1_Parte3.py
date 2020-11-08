import sys,math

def menu():
    print("Menu")
    print("Selecione 1 - Área do Rectângulo")
    print("Selecione 2 - Área do Trapézio")
    print("Selecione 3 - Área do Triângulo")
    print("Selecione 9 - Sair")
    opcao = str(input("Selecione uma opção: "))
    menuoptions(opcao)
    
def menuoptions(opcao):
    if opcao == "1":
        print("Área do Rectângulo")
        base = int(input("Insira o valor da base: "))
        altura = int(input("Insira o valor da altura: "))
        print("Área: ", area_rectangulo(base, altura))
    if opcao == "2":
        print("Área do Trapézio")
        base_maior = int(input("Insira o valor da base maior: "))
        base_menor = int(input("Insira o valor da base menor: "))
        altura = int(input("Insira o valor da altura: "))
        print("Área: ", area_trapezio(base_maior, base_menor, altura))
    if opcao == "3":
        print("Área do Triângulo")
        lado_a = int(input("Insira o valor de um dos lado A: "))
        lado_b = int(input("Insira o valor de um dos lado B: "))
        lado_c = int(input("Insira o valor de um dos lado C: "))

        print("Área: ",3 area_triangulo(lado_a, lado_b, lado_c))
    if opcao == "9":
        return sys.exit(0)
    print("")
    return menu()

def area_trapezio(base_maior, base_menor,altura):
	area = (base_maior + base_menor) * altura / 2
	return area

def area_rectangulo(base, altura):
	area = base * altura
	return area

def area_triangulo(lado_a, lado_b, lado_c):
    s = (lado_a + lado_b + lado_c) / 2
    area = math.sqrt(s * (s - lado_a) * (s - lado_b) * (s - lado_c))
    return area

menu()
