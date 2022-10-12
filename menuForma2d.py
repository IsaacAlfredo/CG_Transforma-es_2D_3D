from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import showscreen as sc

import os
try:
    del os.environ['DISPLAY']
except:
    pass

def menuForma():
    forma = input("Selecione a forma:\n0- Sair\n1- Quadrado\n2- Triangulo\n3- Circulo\n")

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Transformacoes geometricas")
    if forma == "1":
        glutDisplayFunc(sc.showScreenQuadrado)  # chama o método continuamente
        glutIdleFunc(sc.showScreenQuadrado)     # desenha as formas
    elif forma == "2":
        glutDisplayFunc(sc.showScreenTriangulo)
        glutIdleFunc(sc.showScreenTriangulo)
    elif forma == "3": 
        glutDisplayFunc(sc.showScreenCirculo)
        glutIdleFunc(sc.showScreenCirculo)
    glutMainLoop()  # mantem a janela em loop