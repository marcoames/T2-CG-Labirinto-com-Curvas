
from Ponto import Ponto
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Bezier:
    def __init__NEW(self, p0: Ponto, p1: Ponto, p2: Ponto):
        print("Construtora da Bezier")
        self.ComprimentoTotalDaCurva = 0.0
        self.Coords = []
        self.Coords += [p0]
        self.Coords += [p1]
        self.Coords += [p2]
        #P = self.Coords[0]
        # P.imprime()

    def __init__(self, *args: Ponto):
        #print ("Construtora da Bezier")
        self.ComprimentoTotalDaCurva = 0.0
        self.Coords = []
        #print (args)
        for i in args:
            self.Coords.append(i)
        #P = self.Coords[2]
        # P.imprime()

    def Calcula(self, t):
        UmMenosT = 1-t
        P = Ponto()
        P = self.Coords[0] * UmMenosT * UmMenosT + \
            self.Coords[1] * 2 * UmMenosT * t + self.Coords[2] * t*t
        return P

    def setCor(self, cor):
        self.cor = cor

    def Traca(self):
        t = 0.0
        DeltaT = 1.0/50
        P = Ponto
        glBegin(GL_LINE_STRIP)

        # cor da curva
        glColor(self.cor)

        while(t < 1.0):
            P = self.Calcula(t)
            glVertex2f(P.x, P.y)
            t += DeltaT
        P = self.Calcula(1.0)  # faz o acabamento da curva
        glVertex2f(P.x, P.y)

        glEnd()
