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

    glutInit() # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
    glutInitWindowSize(500, 500)   # Set the width and height of your window
    glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
    glutCreateWindow("OpenGL Coding Practice") # Give your window a title
    if forma == "1":
        glutDisplayFunc(sc.showScreenQuadrado)  # Tell OpenGL to call the showScreen method continuously
        glutIdleFunc(sc.showScreenQuadrado)     # Draw any graphics or shapes in the showScreen function at all times
    elif forma == "2":
        glutDisplayFunc(sc.showScreenTriangulo)  # Tell OpenGL to call the showScreen method continuously
        glutIdleFunc(sc.showScreenTriangulo)
    elif forma == "3": 
        glutDisplayFunc(sc.showScreenCirculo)  # Tell OpenGL to call the showScreen method continuously
        glutIdleFunc(sc.showScreenCirculo)
    glutMainLoop()  # Keeps the window created above displaying/running in a loop
