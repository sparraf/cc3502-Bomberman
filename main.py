import pygame

from Controlador.Controlador import Controlador

juego = Controlador()

# Ciclo de juego
while True:
    juego.actualizar()
    # Forzar 30 fps
    pygame.time.wait(int(1000/30))
