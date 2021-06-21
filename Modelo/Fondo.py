from .CC3501Utils import *


class Fondo(Figura):

    """
    Clase Fondo: Modela cómo se dibuja el fondo del juego. El constructor recibe
    como argumentos el ancho y alto de la pantalla
    """

    def __init__(self, ancho, alto, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.ancho = ancho
        self.alto = alto
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_QUADS)

        glColor3f(0.0, 102 / 255.0, 0.0)
        #glColor3f(179/255.0, 123/255.0, 50/255.0)
        #glColor3f(87/255.0, 113/255.0, 199/255.0)

        glVertex2f(self.ancho, 0)
        glVertex2f(0, 0)
        glVertex2f(0, self.alto)
        glVertex2f(self.ancho, self.alto)
        glEnd()
