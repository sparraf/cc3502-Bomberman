from .CC3501Utils import *
from .Dimensiones import *


class Muro(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.hitbox = pygame.Rect(pos.x, ALTO_PANTALLA - pos.y, ANCHO_CELDA, ALTO_CELDA)
        self.hitbox.move_ip(0.0, -ALTO_CELDA)
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_QUADS)
        glColor3f(192/255.0, 192/255.0, 192/255.0)

        glVertex2f(0, 0)
        glVertex2f(ANCHO_CELDA, 0)
        glVertex2f(ANCHO_CELDA, ALTO_CELDA)
        glVertex2f(0, ALTO_CELDA)

        glColor3f(0.0, 0.0, 0.0)

        glVertex2f(0, 0)
        glVertex2f(ANCHO_CELDA/20, 0)
        glVertex2f(ANCHO_CELDA/20, ALTO_CELDA)
        glVertex2f(0, ALTO_CELDA)

        glVertex2f(0, ALTO_CELDA)
        glVertex2f(ANCHO_CELDA, ALTO_CELDA)
        glVertex2f(ANCHO_CELDA, ALTO_CELDA * 19/20)
        glVertex2f(0, ALTO_CELDA * 19/20)

        glVertex2f(ANCHO_CELDA/10, ALTO_CELDA/10)
        glVertex2f(ANCHO_CELDA * 3/20, ALTO_CELDA/10)
        glVertex2f(ANCHO_CELDA * 3/20, ALTO_CELDA * 3/20)
        glVertex2f(ANCHO_CELDA/10, ALTO_CELDA * 3/20)

        glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA/10)
        glVertex2f(ANCHO_CELDA * 9/10, ALTO_CELDA/10)
        glVertex2f(ANCHO_CELDA * 9/10, ALTO_CELDA * 3/20)
        glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA * 3/20)

        glVertex2f(ANCHO_CELDA/10, ALTO_CELDA * 17/20)
        glVertex2f(ANCHO_CELDA * 3/20, ALTO_CELDA * 17/20)
        glVertex2f(ANCHO_CELDA * 3/20, ALTO_CELDA * 9/10)
        glVertex2f(ANCHO_CELDA/10, ALTO_CELDA * 9/10)

        glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA * 17/20)
        glVertex2f(ANCHO_CELDA * 9/10, ALTO_CELDA * 17/20)
        glVertex2f(ANCHO_CELDA * 9/10, ALTO_CELDA * 9/10)
        glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA * 9/10)

        glColor3f(255.0, 255.0, 255.0)

        glVertex2f(0, 0)
        glVertex2f(ANCHO_CELDA, 0)
        glVertex2f(ANCHO_CELDA, ALTO_CELDA/20)
        glVertex2f(0, ALTO_CELDA/20)

        glVertex2f(ANCHO_CELDA, 0)
        glVertex2f(ANCHO_CELDA, ALTO_CELDA)
        glVertex2f(ANCHO_CELDA * 19/20, ALTO_CELDA)
        glVertex2f(ANCHO_CELDA * 19/20, 0)

        glEnd()


class MuroDestructible(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0), validez=True):
        self.hitbox = pygame.Rect(pos.x, ALTO_PANTALLA - pos.y, ANCHO_CELDA, ALTO_CELDA)
        self.hitbox.move_ip(0.0, -ALTO_CELDA)
        self.validez = validez
        super().__init__(pos, rgb)

    def cambiar_validez(self, nuevo_valor):
        self.validez = nuevo_valor

    def figura(self):
        if not self.validez:
            pass
        else:
            glBegin(GL_QUADS)

            glColor3f(181/255.0, 90/255.0, 0.0)

            glVertex2f(0, 0)
            glVertex2f(ANCHO_CELDA, 0)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 37/120)
            glVertex2f(0, ALTO_CELDA * 37/120)

            glVertex2f(0, ALTO_CELDA * 43/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 43/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 77/120)
            glVertex2f(0, ALTO_CELDA * 77/120)

            glVertex2f(0, ALTO_CELDA * 83/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 83/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA)
            glVertex2f(0, ALTO_CELDA)

            glColor3f(0.0, 0.0, 0.0)

            glVertex2f(ANCHO_CELDA * 19/40, 0)
            glVertex2f(ANCHO_CELDA * 21/40, 0)
            glVertex2f(ANCHO_CELDA * 21/40, ALTO_CELDA * 37/120)
            glVertex2f(ANCHO_CELDA * 19/40, ALTO_CELDA * 37/120)

            glVertex2f(0, ALTO_CELDA * 37/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 37/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 43/120)
            glVertex2f(0, ALTO_CELDA * 43/120)

            glVertex2f(ANCHO_CELDA * 31/120, ALTO_CELDA * 43/120)
            glVertex2f(ANCHO_CELDA * 37/120, ALTO_CELDA * 43/120)
            glVertex2f(ANCHO_CELDA * 37/120, ALTO_CELDA * 77/120)
            glVertex2f(ANCHO_CELDA * 31/120, ALTO_CELDA * 77/120)

            glVertex2f(ANCHO_CELDA * 83/120, ALTO_CELDA * 43/120)
            glVertex2f(ANCHO_CELDA * 89/120, ALTO_CELDA * 43/120)
            glVertex2f(ANCHO_CELDA * 89/120, ALTO_CELDA * 77/120)
            glVertex2f(ANCHO_CELDA * 83/120, ALTO_CELDA * 77/120)

            glVertex2f(0, ALTO_CELDA * 77/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 77/120)
            glVertex2f(ANCHO_CELDA, ALTO_CELDA * 83/120)
            glVertex2f(0, ALTO_CELDA * 83/120)

            glVertex2f(ANCHO_CELDA * 19/40, ALTO_CELDA * 83/120)
            glVertex2f(ANCHO_CELDA * 21/40, ALTO_CELDA * 83/120)
            glVertex2f(ANCHO_CELDA * 21/40, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 19/40, ALTO_CELDA)

            glEnd()
