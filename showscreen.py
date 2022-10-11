from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import formas
from menu2d import matResult
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
    #honestamente, não sei bem como essa função trabalha apesar de ter lido a documentação do método.
    #Sei apenas que ela mantem a figura continuamente na janela. Deixei outros métodos em comentário, que 
    #estavam na implementação onde encontrei essa função, porém não se mostraram necessários.
    #glViewport(0, 0, 500, 500)
    #glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    #glMatrixMode (GL_MODELVIEW)
    #glLoadIdentity()

def showScreenQuadrado():
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Cor rosa
    formas.quadrado(0,0,transfExemplo())
    glColor3f(50.0, 50.0, 50.0)
    formas.quadrado(0,0,np.identity(3)) #utilizamos a matriz identidade para manter o objeto inalterado a fins de comparação
    glutSwapBuffers()

def showScreenTriangulo():
    iterate()
    glColor3f(1.0, 0.0, 3.0) 
    formas.triangulo(0,0,transfExemplo())
    glColor3f(50.0, 50.0, 50.0)
    formas.triangulo(0,0,np.identity(3))
    glutSwapBuffers()
def showScreenCirculo():
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    formas.circulo(0,0,transfExemplo())
    glColor3f(50.0, 50.0, 50.0)
    formas.circulo(0,0,np.identity(3))

    glutSwapBuffers()
