from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import formas
from menu2d import matResult
import operacoes as op
import numpy as np

def transfExemplo():
    pontoInicial = [[1,1,1]]
    listaMatrizes = []
    listaMatrizes.append(op.escala(2,2))
    listaMatrizes.append(op.translacao(100,100))
    listaMatrizes.append(op.rotacao(45))
    #listaMatrizes.append(op.rotacao(90))
    #listaMatrizes.reverse()
    #print(matResult(listaMatrizes))
    return matResult(listaMatrizes)
    

def iterate():
    #glViewport(0, 0, 500, 500)
    #glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    #glMatrixMode (GL_MODELVIEW)
    #glLoadIdentity()

def showScreenQuadrado():
    pontoFinal = transfExemplo()

    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    #glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    formas.quadrado(1,1,transfExemplo())
    glColor3f(50.0, 50.0, 50.0) # Set the color to pink
    formas.quadrado(1,1,np.identity(3))
    glutSwapBuffers()

def showScreenTriangulo():
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    #glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    formas.triangulo(0,0)
    glutSwapBuffers()
def showScreenCirculo():
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    #glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    formas.circulo(250,250)
    glutSwapBuffers()

#print(np.matmul(transfExemplo(),[1,1,1]))