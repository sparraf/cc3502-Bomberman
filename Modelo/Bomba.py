from .CC3501Utils import *
from .Dimensiones import *


class Bomba(Figura):
    def __init__(self, pos=Vector(0,0), timer=90, rgb=(0.0,0.0,0.0), alcance=1):
        self.hitbox = pygame.Rect(pos.x, ALTO_PANTALLA - pos.y, ANCHO_CELDA, ALTO_CELDA)
        self.hitbox.move_ip(0.0, -ALTO_CELDA)
        self.timer = timer
        self.validez = True
        # estado: 0 es bomba negra, 1 es bomba roja, y 2 es explosión
        self.estado = 0
        self.alcance = {"n": alcance, "s": alcance, "e": alcance, "o": alcance}

        self.killbox_hor = pygame.Rect(0.0, 0.0, ANCHO_CELDA * (1 + 2 * alcance - 4 / 10), ALTO_CELDA * 6 / 10)
        self.killbox_hor.move_ip(pos.x - ANCHO_CELDA * (alcance - 2 / 10), ALTO_PANTALLA - pos.y - ALTO_CELDA * 8 / 10)

        self.killbox_ver = pygame.Rect(0.0, 0.0, ANCHO_CELDA * 6/10, ALTO_CELDA * (1 + 2 * alcance - 4/10))
        self.killbox_ver.move_ip(pos.x + ANCHO_CELDA * 2/10, ALTO_PANTALLA - pos.y - ALTO_CELDA * (1 + alcance - 2/10))
        super().__init__(pos, rgb)

    def obtener_posicion(self):
        return self.pos

    def tick(self):
        self.timer -= 1

    def obtener_validez(self):
        return self.validez

    def cambiar_validez(self, nueva_validez):
        self.validez = nueva_validez

    def obtener_timer(self):
        return self.timer

    def obtener_estado(self):
        return self.estado

    def cambiar_estado(self, estado):
        self.estado = estado

    def agregar_colision(self, orientacion, nuevo_alcance):
        self.alcance[orientacion] = nuevo_alcance

        self.killbox_hor = pygame.Rect(0.0, 0.0, ANCHO_CELDA * (1 + self.alcance["e"] + self.alcance["o"] - 4/10),
                                       ALTO_CELDA * 6/10)
        self.killbox_hor.move_ip(self.pos.x - ANCHO_CELDA * (self.alcance["o"] - 2/10),
                                 ALTO_PANTALLA - self.pos.y - ALTO_CELDA * 8/10)

        self.killbox_ver = pygame.Rect(0.0, 0.0, ANCHO_CELDA * 6/10,
                                       ALTO_CELDA * (1 + self.alcance["n"] + self.alcance["s"] - 4/10))
        self.killbox_ver.move_ip(self.pos.x + ANCHO_CELDA * 2/10,
                                 ALTO_PANTALLA - self.pos.y - ALTO_CELDA * (1 + self.alcance["n"] - 2/10))

    def figura(self):
        if not self.validez:
            pass

        elif self.estado == 0:
            # Cuerpo de la bomba
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA/2, ALTO_CELDA/2)

            angulo = 2 * pi / 20
            radio = ANCHO_CELDA * 2/5
            for i in range(21):
                angulo_actual = angulo * i
                glVertex2f(ANCHO_CELDA/2 + cos(angulo_actual) * radio, ALTO_CELDA/2 + sin(angulo_actual) * radio)

            glEnd()

            # Brillo de la bomba
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(220.0/255, 220.0/255, 220.0/255)

            glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

            angulo_ini = 0
            radio = ANCHO_CELDA * 6 / 20
            for i in range(6):
                angulo_actual = angulo_ini + 3 * pi/50 * i
                glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

            angulo_ini = 0
            radio = ANCHO_CELDA * 5 / 20
            for i in range(6):
                angulo_actual = angulo_ini + 3 * pi/26 * i
                glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(220.0/255, 220.0/255, 220.0/255)

            glVertex2f(ANCHO_CELDA * 29 / 40, ALTO_CELDA * 14 / 40)

            angulo_ini = 2*pi/20
            radio = ANCHO_CELDA * 1 / 20
            for i in range(21):
                angulo_actual = angulo_ini * i
                glVertex2f(ANCHO_CELDA * 31 / 40 + cos(angulo_actual) * radio, ALTO_CELDA * 16 / 40 +
                           sin(angulo_actual) * radio)

            glEnd()

            # Mecha de la bomba
            glBegin(GL_QUADS)

            glColor3f(1.0, 1.0, 1.0)

            glVertex2f(ANCHO_CELDA * 11/20, ALTO_CELDA * 8/10)
            glVertex2f(ANCHO_CELDA * 12/20, ALTO_CELDA * 8/10)
            glVertex2f(ANCHO_CELDA * 12/20, ALTO_CELDA * 19/20)
            glVertex2f(ANCHO_CELDA * 11/20, ALTO_CELDA * 19/20)

            glVertex2f(ANCHO_CELDA * 12/20, ALTO_CELDA * 9/10)
            glVertex2f(ANCHO_CELDA * 13/20, ALTO_CELDA * 9/10)
            glVertex2f(ANCHO_CELDA * 13/20, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 12/20, ALTO_CELDA)

            glColor3f(255/255.0, 235/255.0, 45/255.0)

            glVertex2f(ANCHO_CELDA * 12/20, ALTO_CELDA * 19/20)
            glVertex2f(ANCHO_CELDA * 14/20, ALTO_CELDA * 19/20)
            glVertex2f(ANCHO_CELDA * 14/20, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 12/20, ALTO_CELDA)

            glEnd()

        elif self.estado == 1:
            # Cuerpo de la bomba
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(200.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA / 2)

            angulo = 2 * pi / 20
            radio = ANCHO_CELDA * 2 / 5
            for i in range(21):
                angulo_actual = angulo * i
                glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio, ALTO_CELDA / 2 + sin(angulo_actual) * radio)

            glEnd()

            # Mecha de la bomba
            glBegin(GL_QUADS)

            glColor3f(1.0, 1.0, 1.0)

            glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 19 / 20)
            glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 19 / 20)

            glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 9 / 10)
            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA * 9 / 10)
            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA)

            glColor3f(255 / 255.0, 235 / 255.0, 45 / 255.0)

            glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA * 19 / 20)
            glVertex2f(ANCHO_CELDA * 14 / 20, ALTO_CELDA * 19 / 20)
            glVertex2f(ANCHO_CELDA * 14 / 20, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 12 / 20, ALTO_CELDA)

            glEnd()

        elif self.estado == 2:
            # Fondo de la explosión
            glBegin(GL_QUADS)

            glColor3f(255/255.0, 212/255.0, 161/255.0)

            glVertex2f(ANCHO_CELDA * 2/10, ALTO_CELDA * 2/10)
            glVertex2f(ANCHO_CELDA * 8/10, ALTO_CELDA * 2/10)
            glVertex2f(ANCHO_CELDA * 8/10, ALTO_CELDA * 8/10)
            glVertex2f(ANCHO_CELDA * 2/10, ALTO_CELDA * 8/10)

            glEnd()

            # Esquina inferior izquierda
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255/255.0, 179/255.0, 78/255.0)

            glVertex2f(ANCHO_CELDA * 2/10, ALTO_CELDA * 2/10)

            angulo = 2 * pi/20
            radio = ANCHO_CELDA * 2 / 10

            for i in range(6):
                angulo_actual = angulo*i
                glVertex2f(ANCHO_CELDA * 2 / 10 + cos(angulo_actual) * radio, ALTO_CELDA * 2 / 10 +
                           sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 2 / 10)

            angulo = 2 * pi / 20
            radio = ANCHO_CELDA * 1 / 10

            for i in range(6):
                angulo_actual = angulo * i
                glVertex2f(ANCHO_CELDA * 2 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 2 / 10 + sin(angulo_actual) * radio)

            glEnd()

            # Esquina superior izquierda
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 8 / 10)

            angulo = 2 * pi / 20
            radio = ANCHO_CELDA * 2 / 10

            for i in range(6):
                angulo_actual = - angulo * i
                glVertex2f(ANCHO_CELDA * 2 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 8 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 8 / 10)

            angulo = 2 * pi / 20
            radio = ANCHO_CELDA * 1 / 10

            for i in range(6):
                angulo_actual = - angulo * i
                glVertex2f(ANCHO_CELDA * 2 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 8 / 10 + sin(angulo_actual) * radio)

            glEnd()

            # Esquina superior derecha
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)

            angulo_ini = pi
            radio = ANCHO_CELDA * 2 / 10

            for i in range(6):
                angulo_actual = angulo_ini + pi/10 * i
                glVertex2f(ANCHO_CELDA * 8 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 8 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)

            angulo_ini = pi
            radio = ANCHO_CELDA * 1 / 10

            for i in range(6):
                angulo_actual = angulo_ini + pi/10 * i
                glVertex2f(ANCHO_CELDA * 8 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 8 / 10 + sin(angulo_actual) * radio)

            glEnd()

            # Esquina inferior derecha
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 2 / 10)

            angulo_ini = pi
            radio = ANCHO_CELDA * 2 / 10

            for i in range(6):
                angulo_actual = angulo_ini - pi / 10 * i
                glVertex2f(ANCHO_CELDA * 8 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 2 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 2 / 10)

            angulo_ini = pi
            radio = ANCHO_CELDA * 1 / 10

            for i in range(6):
                angulo_actual = angulo_ini - pi/10 * i
                glVertex2f(ANCHO_CELDA * 8 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 2 / 10 + sin(angulo_actual) * radio)

            glEnd()

            # Pilares de la explosión
            glBegin(GL_QUADS)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 8/10, ALTO_CELDA * 2/10)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, 0)
            glVertex2f(ANCHO_CELDA * 2 / 10, 0)

            glVertex2f(0, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(0, ALTO_CELDA * 8 / 10)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 7 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 7 / 10)

            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA)

            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, 0)
            glVertex2f(ANCHO_CELDA * 3 / 10, 0)

            glVertex2f(0, ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 7 / 10)
            glVertex2f(0, ALTO_CELDA * 7 / 10)

            glColor3f(255/255.0, 212/255.0, 161/255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 6 / 10)

            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA)

            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, 0)
            glVertex2f(ANCHO_CELDA * 4 / 10, 0)

            glVertex2f(0, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 6 / 10)
            glVertex2f(0, ALTO_CELDA * 6 / 10)

            # Extender los pilares de la bomba según su alcance
            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))
            glVertex2f(ANCHO_CELDA * 2 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))

            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 8 / 10)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 7 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 7 / 10)

            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))
            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))

            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))
            glVertex2f(ANCHO_CELDA * 3 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))

            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 7 / 10)
            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 7 / 10)

            glColor3f(255 / 255.0, 212 / 255.0, 161 / 255.0)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 6 / 10)

            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 8 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))
            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))

            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))
            glVertex2f(ANCHO_CELDA * 4 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))

            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 6 / 10)
            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 6 / 10)

            glEnd()

            # Finales pilares
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 5 / 10)

            angulo_ini = -pi/2
            radio = ANCHO_CELDA * 3 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10) + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 5 / 10)

            angulo_ini = -pi / 2
            radio = ANCHO_CELDA * 2 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10) + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 212 / 255.0, 161 / 255.0)

            glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10), ALTO_CELDA * 5 / 10)

            angulo_ini = -pi / 2
            radio = ANCHO_CELDA * 1 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * (1 + self.alcance["e"] - 5 / 10) + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10,  ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))

            angulo_ini = 0
            radio = ANCHO_CELDA * 3 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10) + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10,  ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))

            angulo_ini = 0
            radio = ANCHO_CELDA * 2 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10) + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 212 / 255.0, 161 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10,  ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10))

            angulo_ini = 0
            radio = ANCHO_CELDA * 1 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * (1 + self.alcance["n"] - 5 / 10) + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))

            angulo_ini = -pi
            radio = ANCHO_CELDA * 3 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           - ALTO_CELDA * (self.alcance["s"] - 5 / 10) + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))

            angulo_ini = -pi
            radio = ANCHO_CELDA * 2 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           - ALTO_CELDA * (self.alcance["s"] - 5 / 10) + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 212 / 255.0, 161 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10, - ALTO_CELDA * (self.alcance["s"] - 5 / 10))

            angulo_ini = -pi
            radio = ANCHO_CELDA * 1 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           - ALTO_CELDA * (self.alcance["s"] - 5 / 10) + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_TRIANGLE_FAN)

            glColor3f(243 / 255.0, 38 / 255.0, 38 / 255.0)

            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 5 / 10)

            angulo_ini = pi / 2
            radio = ANCHO_CELDA * 3 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10) + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 179 / 255.0, 78 / 255.0)

            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 5 / 10)

            angulo_ini = pi / 2
            radio = ANCHO_CELDA * 2 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10) + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 212 / 255.0, 161 / 255.0)

            glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10), ALTO_CELDA * 5 / 10)

            angulo_ini = pi / 2
            radio = ANCHO_CELDA * 1 / 10

            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(- ANCHO_CELDA * (self.alcance["o"] - 5 / 10) + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()
