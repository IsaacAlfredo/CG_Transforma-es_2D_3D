import operacoes3d as op3d
from operacoes import matResult

def menu3d():
    listaMatrizes = []

    while True:
        menu = input(
            "\nTransformações 3D\n"
            "Escolha uma operação:\n"
            "0- Sair\n"
            "1- Translação\n"
            "2- Rotação\n"
            "3- Escala\n"
            "4- Translação inversa\n"
            "5- Rotação inversa\n"
            "6- Escala inversa\n"
            "=> "
        )

        if menu == "0":
            break
        elif menu == "1":
            tx = int(input("\nDigite o fator de translação em x:\n=> "))
            ty = int(input("Digite o fator de translação em y:\n=> "))
            tz = int(input("Digite o fator de translação em z:\n=> "))
            listaMatrizes.append(op3d.translacao(tx, ty, tz))
        elif menu == "2":
            angulo = int(input("\nDigite o angulo de rotação:\n=> "))
            eixo = input(
                "Escolha um eixo para rotação:\n"
                "0- X\n"
                "1- Y\n"
                "2- Z\n"
                "=> "
            )

            if eixo == "0":
                listaMatrizes.append(op3d.rotacaoEmX(angulo))
            elif eixo == "1":
                listaMatrizes.append(op3d.rotacaoEmY(angulo))
            elif eixo == "2":
                listaMatrizes.append(op3d.rotacaoEmZ(angulo))
            else:
                print("\nOpção inválida.")
        elif menu == "3":
            sx = int(input("\nDigite o fator de escala em x:\n=> "))
            sy = int(input("Digite o fator de escala em y:\n=> "))
            sz = int(input("Digite o fator de escala em z:\n=> "))
            listaMatrizes.append(op3d.escala(sx, sy, sz))
        elif menu == "4":
            print("\nO valor digitado será considerado negativo")
            tx = int(input("\nDigite o fator de translação em x:\n=> "))
            ty = int(input("Digite o fator de translação em y:\n=> "))
            tz = int(input("Digite o fator de translação em z:\n=> "))
            listaMatrizes.append(op3d.translacaoInv(tx, ty, tz))
        elif menu == "5":
            print("\nO valor digitado será considerado negativo")
            angulo = int(input("Digite o angulo de rotação:\n=> "))
            eixo = input(
                "Escolha um eixo para rotação:\n"
                "0- X\n"
                "1- Y\n"
                "2- Z\n"
                "=> "
            )

            if eixo == "0":
                listaMatrizes.append(op3d.rotacaoInvEmX(angulo))
            elif eixo == "1":
                listaMatrizes.append(op3d.rotacaoInvEmY(angulo))
            elif eixo == "2":
                listaMatrizes.append(op3d.rotacaoInvEmZ(angulo))
            else:
                print("\nOpção inválida.")
        elif menu == "6":
            print("\nO valor digitado será considerado negativo")
            sx = int(input("Digite o fator de escala em x:\n=> "))
            sy = int(input("Digite o fator de escala em y:\n=> "))
            sz = int(input("Digite o fator de escala em z:\n=> "))
            listaMatrizes.append(op3d.escalaInv(sx, sy, sz))
        else:
            print("\nOpção inválida.")
    print(matResult(listaMatrizes))