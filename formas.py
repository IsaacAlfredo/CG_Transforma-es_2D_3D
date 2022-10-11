from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def quadrado(x,y,transfMatriz):
    a = [x,y,1] #ponto inferior esquerdo
    b = [x+100,y,1] #ponto inferior direito
    c = [x+100,y+100,1] #ponto superior direito
    d = [x, y+100,1] #ponto superior esquerdo

    alinha = list(np.matmul(transfMatriz,a))
    blinha = list(np.matmul(transfMatriz,b))
    clinha = list(np.matmul(transfMatriz,c))
    dlinha = list(np.matmul(transfMatriz,d))

    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(alinha[0], alinha[1]) # Coordinates for the bottom left point
    glVertex2f(blinha[0], blinha[1]) # Coordinates for the bottom right point
    glVertex2f(clinha[0], clinha[1]) # Coordinates for the top right point
    glVertex2f(dlinha[0], dlinha[1]) # Coordinates for the top left point
    glEnd()

def triangulo(x,y,transfMatriz):
    a = [x,y,1] #ponto inferior esquerdo
    b = [x+100,y,1] #ponto inferior direito
    c = [x,y+100,1] #ponto superior

    alinha = list(np.matmul(transfMatriz,a))
    blinha = list(np.matmul(transfMatriz,b))
    clinha = list(np.matmul(transfMatriz,c))

    glBegin(GL_TRIANGLES) # Begin the sketch
    glVertex2f(alinha[0], alinha[1]) # Coordinates for the bottom left point
    glVertex2f(blinha[0], blinha[1]) # Coordinates for the bottom right point
    glVertex2f(clinha[0], clinha[1]) # Coordinates for the top right point
    glEnd()

def circulo(x,y,transfMatriz):
    circlePoints = 100
    pi = 3.14
    raio=100
    glBegin(GL_LINE_LOOP)
    for i in range(circlePoints):
        theta=(2*pi*i)/circlePoints
        p = [x+(raio*np.cos(theta)),y+(raio*np.sin(theta)),1]
        plinha = list(np.matmul(transfMatriz,p))
        glVertex2f(plinha[0],plinha[1])
    glEnd()