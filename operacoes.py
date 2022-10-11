import math
import numpy

def translacao(tx,ty):
  return [[1,0,tx],
          [0,1,ty],
          [0,0,1]]

def rotacao(angulo):
  anguloRad = numpy.radians(angulo)
  return [[math.cos(anguloRad),(math.sin(anguloRad)*(-1)),0],
            [math.sin(anguloRad),math.cos(anguloRad),0],
            [0,0,1]]

def escala(sx,sy):
  return [[sx,0,0],
          [0,sy,0],
          [0,0,1]]

def translacaoInv(tx,ty):
  return [[1,0,(tx*(-1))],
          [0,1,(ty*(-1))],
          [0,0,1]]

def rotacaoInv(angulo):
  anguloRad = numpy.radians(angulo)
  return [[math.cos(anguloRad),math.sin(anguloRad),0],
          [(math.sin(anguloRad)*(-1)),math.cos(anguloRad),0],
          [0,0,1]]

def escalaInv(sx,sy):
  return [[(1/sx),0,0],
          [0,(1/sy),0],
          [0,0,1]]

