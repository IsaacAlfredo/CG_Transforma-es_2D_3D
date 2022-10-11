from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def quadrado(x,y,transfMatriz):
    a = [x,y,1] #ponto inferior esquerdo
    b = [x+100,y,1] #ponto inferior direito
    c = [x+100,y+100,1] #ponto superior direito
    d = [x, y+100,1] #ponto superior esquerdo

    alinha = list(np.matmul(transfMatriz,a)) #pontos após a transformação
    blinha = list(np.matmul(transfMatriz,b))
    clinha = list(np.matmul(transfMatriz,c))
    dlinha = list(np.matmul(transfMatriz,d))

    glBegin(GL_QUADS) # cria uma figura de 4 pontos
    glVertex2f(alinha[0], alinha[1]) 
    glVertex2f(blinha[0], blinha[1]) 
    glVertex2f(clinha[0], clinha[1]) 
    glVertex2f(dlinha[0], dlinha[1]) 
    glEnd()

def triangulo(x,y,transfMatriz):
    a = [x,y,1] #ponto inferior esquerdo
    b = [x+100,y,1] #ponto inferior direito
    c = [x,y+100,1] #ponto superior

    alinha = list(np.matmul(transfMatriz,a)) #Pontos após a transformação
    blinha = list(np.matmul(transfMatriz,b))
    clinha = list(np.matmul(transfMatriz,c))

    glBegin(GL_TRIANGLES) # Cria uma figura de 3 pontos
    glVertex2f(alinha[0], alinha[1]) 
    glVertex2f(blinha[0], blinha[1]) 
    glVertex2f(clinha[0], clinha[1])
    glEnd()

def circulo(x,y,transfMatriz):
    pontos = 100 #total de pontos do circulo
    pi = 3.14
    raio=100
    glBegin(GL_LINE_LOOP)
    for ponto in range(pontos):
        theta=(2*pi*ponto)/pontos #theta = o angulo de cada ponto do circulo
        p = [x+(raio*np.cos(theta)),y+(raio*np.sin(theta)),1] #p = a posição de cada ponto no circulo
        plinha = list(np.matmul(transfMatriz,p)) #pontos após a transformação
        glVertex2f(plinha[0],plinha[1])
    glEnd()