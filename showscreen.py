from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import formas
from menu2d import matResult,menu2d
import operacoes as op
import numpy as np

def transfExemplo():
    listaMatrizes = []
    listaMatrizes.append(op.escala(2,2))
    listaMatrizes.append(op.translacao(100,100))
    listaMatrizes.append(op.rotacao(45))
    #listaMatrizes.append(op.rotacao(90))
    #listaMatrizes.reverse()
    #print(matResult(listaMatrizes))
    return matResult(listaMatrizes)
    
def transfExemplo2():
    listaMatrizes = []
    listaMatrizes.append(op.escala(2,2))
    listaMatrizes.append(op.escalaInv(2,2))
    listaMatrizes.append(op.translacao(100,100))
    listaMatrizes.append(op.translacaoInv(100,100))
    listaMatrizes.append(op.rotacao(45))
    listaMatrizes.append(op.rotacaoInv(45))
    #listaMatrizes.append(op.rotacao(90))
    #listaMatrizes.reverse()
    #print(matResult(listaMatrizes))
    return matResult(listaMatrizes)

def transfExemplo3():
    listaMatrizes = []
    listaMatrizes.append(op.escala(2,2))
    listaMatrizes.append(op.escalaInv(1.5,3))
    listaMatrizes.append(op.translacao(100,100))
    listaMatrizes.append(op.translacaoInv(50,50))
    listaMatrizes.append(op.rotacao(45))
    listaMatrizes.append(op.rotacaoInv(25))
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
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    #glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    formas.quadrado(0,0,transfExemplo())
    glColor3f(50.0, 50.0, 50.0)
    formas.quadrado(0,0,np.identity(3))
    glutSwapBuffers()

def showScreenTriangulo():
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    formas.triangulo(0,0,transfExemplo())
    glColor3f(50.0, 50.0, 50.0)
    formas.triangulo(0,0,np.identity(3))
    glutSwapBuffers()
def showScreenCirculo():
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    formas.circulo(0,0,transfExemplo())
    glColor3f(50.0, 50.0, 50.0)
    formas.circulo(0,0,np.identity(3))

    glutSwapBuffers()

#print(np.matmul(transfExemplo(),[1,1,1]))