from .CC3501Utils import *
from .Dimensiones import *


class Salida(Figura):
    def __init__(self, pos=Vector(0,0), rgb=(0.0,0.0,0.0)):
        self.hitbox = pygame.Rect(pos.x, ALTO_PANTALLA - pos.y, ANCHO_CELDA * 8 /10, ALTO_CELDA * 8 /10)
        self.hitbox.move_ip(ANCHO_CELDA * 1 / 10, -ALTO_CELDA * 9 / 10)
        super().__init__(pos,rgb)

    def figura(self):
        glBegin(GL_QUADS)

        glColor3f(0.0, 0.0, 0.0)

        glVertex2f(ANCHO_CELDA * 1 / 10, ALTO_CELDA * 1 / 10)
        glVertex2f(ANCHO_CELDA * 9 / 10, ALTO_CELDA * 1 / 10)
        glVertex2f(ANCHO_CELDA * 9 / 10, ALTO_CELDA * 5 / 10)
        glVertex2f(ANCHO_CELDA * 1 / 10, ALTO_CELDA * 5 / 10)

        glEnd()

        glBegin(GL_TRIANGLE_FAN)

        glColor3f(0.0, 0.0, 0.0)

        glVertex2f(ANCHO_CELDA / 2, ALTO_CELDA * 5 / 10)

        angulo_ini = 0
        radio = ANCHO_CELDA * 4 / 10
        for i in range(11):
            angulo_actual = angulo_ini + pi/10 * i
            glVertex2f(ANCHO_CELDA/2 + cos(angulo_actual) * radio, ALTO_CELDA * 5/10 + sin(angulo_actual) * radio)

        glEnd()
