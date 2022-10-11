import operacoes as op
import numpy as np

def matResult(listaMatrizes):
    matrizResult = listaMatrizes[0]

    for matriz in range(1,len(listaMatrizes)):
        matrizResult = np.matmul(matrizResult,listaMatrizes[matriz])
    return matrizResult

def menu2d():
    listaMatrizes = []

    while True:
        menu = input("Escolha uma operação:\n0- Sair\n1- Translação\n2- Rotação\n3- Escala\n4- Translação inversa\n5- Rotação inversa\n6- Escala inversa\n")
        if menu == "0":
            break
        elif menu == "1":
            tx = int(input("Digite o fator de translação em x:\n"))
            ty = int(input("Digite o fator de translação em y:\n"))
            listaMatrizes.append(op.translacao(tx,ty))
            print(listaMatrizes)

        elif menu == "2":
            angulo = int(input("Digite o angulo de rotação:\n"))
            listaMatrizes.append(op.rotacao(angulo))
        elif menu == "3":
            sx = int(input("Digite o fator de escala em x:\n"))
            sy = int(input("Digite o fator de escala em y:\n"))
            listaMatrizes.append(op.escala(sx,sy))
        elif menu == "4":
            print("O valor digitado será considerado negativo")
            tx = int(input("Digite o fator de translação em x:\n"))
            ty = int(input("Digite o fator de translação em y:\n"))
            listaMatrizes.append(op.translacaoInv(tx,ty))
        elif menu == "5":
            print("O valor digitado será considerado negativo")
            angulo = int(input("Digite o angulo de rotação:\n"))
            listaMatrizes.append(op.rotacaoInv(angulo))
        elif menu == "6":
            print("O valor digitado será considerado negativo")
            sx = int(input("Digite o fator de escala em x:\n"))
            sy = int(input("Digite o fator de escala em y:\n"))
            listaMatrizes.append(op.escalaInv(sx,sy))
        else:
            print("Opção inválida.")
    return listaMatrizes
