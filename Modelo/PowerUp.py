from .CC3501Utils import *
from .Dimensiones import *


class PowerUp(Figura):
    def __init__(self, type, pos=Vector(0,0), rgb=(0.0,0.0,0.0)):
        self.hitbox = pygame.Rect(pos.x, ALTO_PANTALLA - pos.y, ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)
        self.hitbox.move_ip(ANCHO_CELDA * 1 / 10, -ALTO_CELDA * 9 / 10)
        # type indica el tipo de power up (0 es mas bombas simultáneas, 1 es mayor alcance de bombas)
        self.type = type
        self.validez = True
        super().__init__(pos, rgb)

    def cambiar_validez(self, nueva_validez):
        self.validez = nueva_validez

    def figura(self):
        if not self.validez:
            pass
        else:
            # Fondo del powerup
            glBegin(GL_QUADS)

            glColor3f(233/255.0, 48/255.0, 48/255.0)

            glVertex2f(ANCHO_CELDA * 1 / 10, ALTO_CELDA * 1 / 10)
            glVertex2f(ANCHO_CELDA * 9 / 10, ALTO_CELDA * 1 / 10)
            glVertex2f(ANCHO_CELDA * 9 / 10, ALTO_CELDA * 9 / 10)
            glVertex2f(ANCHO_CELDA * 1 / 10, ALTO_CELDA * 9 / 10)

            glColor3f(122/255.0, 181/255.0, 63/255.0)

            glVertex2f(ANCHO_CELDA * 3 / 20, ALTO_CELDA * 3 / 20)
            glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA * 3 / 20)
            glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA * 17 / 20)
            glVertex2f(ANCHO_CELDA * 3 / 20, ALTO_CELDA * 17 / 20)

            glEnd()

            # Caso 1: Más bombas simultáneas
            if self.type == 0:
                glBegin(GL_TRIANGLE_FAN)

                glColor3f(0.0, 0.0, 0.0)

                glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

                angulo = 2 * pi / 20
                radio = ANCHO_CELDA * 6 / 20
                for i in range(21):
                    angulo_actual = angulo * i
                    glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 +
                               sin(angulo_actual) * radio)

                glEnd()


                glBegin(GL_QUADS)

                glColor3f(1.0, 1.0, 1.0)

                glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 13 / 20)
                glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 13 / 20)
                glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 16 / 20)
                glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 16 / 20)

                glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 15 / 20)
                glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA * 15 / 20)
                glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA * 33 / 40)
                glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 33 / 40)

                glEnd()


                glBegin(GL_TRIANGLE_FAN)

                glColor3f(220.0 / 255, 220.0 / 255, 220.0 / 255)

                glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

                angulo_ini =  - pi/6
                radio = ANCHO_CELDA * 4 / 20
                for i in range(6):
                    angulo_actual = angulo_ini + 3 * pi / 50 * i
                    glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 +
                               sin(angulo_actual) * radio)

                glEnd()

                glBegin(GL_TRIANGLE_FAN)

                glColor3f(0.0, 0.0, 0.0)

                glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

                angulo_ini = -pi / 6
                radio = ANCHO_CELDA * 3 / 20
                for i in range(6):
                    angulo_actual = angulo_ini + 3 * pi / 50 * i
                    glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 +
                               sin(angulo_actual) * radio)

                glEnd()

            # Caso 2: Mayor alcance de bombas
            elif self.type == 1:
                glBegin(GL_TRIANGLE_FAN)

                glColor3f(255/255.0, 119/255.0, 0/255.0)

                glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

                angulo_ini = -pi
                radio = ANCHO_CELDA * 7/20
                for i in range(11):
                    angulo_actual = angulo_ini + pi/10 * i
                    glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 +
                               sin(angulo_actual) * radio)

                glEnd()


                glBegin(GL_TRIANGLES)

                glVertex2f(ANCHO_CELDA * 3 / 20, ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * 10 / 20, ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * 10 / 20, ALTO_CELDA * 17 / 20)

                glVertex2f(ANCHO_CELDA * (3 / 20 + 1 / 6), ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * (10 / 20 + 1 / 6), ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * (10 / 20 + 1 / 6), ALTO_CELDA * 17 / 20)

                glVertex2f(ANCHO_CELDA * (3 / 20 + 2 / 6), ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * (10 / 20 + 2 / 6), ALTO_CELDA * 17 / 20)

                glEnd()


                glBegin(GL_TRIANGLE_FAN)

                glColor3f(250 / 255.0, 200 / 255.0, 0 / 255.0)

                glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

                angulo_ini = -pi
                radio = ANCHO_CELDA * 6 / 20
                for i in range(11):
                    angulo_actual = angulo_ini + pi / 10 * i
                    glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 +
                               sin(angulo_actual) * radio)

                glEnd()


                glBegin(GL_TRIANGLES)

                glVertex2f(ANCHO_CELDA * 4 / 20, ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA * 16 / 20)

                glVertex2f(ANCHO_CELDA * (4 / 20 + 1 / 6), ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * (9 / 20 + 1 / 6), ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * (10 / 20 + 1 / 6), ALTO_CELDA * 16 / 20)

                glVertex2f(ANCHO_CELDA * (4 / 20 + 2 / 6), ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * 16 / 20, ALTO_CELDA * 10 / 20)
                glVertex2f(ANCHO_CELDA * (10 / 20 + 2 / 6), ALTO_CELDA * 16 / 20)

                glEnd()

                # Dibujar ojos
                glBegin(GL_QUADS)

                glColor3f(0.0, 0.0, 0.0)

                glVertex2f(ANCHO_CELDA * (13 / 40 - 1 / 40), ALTO_CELDA * (10 / 20 - 1 / 10))
                glVertex2f(ANCHO_CELDA * (13 / 40 + 1 / 40), ALTO_CELDA * (10 / 20 - 1 / 10))
                glVertex2f(ANCHO_CELDA * (13 / 40 + 1 / 40), ALTO_CELDA * (10 / 20 + 1 / 10))
                glVertex2f(ANCHO_CELDA * (13 / 40 - 1 / 40), ALTO_CELDA * (10 / 20 + 1 / 10))

                glVertex2f(ANCHO_CELDA * (10 / 20 - 1 / 40), ALTO_CELDA * (10 / 20 - 1 / 10))
                glVertex2f(ANCHO_CELDA * (10 / 20 + 1 / 40), ALTO_CELDA * (10 / 20 - 1 / 10))
                glVertex2f(ANCHO_CELDA * (10 / 20 + 1 / 40), ALTO_CELDA * (10 / 20 + 1 / 10))
                glVertex2f(ANCHO_CELDA * (10 / 20 - 1 / 40), ALTO_CELDA * (10 / 20 + 1 / 10))

                glEnd()

                # Dibujar boca
                glBegin(GL_TRIANGLE_FAN)

                glColor3f(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0)

                glVertex2f(ANCHO_CELDA * 8 / 20, ALTO_CELDA * 7 / 20)

                angulo_ini = -pi
                radio = ANCHO_CELDA * 5 / 40
                for i in range(11):
                    angulo_actual = angulo_ini + pi / 10 * i
                    glVertex2f(ANCHO_CELDA * 8 / 20 + cos(angulo_actual) * radio, ALTO_CELDA * 7 / 20 +
                               sin(angulo_actual) * radio)

                glEnd()


                glBegin(GL_TRIANGLE_FAN)

                glColor3f(238/255.0, 22/255.0, 22/255.0)

                glVertex2f(ANCHO_CELDA * 8 / 20, ALTO_CELDA * (7 / 20 - 1/40))

                angulo_ini = -pi
                radio = ANCHO_CELDA * 1 / 20
                for i in range(11):
                    angulo_actual = angulo_ini + pi / 10 * i
                    glVertex2f(ANCHO_CELDA * 8 / 20 + cos(angulo_actual) * radio,
                               ALTO_CELDA * (7 / 20 - 1 / 40) + sin(angulo_actual) * radio)

                glEnd()
