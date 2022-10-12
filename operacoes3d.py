import numpy
import math

def translacao(tx, ty, tz):
    return [
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ]

def rotacaoEmX(angulo):
    anguloRad = numpy.radians(angulo)
    return [
        [1, 0, 0, 0],
        [0, math.cos(anguloRad), (math.sin(anguloRad) * (-1)), 0],
        [0, math.sin(anguloRad), math.cos(anguloRad), 0],
        [0, 0, 0, 1]
    ]

def rotacaoEmY(angulo):
    anguloRad = numpy.radians(angulo)
    return [
        [math.cos(anguloRad), 0, math.sin(anguloRad), 0],
        [0, 1, 0, 0],
        [(math.sin(anguloRad) * (-1)), 0, math.cos(anguloRad), 0],
        [0, 0, 0, 1]
    ]

def rotacaoEmZ(angulo):
    anguloRad = numpy.radians(angulo)
    return [
        [math.cos(anguloRad), (math.sin(anguloRad) * (-1)), 0, 0],
        [math.sin(anguloRad), math.cos(anguloRad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

def escala(sx, sy, sz):
    return [
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ]

def rotacaoInvEmX(angulo):
    anguloRad = numpy.radians(angulo * (-1))
    return [
        [1, 0, 0, 0],
        [0, math.cos(anguloRad), (math.sin(anguloRad) * (-1)), 0],
        [0, math.sin(anguloRad), math.cos(anguloRad), 0],
        [0, 0, 0, 1]
    ]

def rotacaoInvEmY(angulo):
    anguloRad = numpy.radians(angulo * (-1))
    return [
        [math.cos(anguloRad), 0, math.sin(anguloRad), 0],
        [0, 1, 0, 0],
        [(math.sin(anguloRad) * (-1)), 0, math.cos(anguloRad), 0],
        [0, 0, 0, 1]
    ]

def rotacaoInvEmZ(angulo):
    anguloRad = numpy.radians(angulo * (-1))
    return [
        [math.cos(anguloRad), (math.sin(anguloRad) * (-1)), 0, 0],
        [math.sin(anguloRad), math.cos(anguloRad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

def translacaoInv(tx, ty, tz):
    return [
        [1, 0, 0, tx * (-1)],
        [0, 1, 0, ty * (-1)],
        [0, 0, 1, tz * (-1)],
        [0, 0, 0, 1]
    ]

def escalaInv(sx, sy, sz):
    return [
        [(1 / sx), 0, 0, 0],
        [0, (1 / sy), 0, 0],
        [0, 0, (1 / sz), 0],
        [0, 0, 0, 1]
    ]

