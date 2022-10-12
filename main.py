import menuForma2d as mf
import menu2d
import menu3d

while True:
    dimensao = input("Digite uma operação:\n0- Sair\n1- 2D\n2- 3D\n")
    if dimensao == "1":
        print(menu2d.menu2d())
        mf.menuForma()
    elif dimensao == "2":
        menu3d.menu3d()
    elif dimensao == "0":
        break
    else:
        print("Opção invalida")