from .CC3501Utils import *
from .Dimensiones import *


class Enemigo(Figura):
    def __init__(self, pos=Vector(0,0), type=0, rgb=(0.0,0.0,0.0)):
        self.hitbox = pygame.Rect(pos.x, pos.y, ANCHO_CELDA * 8 / 10, ALTO_CELDA * 8 / 10)
        self.hitbox.move_ip(ANCHO_CELDA * 1 / 10, -ALTO_CELDA * 9/10)
        self.vel_x = Vector(ANCHO_CELDA * 1/20, 0)
        self.vel_y = Vector(0, 1/20 * ALTO_CELDA)
        self.type = type
        self.vel_elegida = Vector(0,0)
        self.timer = 20
        self.validez = True
        super().__init__(pos, rgb)

    def tick(self):
        self.timer -= 1

    def reset_timer(self):
        self.timer = 20

    def cambiar_velocidad(self, nueva_velocidad):
        self.vel_elegida = nueva_velocidad

    def obtener_velocidad(self):
        return self.vel_elegida

    def obtener_velocidad_x(self):
        return self.vel_x

    def obtener_velocidad_y(self):
        return self.vel_y

    def obtener_posicion(self):
        return self.pos

    def mover(self):
        self.pos += self.vel_elegida
        self.hitbox.topleft = (self.pos.x, ALTO_PANTALLA - self.pos.y)
        self.hitbox.move_ip(ANCHO_CELDA * 1 / 10, -ALTO_CELDA * 8 / 10)

    def cambiar_validez(self, nueva_validez):
        self.validez = nueva_validez

    def figura(self):
        # Caso 0: Enemigo eliminado
        if not self.validez:
            pass
        # Caso 1: Alien
        elif self.type == 0:
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 6 / 10)

            angulo_ini = 0
            radio = ANCHO_CELDA * 3 / 10
            for i in range(11):
                angulo_actual = angulo_ini + pi/10 * i
                glVertex2f(ANCHO_CELDA/2 + cos(angulo_actual) * radio, ALTO_CELDA * 6 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_QUADS)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 4 / 10)

            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 9 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * 1 / 10)
            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 4 / 10)

            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 1 / 10)
            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 1 / 10)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 1 / 10, ALTO_CELDA * 2 / 10)
            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * 1 / 10)
            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 4 / 10)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(54/255.0, 151/255.0, 236/255.0)


            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 6 / 10)

            angulo_ini = 0
            radio = ANCHO_CELDA * 5 / 20
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 6 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_QUADS)

            glVertex2f(ANCHO_CELDA * 15 / 20, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 33 / 40, ALTO_CELDA * 4 / 20)
            glVertex2f(ANCHO_CELDA * 14 / 20, ALTO_CELDA * 7 / 40)
            glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 4 / 10)

            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 3 / 20)
            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA * 3 / 20)

            glVertex2f(ANCHO_CELDA * 5 / 20, ALTO_CELDA * 4 / 10)
            glVertex2f(ANCHO_CELDA * 7 / 40, ALTO_CELDA * 4 / 20)
            glVertex2f(ANCHO_CELDA * 6 / 20, ALTO_CELDA * 7 / 40)
            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA * 4 / 10)

            glColor3f(1.0, 1.0, 1.0)

            glVertex2f(ANCHO_CELDA * 5 / 20, ALTO_CELDA * 11 / 20)
            glVertex2f(ANCHO_CELDA * 15 / 20, ALTO_CELDA * 11 / 20)
            glVertex2f(ANCHO_CELDA * 15 / 20, ALTO_CELDA * 9 / 20)
            glVertex2f(ANCHO_CELDA * 5 / 20, ALTO_CELDA * 9 / 20)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA * 6 / 20, ALTO_CELDA * 21 / 40)
            glVertex2f(ANCHO_CELDA * 14 / 20, ALTO_CELDA * 21 / 40)
            glVertex2f(ANCHO_CELDA * 14 / 20, ALTO_CELDA * 19 / 40)
            glVertex2f(ANCHO_CELDA * 6 / 20, ALTO_CELDA * 19 / 40)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(1.0, 1.0, 1.0)

            glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA * 15 / 20)

            angulo_ini = 0
            radio = ANCHO_CELDA * 1 / 10
            for i in range(21):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA / 2 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 15 / 20 + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_QUADS)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA * (10 / 20 - 1 / 40), ALTO_CELDA * (14 / 20 - 1 / 40))
            glVertex2f(ANCHO_CELDA * (10 / 20 + 1 / 40), ALTO_CELDA * (14 / 20 - 1 / 40))
            glVertex2f(ANCHO_CELDA * (10 / 20 + 1 / 40), ALTO_CELDA * (14 / 20 + 1 / 40))
            glVertex2f(ANCHO_CELDA * (10 / 20 - 1 / 40), ALTO_CELDA * (14 / 20 + 1 / 40))

            glEnd()

        elif self.type == 1:
            # Caso 2: Platillo volador
            # Dibujar cuerpo
            glBegin(GL_QUADS)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA * 2 / 10, ALTO_CELDA * 5 / 10)
            glVertex2f(ANCHO_CELDA * 8 / 10, ALTO_CELDA * 5 / 10)
            glVertex2f(ANCHO_CELDA * 9 / 10, ALTO_CELDA * 3 / 10)
            glVertex2f(ANCHO_CELDA * 1 / 10, ALTO_CELDA * 3 / 10)

            glColor3f(255 / 255.0, 40 / 255.0, 0 / 255.0)

            glVertex2f(ANCHO_CELDA * 5 / 20, ALTO_CELDA * 9 / 20)
            glVertex2f(ANCHO_CELDA * 15 / 20, ALTO_CELDA * 9 / 20)
            glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA * 7 / 20)
            glVertex2f(ANCHO_CELDA * 4 / 20, ALTO_CELDA * 7 / 20)

            glEnd()

            # Dibujar casco
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 5 / 10)

            angulo_ini = 0
            radio = ANCHO_CELDA * 3 / 10
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(63/255.0, 198/255.0, 247/255.0)

            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 5 / 10)

            angulo_ini = 0
            radio = ANCHO_CELDA * 5 / 20
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 5 / 10 + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_QUADS)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA * 7 / 10)
            glVertex2f(ANCHO_CELDA * 4 / 10, ALTO_CELDA * 7 / 10)

            glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 6 / 10)
            glVertex2f(ANCHO_CELDA * 6 / 10, ALTO_CELDA * 7 / 10)
            glVertex2f(ANCHO_CELDA * 11 / 20, ALTO_CELDA * 7 / 10)

            glEnd()

            # Dibujar adornos
            glBegin(GL_TRIANGLE_FAN)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * 3 / 10)

            angulo_ini = -pi
            radio = ANCHO_CELDA * 1 / 10
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 3 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 3 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 3 / 10)

            angulo_ini = -pi
            radio = ANCHO_CELDA * 1 / 10
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 3 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * 3 / 10)

            angulo_ini = -pi
            radio = ANCHO_CELDA * 1 / 10
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 7 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 3 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glColor3f(255 / 255.0, 40 / 255.0, 0 / 255.0)

            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA * 3 / 10)

            angulo_ini = -pi
            radio = ANCHO_CELDA * 1 / 20
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 3 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 3 / 10 + sin(angulo_actual) * radio)

            glEnd()


            glBegin(GL_TRIANGLE_FAN)

            glVertex2f(ANCHO_CELDA * 5 / 10, ALTO_CELDA * 3 / 10)

            angulo_ini = -pi
            radio = ANCHO_CELDA * 1 / 20
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 5 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 3 / 10 + sin(angulo_actual) * radio)

            glEnd()

            glBegin(GL_TRIANGLE_FAN)

            glVertex2f(ANCHO_CELDA * 7 / 10, ALTO_CELDA * 3 / 10)

            angulo_ini = -pi
            radio = ANCHO_CELDA * 1 / 20
            for i in range(11):
                angulo_actual = angulo_ini + pi / 10 * i
                glVertex2f(ANCHO_CELDA * 7 / 10 + cos(angulo_actual) * radio,
                           ALTO_CELDA * 3 / 10 + sin(angulo_actual) * radio)

            glEnd()
