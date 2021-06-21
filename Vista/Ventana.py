from Modelo.CC3501Utils import *

import numpy as np

class Ventana:

    """
    Clase Ventana: Se encarga de limpiar y actualizar todos los objetos del juego en pantalla
    """
    def __init__(self, fondo, jugador, muros, bombas, powerups, enemigos, salida):
        self.fondo = fondo
        self.jugador = jugador
        self.muros = muros
        self.bombas = bombas
        self.powerups = powerups
        self.enemigos = enemigos
        self.salida = salida

    def dibujar(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.fondo.dibujar()
        self.salida.dibujar()
        for powerup in self.powerups:
            powerup.dibujar()
        for bomba in self.bombas:
            bomba.dibujar()
        for enemigo in self.enemigos:
            enemigo.dibujar()
        for muro in self.muros:
            muro.dibujar()
        self.jugador.dibujar()
