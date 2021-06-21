import os
import sys
import random

import numpy as np

from Modelo.CC3501Utils import *

from Modelo.Fondo import Fondo
from Modelo.Muro import Muro
from Modelo.Muro import MuroDestructible
from Modelo.Bomba import Bomba
from Modelo.Jugador import Jugador
from Modelo.PowerUp import PowerUp
from Modelo.Enemigo import Enemigo
from Modelo.Salida import Salida
from Vista.Ventana import Ventana

from Modelo.Dimensiones import *

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Controlador:

    """
    Clase Controlador: Se dedica a inicializar las librerías de pygame y OpenGL correctamente,
    inicializar los objetos que componen el juego, y finalmente realizar el manejo de eventos
    """

    def __init__(self):

        # Inicializar pygame y OpenGL
        self.ancho = ANCHO_PANTALLA
        self.alto = ALTO_PANTALLA
        init(self.ancho, self.alto, 'RoBomber!')

        # Calcular numero de filas y columnas del laberinto
        self.n_filas = int(self.alto / ALTO_CELDA)
        self.n_cols = int(self.ancho / ANCHO_CELDA)

        # Crear matriz que representa la posicion de los obstáculos en el laberinto
        # 1 significa muro indestructible, 2 significa muro destructible, 3 significa bomba, y 4 significa enemigo
        self.matriz = np.zeros((self.n_filas, self.n_cols))

        # Numero maximo de bombas consecutivas
        self.lim_bombas = 1

        # Alcance de las bombas
        self.alcance_bomba = 1

        # Crear Fondo
        self.fondo = Fondo(self.ancho, self.alto)

        # Crear Jugador
        self.jugador = Jugador(Vector(ANCHO_CELDA*1, ALTO_CELDA * (self.n_filas - 2)))

        # Crear Muros
        # Crear lista de muros a dibujar y diccionario que mapea cada muro referenciado en la matriz de posiciones a su
        # índice respectivo en la lista de muros a dibujar.
        self.matriz_a_lista = {}
        self.muros = []
        # Dibujar bordes
        for col in range(self.n_cols):
            self.matriz[0, col] = 1
            self.muros.append(Muro(Vector(ANCHO_CELDA * col, ALTO_CELDA * (self.n_filas - 1))))
            string = "f0c" + str(col)
            self.matriz_a_lista[string] = len(self.muros) - 1

            self.matriz[-1, col] = 1
            self.muros.append(Muro(Vector(ANCHO_CELDA * col, 0)))
            string = "f" + str(self.n_filas - 1) + "c" + str(col)
            self.matriz_a_lista[string] = len(self.muros) - 1

        for fila in range(1, self.n_filas - 1):
            self.matriz[fila, 0] = 1
            self.muros.append(Muro(Vector(0, ALTO_CELDA * (self.n_filas - fila - 1))))
            string = "f" + str(fila) + "c0"
            self.matriz_a_lista[string] = len(self.muros) - 1

            self.matriz[fila, -1] = 1
            self.muros.append(Muro(Vector(ANCHO_CELDA * (self.n_cols - 1), ALTO_CELDA * (self.n_filas - fila - 1))))
            string = "f" + str(fila) + "c" + str(self.n_cols - 1)
            self.matriz_a_lista[string] = len(self.muros) - 1

        # Dibujar muros internos
        for fila in range(2, self.n_filas - 2):
            if fila % 2 == 0:
                for col in range(2, self.n_cols - 2):
                    if col % 2 == 0:
                        self.matriz[fila,col] = 1
                        self.muros.append(Muro(Vector(ANCHO_CELDA * col, ALTO_CELDA * (self.n_filas - fila - 1))))
                        string = "f" + str(fila) + "c" + str(col)
                        self.matriz_a_lista[string] = len(self.muros) - 1

        # Dibujar muros destructibles
        # Dibujar primera fila (caso especial, no pueden haber muros sobre el jugador)
        lista_random = np.random.choice(np.arange(3, self.n_cols - 1), 6, replace=False)
        for numero in lista_random:
            self.matriz[1, numero] = 2
            self.muros.append(MuroDestructible(Vector(ANCHO_CELDA * numero, ALTO_CELDA * (self.n_filas - 2))))
            string = "f1c" + str(numero)
            self.matriz_a_lista[string] = len(self.muros) - 1
        # Dibujar segunda fila (caso especial, el jugador no puede comenzar atrapado)
        lista_random = np.random.choice(np.arange(3, self.n_cols - 1, step=2), 3, replace=False)
        for numero in lista_random:
            self.matriz[2, numero] = 2
            self.muros.append(MuroDestructible(Vector(ANCHO_CELDA * numero, ALTO_CELDA * (self.n_filas - 3))))
            string = "f2c" + str(numero)
            self.matriz_a_lista[string] = len(self.muros) - 1
        # Dibujar resto de las filas
        for fila in range(3, self.n_filas - 1):
            if fila % 2 == 1:
                lista_random = np.random.choice(np.arange(1, self.n_cols - 1), 6, replace=False)
                for numero in lista_random:
                    self.matriz[fila, numero] = 2
                    self.muros.append(MuroDestructible(Vector(ANCHO_CELDA * numero, ALTO_CELDA * (self.n_filas - fila -
                                                                                                  1))))
                    string = "f" + str(fila) + "c" + str(numero)
                    self.matriz_a_lista[string] = len(self.muros) - 1
            else:
                lista_random = np.random.choice(np.arange(1, self.n_cols - 1, step=2), 3, replace=False)
                for numero in lista_random:
                    self.matriz[fila, numero] = 2
                    self.muros.append(MuroDestructible(Vector(ANCHO_CELDA * numero, ALTO_CELDA * (self.n_filas - fila -
                                                                                                  1))))
                    string = "f" + str(fila) + "c" + str(numero)
                    self.matriz_a_lista[string] = len(self.muros) - 1

        # Crear Bombas
        self.bombas = []

        # Crear PowerUps
        self.powerups = []
        # Ubicar powerups en celdas con muros destructibles
        celdas_libres = np.where(self.matriz == 2)
        # Se toman posiciones aleatorias que estén tres o más filas abajo del jugador
        lista_random = np.random.choice(range(18, len(celdas_libres[0])), 7, False)
        tipo = 0
        salida_ubicada = False
        for i in lista_random:
            print(str(celdas_libres[0][i]) + "," + str(celdas_libres[1][i]))
            if not salida_ubicada:
                self.salida = Salida(Vector(ANCHO_CELDA * celdas_libres[1][i], ALTO_CELDA * (self.n_filas -
                                                                                             celdas_libres[0][i] - 1)))
                salida_ubicada = True
            else:
                pos = Vector(ANCHO_CELDA * celdas_libres[1][i], ALTO_CELDA * (self.n_filas - celdas_libres[0][i] - 1))
                self.powerups.append(PowerUp(type=tipo, pos=pos))
                tipo = not tipo

        # Crear Enemigos
        self.enemigos = []
        # Ubicar enemigos en celdas sin muros
        celdas_libres = np.where(self.matriz == 0)
        # Se toman posiciones aleatorias que estén tres o más filas abajo del jugador
        lista_random = np.random.choice(range(18, len(celdas_libres[0])), 7, False)
        tipo = 0
        for i in lista_random:
            pos = Vector(ANCHO_CELDA * celdas_libres[1][i], ALTO_CELDA * (self.n_filas - celdas_libres[0][i] - 1))
            self.enemigos.append(Enemigo(type=tipo, pos=pos))
            tipo = not tipo

        # Crear Vista
        self.ventana = Ventana(self.fondo, self.jugador, self.muros, self.bombas, self.powerups, self.enemigos,
                               self.salida)

        # Booleano que indica si el juego se acabó
        self.game_over = False

    def actualizar(self):
        # Actualizar la ventana
        self.ventana.dibujar()
        pygame.display.flip()

        # Rutina de game over: El juego no avanza y solo se puede cerrar el programa
        while self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Comportamiento enemigos
        for enemigo in self.enemigos:
            celda_enemigo = (int(round(self.n_filas - enemigo.obtener_posicion().y / ALTO_CELDA - 1)),
                             int(round(enemigo.obtener_posicion().x / ANCHO_CELDA)))
            pos_enemigo = enemigo.obtener_posicion()
            # Inicio timer: Elegir una dirección aleatoria de movimiento, dentro de las opciones válidas
            if enemigo.timer == 20:
                # Introducir al enemigo en la matriz de obstáculos
                self.matriz[celda_enemigo[0], celda_enemigo[1]] = 4
                velocidades = [Vector(0,0)]
                if self.matriz[celda_enemigo[0] - 1, celda_enemigo[1]] == 0:
                    velocidades.append(enemigo.obtener_velocidad_y())
                if self.matriz[celda_enemigo[0] + 1, celda_enemigo[1]] == 0:
                    velocidades.append(enemigo.obtener_velocidad_y() * -1)
                if self.matriz[celda_enemigo[0], celda_enemigo[1] - 1] == 0:
                    velocidades.append(enemigo.obtener_velocidad_x() * -1)
                if self.matriz[celda_enemigo[0], celda_enemigo[1] + 1] == 0:
                    velocidades.append(enemigo.obtener_velocidad_x())
                enemigo.cambiar_velocidad(np.random.choice(velocidades, 1)[0])
                enemigo.mover()
                enemigo.tick()
            # Si no ha pasado un segundo, continuar moviendose en esa dirección
            elif enemigo.timer != 0:
                enemigo.tick()
                # Si chocó con otro enemigo o bomba mientras se movía, retroceder
                for otro_enemigo in self.enemigos:
                    if otro_enemigo == enemigo:
                        pass
                    elif otro_enemigo.hitbox.colliderect(enemigo.hitbox):
                        enemigo.cambiar_velocidad(enemigo.obtener_velocidad() * -1)
                for bomba in self.bombas:
                    if bomba.hitbox.colliderect(enemigo.hitbox):
                        enemigo.cambiar_velocidad(enemigo.obtener_velocidad() * -1)
                enemigo.mover()
                celda_nueva = (int(round(self.n_filas - enemigo.obtener_posicion().y / ALTO_CELDA - 1)),
                             int(round(enemigo.obtener_posicion().x / ANCHO_CELDA)))
                # Si el enemigo cambió de celda, borrar su posición anterior de la matriz de obstáculos
                if celda_nueva != celda_enemigo:
                    self.matriz[celda_enemigo[0], celda_enemigo[1]] = 0
                # Si el enemigo está desalineado con las celdas, reiniciar el timer cuando se alinien
                if (enemigo.obtener_velocidad().y == 0 and pos_enemigo.x % ANCHO_CELDA == 0) or \
                        (enemigo.obtener_velocidad().x == 0 and pos_enemigo.y % ALTO_CELDA == 0):
                    enemigo.reset_timer()

            # Luego de haber pasado un segundo, reiniciar la rutina
            else:
                enemigo.reset_timer()
            # Si enemigo toca a jugador, se acaba el juego
            if self.jugador.hitbox.colliderect(enemigo.hitbox):
                self.game_over = True
                print("GAME OVER")

        # Revisar si se han creado bombas
        if self.bombas:
            # Actualizar el timer de todas las bombas
            for bomba in self.bombas:
                bomba.tick()
                timer = bomba.obtener_timer()
                # Si el timer llega a cero, explotar la bomba
                if timer == 0:
                    bomba.cambiar_estado(2)
                    celda_bomba = (round(self.n_filas - bomba.obtener_posicion().y / ALTO_CELDA - 1),
                                   round(bomba.obtener_posicion().x / ANCHO_CELDA))

                    # Revisar si la explosión choca con algun muro, y destruirlo si es destructible
                    for i in range(bomba.alcance["n"]):
                        if self.matriz[celda_bomba[0] - (i + 1), celda_bomba[1]] != 0:
                            bomba.agregar_colision("n", i + 1)
                            if self.matriz[celda_bomba[0] - (i + 1), celda_bomba[1]] == 2:
                                string = "f" + str(celda_bomba[0] - (i+1)) + "c" + str(celda_bomba[1])
                                muro = self.muros[self.matriz_a_lista[string]]
                                muro.cambiar_validez(False)
                                muro.crear()
                                self.matriz[celda_bomba[0] - (i + 1), celda_bomba[1]] = 0
                            break
                    for i in range(bomba.alcance["s"]):
                        if self.matriz[celda_bomba[0] + (i + 1), celda_bomba[1]] != 0:
                            bomba.agregar_colision("s", i + 1)
                            if self.matriz[celda_bomba[0] + (i + 1), celda_bomba[1]] == 2:
                                string = "f" + str(celda_bomba[0] + (i+1)) + "c" + str(celda_bomba[1])
                                muro = self.muros[self.matriz_a_lista[string]]
                                muro.cambiar_validez(False)
                                muro.crear()
                                self.matriz[celda_bomba[0] + (i + 1), celda_bomba[1]] = 0
                            break
                    for i in range(bomba.alcance["e"]):
                        if self.matriz[celda_bomba[0], celda_bomba[1] + (i + 1)] != 0:
                            bomba.agregar_colision("e", i + 1)
                            if self.matriz[celda_bomba[0], celda_bomba[1] + (i + 1)] == 2:
                                string = "f" + str(celda_bomba[0])  + "c" + str(celda_bomba[1] + (i+1))
                                muro = self.muros[self.matriz_a_lista[string]]
                                muro.cambiar_validez(False)
                                muro.crear()
                                self.matriz[celda_bomba[0], celda_bomba[1] + (i + 1)] = 0
                            break
                    for i in range(bomba.alcance["o"]):
                        if self.matriz[celda_bomba[0], celda_bomba[1] - (i + 1)] != 0:
                            bomba.agregar_colision("o", i + 1)
                            if self.matriz[celda_bomba[0], celda_bomba[1]  - (i + 1)] == 2:
                                string = "f" + str(celda_bomba[0]) + "c" + str(celda_bomba[1] - (i+1))
                                muro = self.muros[self.matriz_a_lista[string]]
                                muro.cambiar_validez(False)
                                muro.crear()
                                self.matriz[celda_bomba[0], celda_bomba[1] - (i + 1)] = 0
                            break

                    # Revisar si la explosión tocó a algún enemigo
                    for enemigo in self.enemigos:
                        if enemigo.hitbox.colliderect(bomba.killbox_hor) or enemigo.hitbox.colliderect(bomba.killbox_ver):
                            enemigo.cambiar_validez(False)
                            enemigo.crear()
                            celda_enemigo = (int(round(self.n_filas - enemigo.obtener_posicion().y / ALTO_CELDA - 1)),
                                             int(round(enemigo.obtener_posicion().x / ANCHO_CELDA)))
                            self.matriz[celda_enemigo[0], celda_enemigo[1]] = 0
                            self.enemigos.remove(enemigo)

                    # Revisar si la explosión tocó al jugador
                    if bomba.killbox_ver.colliderect(self.jugador.hitbox) or bomba.killbox_hor.colliderect(self.jugador.hitbox):
                        self.game_over = True
                        print("GAME OVER")

                elif timer < 0:
                    # Continuar revisando si la explosión tocó a algún enemigo
                    for enemigo in self.enemigos:
                        if enemigo.hitbox.colliderect(bomba.killbox_hor) or enemigo.hitbox.colliderect(
                                bomba.killbox_ver):
                            enemigo.cambiar_validez(False)
                            enemigo.crear()
                            celda_enemigo = (int(round(self.n_filas - enemigo.obtener_posicion().y / ALTO_CELDA - 1)),
                                             int(round(enemigo.obtener_posicion().x / ANCHO_CELDA)))
                            self.matriz[celda_enemigo[0], celda_enemigo[1]] = 0
                            self.enemigos.remove(enemigo)

                    # Continuar revisando si la explosión tocó al jugador
                    if bomba.killbox_ver.colliderect(self.jugador.hitbox) or bomba.killbox_hor.colliderect(self.jugador.hitbox):
                        self.game_over = True
                        print("GAME OVER")

                    # La explosión se mantiene por 20 frames
                    if timer == -20:
                        bomba.cambiar_validez(False)
                        bomba.crear()
                        celda_bomba = (round(self.n_filas - bomba.obtener_posicion().y / ALTO_CELDA - 1),
                                       round(bomba.obtener_posicion().x / ANCHO_CELDA))
                        self.matriz[celda_bomba[0], celda_bomba[1]] = 0
                        self.bombas.remove(bomba)
                        del self.matriz_a_lista["f" + str(celda_bomba[0]) + "c" + str(celda_bomba[1])]
                    else:
                        pass
                # Parpadear la bomba luego de 20 frames y parpadear mas rapido luego de 60 frames
                elif timer < 70 and timer % 10 == 0:
                    nuevo_estado = not bomba.obtener_estado()
                    bomba.cambiar_estado(nuevo_estado)
                elif timer < 30 and timer % 10 == 5:
                    nuevo_estado = not bomba.obtener_estado()
                    bomba.cambiar_estado(nuevo_estado)

        # Revisar si existen powerups
        if self.powerups:
            for powerup in self.powerups:
                # Revisar colisiones con powerups
                if self.jugador.hitbox.colliderect(powerup.hitbox):
                    # Caso 1: Más bombas simultaneas
                    if powerup.type == 0:
                        self.lim_bombas += 1
                    # Caso 2: Mayor alcance de bombas
                    else:
                        self.alcance_bomba += 1
                    # Eliminar powerup
                    powerup.cambiar_validez(False)
                    powerup.crear()
                    self.powerups.remove(powerup)

        # Calcular la celda en la que se encuentra el jugador (en notacion (fila,columna))
        celda_jugador = (round(self.n_filas - self.jugador.obtener_posicion().y / ALTO_CELDA - 1),
                         round(self.jugador.obtener_posicion().x / ANCHO_CELDA))

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Poner una bomba al apretar "a"
                if event.key == K_a and len(self.bombas) < self.lim_bombas:
                    orientacion_jugador = self.jugador.obtener_orientacion()
                    # Revisar si se puede poner la bomba en la direccion que está mirando el jugador
                    obst = self.matriz[celda_jugador[0]-orientacion_jugador.y, celda_jugador[1]+orientacion_jugador.x]
                    if obst == 0:
                        pos_bomba = Vector((celda_jugador[1] + orientacion_jugador.x) * ANCHO_CELDA,
                                           (self.n_filas - 1 + orientacion_jugador.y - celda_jugador[0]) * ALTO_CELDA)
                        self.bombas.append(Bomba(pos_bomba, alcance=self.alcance_bomba))
                        # Revisar si hay algun enemigo en el lugar
                        colision = False
                        for enemigo in self.enemigos:
                            if enemigo.hitbox.colliderect(self.bombas[-1].hitbox):
                                self.bombas.pop()
                                colision = True
                                break
                        # Agregar la bomba a la matriz de obstáculos para poder calcular colisiones con objetos
                        if not colision:
                            self.matriz[celda_jugador[0] - orientacion_jugador.y, celda_jugador[1] +
                                        orientacion_jugador.x] = 3
                            string = "f" + str(celda_jugador[0] - orientacion_jugador.y) + "c" + str(
                                celda_jugador[1] + orientacion_jugador.x)
                            self.matriz_a_lista[string] = len(self.bombas) - 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.jugador.cambiar_orientacion(Vector(0, 1))
            delta_pos = self.jugador.obtener_velocidad_y()
            # Revisar si hay colisión con algún muro o bomba. Si se choca con la esquina de un bloque, empujar al
            # jugador hacia afuea
            if 0 < self.matriz[celda_jugador[0] - 1, celda_jugador[1] + 1] < 3:
                string = "f" + str(celda_jugador[0] - 1) + "c" + str(celda_jugador[1] + 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos -= self.jugador.obtener_velocidad_x()

            if 0 < self.matriz[celda_jugador[0] - 1, celda_jugador[1] - 1] < 3:
                string = "f" + str(celda_jugador[0] - 1) + "c" + str(celda_jugador[1] - 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos += self.jugador.obtener_velocidad_x()

            if 0 < self.matriz[celda_jugador[0] - 1, celda_jugador[1]] < 3:
                string = "f" + str(celda_jugador[0] - 1) + "c" + str(celda_jugador[1])
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            if self.matriz[celda_jugador[0] - 1, celda_jugador[1]] == 3:
                string = "f" + str(celda_jugador[0] - 1) + "c" + str(celda_jugador[1])
                bomba = self.bombas[self.matriz_a_lista[string]]
                if bomba.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            self.jugador.mover(delta_pos)

        if keys[pygame.K_DOWN]:
            self.jugador.cambiar_orientacion(Vector(0, -1))
            delta_pos = self.jugador.obtener_velocidad_y() * -1
            # Revisar si hay colisión con algún muro o bomba
            if 0 < self.matriz[celda_jugador[0] + 1, celda_jugador[1]] < 3:
                string = "f" + str(celda_jugador[0] + 1) + "c" + str(celda_jugador[1])
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            if 0 < self.matriz[celda_jugador[0] + 1, celda_jugador[1] + 1] < 3:
                string = "f" + str(celda_jugador[0] + 1) + "c" + str(celda_jugador[1] + 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos -= self.jugador.obtener_velocidad_x()

            if 0 < self.matriz[celda_jugador[0] + 1, celda_jugador[1] - 1] < 3:
                string = "f" + str(celda_jugador[0] + 1) + "c" + str(celda_jugador[1] - 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos += self.jugador.obtener_velocidad_x()

            if self.matriz[celda_jugador[0] + 1, celda_jugador[1]] == 3:
                string = "f" + str(celda_jugador[0] + 1) + "c" + str(celda_jugador[1])
                bomba = self.bombas[self.matriz_a_lista[string]]
                if bomba.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            self.jugador.mover(delta_pos)

        if keys[pygame.K_LEFT]:
            self.jugador.cambiar_orientacion(Vector(-1, 0))
            delta_pos = self.jugador.obtener_velocidad_x() * -1
            # Revisar si hay colisión con algún muro o bomba
            if 0 < self.matriz[celda_jugador[0], celda_jugador[1] - 1] < 3:
                string = "f" + str(celda_jugador[0]) + "c" + str(celda_jugador[1] - 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            if 0 < self.matriz[celda_jugador[0] + 1, celda_jugador[1] - 1] < 3:
                string = "f" + str(celda_jugador[0] + 1) + "c" + str(celda_jugador[1] - 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos += self.jugador.obtener_velocidad_y()

            if 0 < self.matriz[celda_jugador[0] - 1, celda_jugador[1] - 1] < 3:
                string = "f" + str(celda_jugador[0] - 1) + "c" + str(celda_jugador[1] - 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos -= self.jugador.obtener_velocidad_y()

            if self.matriz[celda_jugador[0], celda_jugador[1] - 1] == 3:
                string = "f" + str(celda_jugador[0]) + "c" + str(celda_jugador[1] - 1)
                bomba = self.bombas[self.matriz_a_lista[string]]
                if bomba.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            self.jugador.mover(delta_pos)

        if keys[pygame.K_RIGHT]:
            self.jugador.cambiar_orientacion(Vector(1, 0))
            delta_pos = self.jugador.obtener_velocidad_x()
            # Revisar si hay colisión con algún muro o bomba
            if 0 < self.matriz[celda_jugador[0], celda_jugador[1] + 1] < 3:
                string = "f" + str(celda_jugador[0]) + "c" + str(celda_jugador[1] + 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            if 0 < self.matriz[celda_jugador[0] + 1, celda_jugador[1] + 1] < 3:
                string = "f" + str(celda_jugador[0] + 1) + "c" + str(celda_jugador[1] + 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos += self.jugador.obtener_velocidad_y()

            if 0 < self.matriz[celda_jugador[0] - 1, celda_jugador[1] + 1] < 3:
                string = "f" + str(celda_jugador[0] - 1) + "c" + str(celda_jugador[1] + 1)
                muro = self.muros[self.matriz_a_lista[string]]
                if muro.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos -= self.jugador.obtener_velocidad_y()

            if self.matriz[celda_jugador[0], celda_jugador[1] + 1] == 3:
                string = "f" + str(celda_jugador[0]) + "c" + str(celda_jugador[1] + 1)
                bomba = self.bombas[self.matriz_a_lista[string]]
                if bomba.hitbox.colliderect(self.jugador.hitbox):
                    delta_pos = Vector(0, 0)

            self.jugador.mover(delta_pos)

        # Revisar si jugador ganó
        if self.jugador.hitbox.colliderect(self.salida.hitbox):
            print("Has ganado!")
            self.game_over = True

        self.jugador.crear()

        for bomba in self.bombas:
            bomba.crear()
