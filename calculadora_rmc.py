import cmath
import numpy as np
import matplotlib.pyplot as plt
import math

a = 0
b = 0
c = 0
x = 0
x1 = 0
x2 = 0
conjuntoA = []
conjuntoB = []

def conjunto_numerico():
    itensA = int(input("Quantos elementos tem no conjunto A? ")) 
    itensB = int(input("Quantos elementos tem no conjunto B? "))
    
    for c in range(0,itensA):
            conjA = int(input("\nDigite o número do conjunto A: "))
            conjuntoA.append(conjA)
    for i in range(0,itensB):
        conjB = int(input("\nDigite o número do conjunto B: "))
        conjuntoB.append(conjB)

    while True:
        print("\nEscolha a opção que deseja fazer: \n\n[1] Verificar se A é subconjunto próprio de B\n[2] Realizar operação de União\n[3] Calcular intersecção\n[4] Calcular diferença\n[5] Recomeçar(Menu principal)")
        escolhaC = int(input("\nDigite a opção que deseja utilizar: "))

        if escolhaC <= 0 or escolhaC >= 6:
            print("Você digitou opção inexistente, escolha outra opção!")
            continue
        elif escolhaC == 5:
            for y in range(0,len(conjuntoA)):
                conjuntoA.pop()
            for z in range(0, len(conjuntoB)):
                conjuntoB.pop()   
            print("Você voltou ao menu principal!\n\n")
            break
        elif escolhaC == 1:
            if conjuntoA < conjuntoB and conjuntoA != conjuntoB:
                print("A é subconjunto próprio de B")
            else:
                print("A não é subconjunto próprio de B")
        elif escolhaC == 2:    
            j = conjuntoA | conjuntoB
            print(f"A união de A e B é: {j}")
        elif escolhaC == 3:
            d = conjuntoA & conjuntoB
            print(f"A intersecção de A e B é: {d}")
        elif escolhaC == 4:
            e = conjuntoB - conjuntoA
            print(f"A diferença de A e B é: {e}")

def funcao_segundo_grau():

    while True:
        print("\nEscolha a opção que deseja fazer: \n\n[1] Calular raízes\n[2] Calcular função em x pedido\n[3] calcular vértice\n[4] Gerar gráfico\n[5] Recomeçar(Menu principal)")
        
        escolhaF = int(input("\nDigite a opção que deseja utilizar: "))
        
        if escolhaF <= 0 or escolhaF >= 6:
            print("Você digitou opção inexistente, escolha outra opção!\n")
            continue
        elif escolhaF == 5:
            a=0
            b=0
            c=0
            delta = 0
            xv = 0
            yv = 0
            x = 0
            y = 0
            print("Você voltou ao menu principal!")
            break

        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))

        delta = b**2 - 4*a*c
        xv = -b//2*a
        yv = -delta//4*a

        if escolhaF == 1:
            if  delta < 0:
                x1 = (-b + cmath.sqrt(delta)) / (2*a)
                x2 = (-b - cmath.sqrt(delta)) / (2*a)
                raizes = (x1, x2)
                print(f"A raíz da função é: {raizes}")#nao entendi o que é para fazer nas complexas, perguntar
            elif delta == 0:
                x1 = -b / (2*a)
                raizes = (x1)
                print(f"A raíz da função é: {raizes}")
            else:
                x1 = (-b + cmath.sqrt(delta)) / (2*a)
                x2 = (-b - cmath.sqrt(delta)) / (2*a)
                raizes = (x1, x2)
                print(f"As raízes da função é: {raizes}")
        elif escolhaF == 2:
            x = int(input("Digite o valor de x: "))
            funcao = a * x**2 + b * x + c
            print(f"f(x) = {funcao}")
        elif escolhaF == 3:
            if a > 0:
                print(f"Xv = {xv}, Yv = {yv}, sendo valor mínimo")
            elif a < 0:
                print(f"Xv = {xv}, Yv = {yv}, sendo valor máximo")
        elif escolhaF == 4:
            x = np.linspace(-300, 60, 400)
            y = a * x**2 + b * x + c            
            plt.plot(x, y, label = f" {a}x^2 + {b}x + {c}")
            plt.title(f"Função do segundo grau: {a}x^2 + {b}x + {c}")
            plt.xlabel("Eixo X")
            plt.ylabel("Eixo Y")
            plt.grid(True)
            plt.legend()
            plt.axhline(y=0,color='black')
            plt.axvline(x=0,color='black')
            plt.show()  

def funcao_exponecial():
     while True:
        print("\nEscolha a opção que deseja fazer: \n\n[1] Verificar se é crescente ou decrescente\n[2] Calcular função em x pedido\n[3] Gerar gráfico\n[4] Recomeçar(Menu principal)\n")
        
        escolhaFE = int(input("\nDigite a opção que deseja utilizar: "))

        if escolhaFE <= 0 or escolhaFE >= 5:
            print("Você digitou opção inexistente, escolha outra opção!\n")
            continue
        elif escolhaFE == 4:
            a = 0
            b = 0
            x = 0
            y = 0
            print("Você voltou ao menu principal!")
            break

        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        
        if b == 0:
            print("A função não existe\n")
            continue
        elif escolhaFE == 1:
            if b > 0 and b != 1:
                if b > 1:
                    print("A função é crescente")
                elif 0 < b < 1:
                    print("A função é decrescente")
                else:
                    print("A função não é certeza se é crescente ou decrescente")
            elif b == 1:
                print("A função é linear")
            elif b < 0:
                print("A função exponencial so vai existir se X for inteiro")
        elif escolhaFE == 2:
            x = int(input("Digite o valor de x: "))
            funcaoEX = a * b**x
            print(f"f(x) = {funcaoEX}")
        elif escolhaFE == 3:
            x = np.linspace(-10, 10, 400)
            y = a * b ** x            
            plt.plot(x, y, label = f" {a}x{b}^X")
            plt.title(f"Função exponencial: {a}x{b}^X")
            plt.xlabel("Eixo X")
            plt.ylabel("Eixo Y")
            plt.grid(True)
            plt.legend()
            plt.axhline(y=0,color='black')
            plt.axvline(x=0,color='black')
            plt.show() 

def matrizes():
     while True:
        print("\nEscolha a opção que deseja fazer: \n\n[1] Determinante (2X2 ou 3x3)\n[2] Multiplicação\n[3] Matriz transposta\n[4] Recomeçar(Menu principal)\n")

        escolhaMA = int(input("\nDigite a opção que deseja utilizar: "))

        if escolhaMA <= 0 or escolhaMA >= 5:
            print("Você digitou opção inexistente, escolha outra opção!\n")
            continue
        elif escolhaMA == 4:
            num_colunas = 0
            num_linhas = 0
            num_colunas2 = 0
            num_linhas2 = 0
            elementos = 0
            determinante = 0
            for y in range(0,len(matriz)):
                matriz.pop()
            for z in range(0, len(linhas)):
                linhas.pop() 
            for x in range(0,len(matriz2)):
                matriz2.pop()
            for z in range(0, len(linhas2)):
                linhas2.pop() 
            for y in range(0,len(matriz_transposta)):
                matriz_transposta.pop() 
            print("Você voltou ao menu principal!")
            break

        num_linhas = int(input("Digite o número de linhas: "))
        num_colunas = int(input("Digite o número de colunas: "))

        matriz = []

        for i in range(num_linhas):
            linhas = []
            for j in range(num_colunas):
                elementos = int(input(f"Informe o elemento da posição A{i},{j}: "))
                linhas.append(elementos)
            matriz.append(linhas)
        print("A matriz é:")
        for linha in matriz:
            print(linha)
        
        if escolhaMA == 1:
            if num_linhas == 2 and num_colunas == 2:
                determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
                print(f"A determinante da Matriz é: {determinante}")
            elif num_linhas == 3 and num_colunas == 3:
                determinante = (matriz[0][0] * matriz[1][1] * matriz[2][2] +
                        matriz[0][1] * matriz[1][2] * matriz[2][0] +
                        matriz[0][2] * matriz[1][0] * matriz[2][1] -
                        matriz[0][2] * matriz[1][1] * matriz[2][0] -
                        matriz[0][1] * matriz[1][0] * matriz[2][2] -
                        matriz[0][0] * matriz[1][2] * matriz[2][1])
                print(f"A determinante da Matriz é: {determinante}")
            else:
                print("A matriz não é 2x2 ou 3x3")
        elif escolhaMA == 2:
            num_linhas2 = int(input("Digite o número de linhas da segunda matriz: "))
            num_colunas2 = int(input("Digite o número de colunas da segunda matriz: "))

            matriz2 = []

            for i2 in range(num_linhas2):
                linhas2 = []
                for j2 in range(num_colunas2):
                    elementos2 = int(input(f"Informe o elemento da posição A{i2},{j2}: "))
                    linhas2.append(elementos2) 
                matriz2.append(linhas2)       
            if num_linhas != num_colunas2:
                print("Não é possíver fazer a multiplicação de matrizes")
            elif  num_linhas == num_colunas2:
                print("É possíver fazer a multiplicação de matrizes\n\n")
                
                matriz_resultado = []
                
                for i in range(num_linhas):
                    linha_resultado = []
                    for j in range(num_colunas2):
                        linha_resultado.append(0)
                    matriz_resultado.append(linha_resultado)

                for i in range(num_linhas):
                    for j in range(num_colunas2):
                        for k in range(num_colunas):
                            matriz_resultado[i][j] += matriz[i][k] * matriz2[k][j]

                print("Produto das matrizes AxB:")
                for linha in matriz_resultado:
                    print(linha)
                
        elif escolhaMA == 3:
            matriz_transposta = []

            for l in range(len(matriz[0])):
                matriz_transposta.append([0] * len(matriz))

            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    matriz_transposta[j][i] = matriz[i][j]
            print("matriz transposta: ")
            for linha in matriz_transposta:
                print(linha)

def menu():
    while True:
        print("\n\nEscolha umas das opções para continuar: \n[1] Conjuntos numéricos\n[2] Função do segundo grau\n[3] Função exponencial\n[4] Matrizes\n[5] Sair")

        escolhaM = int(input("Digite o conceito matemático deseja utilizar: "))

        if escolhaM <= 0 or escolhaM >=6:
            print("Você digitou opção inexistente, escolha outra opção!")
            continue
        elif escolhaM == 5:
            print("Você saiu da calculadora!!!")
            break
        elif escolhaM == 1:
            conjunto_numerico()
        elif escolhaM == 2:
            funcao_segundo_grau()
        elif escolhaM == 3:
            funcao_exponecial()
        elif escolhaM == 4:
            matrizes()    

print("Bem-vindo a calculadora!!!")
menu()