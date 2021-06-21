from .CC3501Utils import *
from .Dimensiones import *


class Jugador(Figura):
    def __init__(self, pos=Vector(0, 0), orientacion=Vector(0, -1), rgb=(1.0, 1.0, 1.0)):
        self.vel_x = Vector(ANCHO_CELDA * 2 / 30, 0)
        self.vel_y = Vector(0, ALTO_CELDA * 2 / 30)
        self.orientacion = orientacion
        self.hitbox = pygame.Rect(0.0, 0.0, ANCHO_CELDA * 9 / 10, ALTO_CELDA * 9 / 10)
        self.hitbox.move_ip(ANCHO_CELDA * 21 / 20, ALTO_CELDA * 11 / 10)
        super().__init__(pos, rgb)

    def cambiar_orientacion(self, nueva_orientacion: Vector):
        self.orientacion = nueva_orientacion

    def obtener_orientacion(self):
        return self.orientacion

    def mover(self, delta_posicion):
        self.pos += delta_posicion
        self.hitbox.topleft = (self.pos.x, ALTO_PANTALLA - self.pos.y)
        self.hitbox.move_ip(ANCHO_CELDA * 1 / 20, -ALTO_CELDA * 9 / 10)

    def obtener_posicion(self):
        return self.pos

    def obtener_velocidad_x(self):
        return self.vel_x

    def obtener_velocidad_y(self):
        return self.vel_y

    def figura(self):
        norte = Vector(0, 1)
        sur = Vector(0, -1)
        este = Vector(1, 0)
        oeste = Vector(-1, 0)

        if punto(self.orientacion, sur) > 0:
            # Dibujar jugador orientación SUR
            glBegin(GL_QUADS)

            ancho_cabeza = ANCHO_CELDA * 8 / 10
            alto_cabeza = ALTO_CELDA * 23 / 80

            ancho_piernas = ANCHO_CELDA/10
            alto_piernas = ALTO_CELDA/4

            ancho_antenas = ANCHO_CELDA * 1/20
            alto_antenas = ALTO_CELDA * 3/20

            ancho_cuerpo = ANCHO_CELDA * 6/10
            alto_cuerpo = ALTO_CELDA * 5/16

            ancho_ojos = 2*ancho_antenas
            alto_ojos = ancho_ojos

            ancho_boca = 3*ancho_ojos
            alto_boca = ancho_antenas

            # Dibujar la cabeza
            glColor3f(202/255.0, 211/255.0, 226/255.0)

            glVertex2f(ANCHO_CELDA/10, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA/10 + ancho_cabeza, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA/10 + ancho_cabeza, alto_piernas + alto_cuerpo + alto_cabeza)
            glVertex2f(ANCHO_CELDA/10, alto_cuerpo + alto_piernas + alto_cabeza)

            # Dibujar antenas
            glVertex2f(ANCHO_CELDA/10, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA/10 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA/10 + ancho_antenas, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA/10, ALTO_CELDA)

            glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 17/20 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 17/20 + ancho_antenas, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA)

            # Dibujar cuerpo
            glVertex2f(ANCHO_CELDA * 2/10, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2/10 + ancho_cuerpo, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2/10 + ancho_cuerpo, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA * 2/10, alto_piernas + alto_cuerpo)

            # Dibujar piernas
            glColor3f(163/255.0, 168/255.0, 175/255.0)

            glVertex2f(ANCHO_CELDA * 3/10, 0)
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_piernas, 0)
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 3/10, alto_piernas)

            glVertex2f(ANCHO_CELDA * 6/10, 0)
            glVertex2f(ANCHO_CELDA * 6/10 + ancho_piernas, 0)
            glVertex2f(ANCHO_CELDA * 6/10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 6/10, alto_piernas)

            # Dibujar brazo izquierdo
            glVertex2f(ANCHO_CELDA/10, alto_piernas + alto_cuerpo * 3/5)
            glVertex2f(ANCHO_CELDA * 2/10, alto_piernas + alto_cuerpo * 3/5)
            glVertex2f(ANCHO_CELDA * 2/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)

            glVertex2f(ANCHO_CELDA/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 3/20, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 3/20, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/10)
            glVertex2f(ANCHO_CELDA/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/10)

            # Dibujar brazo derecho
            glVertex2f(ANCHO_CELDA * 8/10, alto_piernas + alto_cuerpo * 3/5)
            glVertex2f(ANCHO_CELDA * 9/10, alto_piernas + alto_cuerpo * 3/5)
            glVertex2f(ANCHO_CELDA * 9/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 8/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)

            glVertex2f(ANCHO_CELDA * 17/20, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 9/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 9/10, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/10)
            glVertex2f(ANCHO_CELDA * 17/20, alto_piernas + alto_cuerpo * 3/5 - ANCHO_CELDA/10)

            # Dibujar franja antenas
            glColor3f(62/255.0, 106/255.0, 181/255.0)

            glVertex2f(ANCHO_CELDA/10, ALTO_CELDA - alto_antenas * 3/5)
            glVertex2f(ANCHO_CELDA/10 + ancho_antenas, ALTO_CELDA - alto_antenas * 3/5)
            glVertex2f(ANCHO_CELDA/10 + ancho_antenas, ALTO_CELDA - alto_antenas/5)
            glVertex2f(ANCHO_CELDA/10, ALTO_CELDA - alto_antenas/5)

            glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 17/20 + ancho_antenas, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 17/20 + ancho_antenas, ALTO_CELDA - alto_antenas / 5)
            glVertex2f(ANCHO_CELDA * 17/20, ALTO_CELDA - alto_antenas / 5)

            # Dibujar ojos
            glColor3f(4/255.0, 17/255.0, 40/255.0)

            glVertex2f(ANCHO_CELDA * 5/20, ALTO_CELDA - alto_antenas - alto_cabeza/2)
            glVertex2f(ANCHO_CELDA * 5/20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza/2)
            glVertex2f(ANCHO_CELDA * 5/20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza/2 + alto_ojos)
            glVertex2f(ANCHO_CELDA * 5/20, ALTO_CELDA - alto_antenas - alto_cabeza/2 + alto_ojos)

            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 13 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 13 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)
            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)

            # Dibujar boca
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_ojos/2, alto_piernas + alto_cuerpo + ancho_antenas)
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_ojos/2 + ancho_boca, alto_piernas + alto_cuerpo + ancho_antenas)
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_ojos/2 + ancho_boca, alto_piernas+alto_cuerpo+ancho_antenas+alto_boca)
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_ojos/2, alto_piernas + alto_cuerpo + ancho_antenas+alto_boca)

            glEnd()

        elif punto(self.orientacion, norte) > 0:
            # Dibujar jugador orientación NORTE
            glBegin(GL_QUADS)

            ancho_cabeza = ANCHO_CELDA * 8 / 10
            alto_cabeza = ALTO_CELDA * 23 / 80

            ancho_piernas = ANCHO_CELDA / 10
            alto_piernas = ALTO_CELDA / 4

            ancho_antenas = ANCHO_CELDA * 1 / 20
            alto_antenas = ALTO_CELDA * 3 / 20

            ancho_cuerpo = ANCHO_CELDA * 6 / 10
            alto_cuerpo = ALTO_CELDA * 5 / 16

            # Dibujar la cabeza
            glColor3f(202 / 255.0, 211 / 255.0, 226 / 255.0)

            glVertex2f(ANCHO_CELDA / 10, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA / 10 + ancho_cabeza, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA / 10 + ancho_cabeza, alto_piernas + alto_cuerpo + alto_cabeza)
            glVertex2f(ANCHO_CELDA / 10, alto_cuerpo + alto_piernas + alto_cabeza)

            # Dibujar antenas
            glVertex2f(ANCHO_CELDA / 10, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA / 10 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA / 10 + ancho_antenas, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA / 10, ALTO_CELDA)

            glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 17 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 17 / 20 + ancho_antenas, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA)

            # Dibujar cuerpo
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2 / 10 + ancho_cuerpo, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2 / 10 + ancho_cuerpo, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas + alto_cuerpo)

            # Dibujar piernas
            glColor3f(163/255.0, 168/255.0, 175/255.0)

            glVertex2f(ANCHO_CELDA * 3 / 10, 0)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_piernas, 0)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 3 / 10, alto_piernas)

            glVertex2f(ANCHO_CELDA * 6 / 10, 0)
            glVertex2f(ANCHO_CELDA * 6 / 10 + ancho_piernas, 0)
            glVertex2f(ANCHO_CELDA * 6 / 10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 6 / 10, alto_piernas)

            # Dibujar brazo izquierdo
            glVertex2f(ANCHO_CELDA / 10, alto_piernas + alto_cuerpo * 3 / 5)
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas + alto_cuerpo * 3 / 5)
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)

            glVertex2f(ANCHO_CELDA / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 3 / 20, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 3 / 20, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 10)
            glVertex2f(ANCHO_CELDA / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 10)

            # Dibujar brazo derecho
            glVertex2f(ANCHO_CELDA * 8 / 10, alto_piernas + alto_cuerpo * 3 / 5)
            glVertex2f(ANCHO_CELDA * 9 / 10, alto_piernas + alto_cuerpo * 3 / 5)
            glVertex2f(ANCHO_CELDA * 9 / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 8 / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)

            glVertex2f(ANCHO_CELDA * 17 / 20, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 9 / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 9 / 10, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 10)
            glVertex2f(ANCHO_CELDA * 17 / 20, alto_piernas + alto_cuerpo * 3 / 5 - ANCHO_CELDA / 10)

            # Dibujar franja antenas
            glColor3f(62 / 255.0, 106 / 255.0, 181 / 255.0)

            glVertex2f(ANCHO_CELDA / 10, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA / 10 + ancho_antenas, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA / 10 + ancho_antenas, ALTO_CELDA - alto_antenas / 5)
            glVertex2f(ANCHO_CELDA / 10, ALTO_CELDA - alto_antenas / 5)

            glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 17 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 17 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas / 5)
            glVertex2f(ANCHO_CELDA * 17 / 20, ALTO_CELDA - alto_antenas / 5)

            glEnd()

        elif punto(self.orientacion, este) > 0:
            # Dibujar jugador orientación ESTE
            glBegin(GL_QUADS)

            ancho_cabeza = ANCHO_CELDA * 8 / 10
            alto_cabeza = ALTO_CELDA * 23 / 80

            ancho_piernas = ANCHO_CELDA / 10
            alto_piernas = ALTO_CELDA / 4

            ancho_antenas = ANCHO_CELDA * 1 / 20
            alto_antenas = ALTO_CELDA * 3 / 20

            ancho_cuerpo = ANCHO_CELDA * 6 / 10
            alto_cuerpo = ALTO_CELDA * 5 / 16

            ancho_ojos = 2 * ancho_antenas
            alto_ojos = ancho_ojos

            ancho_boca = 2 * ancho_ojos
            alto_boca = ancho_antenas

            # Dibujar la cabeza
            glColor3f(202 / 255.0, 211 / 255.0, 226 / 255.0)

            glVertex2f(ANCHO_CELDA / 10, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA / 10 + ancho_cabeza, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA / 10 + ancho_cabeza, alto_piernas + alto_cuerpo + alto_cabeza)
            glVertex2f(ANCHO_CELDA / 10, alto_cuerpo + alto_piernas + alto_cabeza)

            # Dibujar antenas
            glVertex2f(ANCHO_CELDA * 3/10, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 3/10 + ancho_antenas, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 3/10, ALTO_CELDA)

            glVertex2f(ANCHO_CELDA * 16 / 20, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 16 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 16 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas/3)
            glVertex2f(ANCHO_CELDA * 16 / 20, ALTO_CELDA - alto_antenas/3)

            # Dibujar mitad de arriba del brazo izquierdo
            glColor3f(163 / 255.0, 168 / 255.0, 175 / 255.0)

            glVertex2f(ANCHO_CELDA * 5/40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 2/10, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 5/20, alto_piernas + alto_cuerpo * 3 / 4)
            glVertex2f(ANCHO_CELDA * 2/10, alto_piernas + alto_cuerpo * 3 / 4)

            # Dibujar cuerpo
            glColor3f(202 / 255.0, 211 / 255.0, 226 / 255.0)

            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2 / 10 + ancho_cuerpo, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2 / 10 + ancho_cuerpo, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas + alto_cuerpo)

            # Dibujar mitad de abajo de brazo izquierdo
            glColor3f(163 / 255.0, 168 / 255.0, 175 / 255.0)

            glVertex2f(ANCHO_CELDA * 5/40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 2/10, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 23/80, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 5/40)
            glVertex2f(ANCHO_CELDA * 5/20, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 13/80)

            # Dibujar brazo derecho
            glVertex2f(ANCHO_CELDA * 8/10, alto_piernas + alto_cuerpo * 3 / 4)
            glVertex2f(ANCHO_CELDA * 35/40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA/20)
            glVertex2f(ANCHO_CELDA * 33/40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 4/40)
            glVertex2f(ANCHO_CELDA * 8/10, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 3/40)

            # Dibujar piernas
            glVertex2f(ANCHO_CELDA * 3 / 10, 0)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_piernas, 0)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 3 / 10, alto_piernas)

            glVertex2f(ANCHO_CELDA * 6 / 10, alto_piernas/4)
            glVertex2f(ANCHO_CELDA * 6 / 10 + ancho_piernas, alto_piernas/4)
            glVertex2f(ANCHO_CELDA * 6 / 10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 6 / 10, alto_piernas)

            # Dibujar franja antenas
            glColor3f(62 / 255.0, 106 / 255.0, 181 / 255.0)

            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_antenas, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_antenas, ALTO_CELDA - alto_antenas / 5)
            glVertex2f(ANCHO_CELDA * 3 / 10, ALTO_CELDA - alto_antenas / 5)

            glVertex2f(ANCHO_CELDA * 16 / 20, ALTO_CELDA - alto_antenas * 9 / 15)
            glVertex2f(ANCHO_CELDA * 16 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas * 9 / 15)
            glVertex2f(ANCHO_CELDA * 16 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas * 7 / 15)
            glVertex2f(ANCHO_CELDA * 16 / 20, ALTO_CELDA - alto_antenas * 7 / 15)

            # Dibujar ojos
            glColor3f(4 / 255.0, 17 / 255.0, 40 / 255.0)

            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 9 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 9 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)
            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)

            glVertex2f(ANCHO_CELDA * 14 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 14 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 14 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)
            glVertex2f(ANCHO_CELDA * 14 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)

            # Dibujar boca
            glVertex2f(ANCHO_CELDA * 19 / 40 + ancho_ojos / 2, alto_piernas + alto_cuerpo + ancho_antenas)
            glVertex2f(ANCHO_CELDA * 19 / 40 + ancho_ojos / 2 + ancho_boca, alto_piernas + alto_cuerpo + ancho_antenas)
            glVertex2f(ANCHO_CELDA * 19 / 40 + ancho_ojos / 2 + ancho_boca,
                       alto_piernas + alto_cuerpo + ancho_antenas + alto_boca)
            glVertex2f(ANCHO_CELDA * 19 / 40 + ancho_ojos / 2, alto_piernas + alto_cuerpo + ancho_antenas + alto_boca)

            glEnd()

        elif punto(self.orientacion, oeste) > 0:
            # Dibujar jugador orientación OESTE
            glBegin(GL_QUADS)

            ancho_cabeza = ANCHO_CELDA * 8 / 10
            alto_cabeza = ALTO_CELDA * 23 / 80

            ancho_piernas = ANCHO_CELDA / 10
            alto_piernas = ALTO_CELDA / 4

            ancho_antenas = ANCHO_CELDA * 1 / 20
            alto_antenas = ALTO_CELDA * 3 / 20

            ancho_cuerpo = ANCHO_CELDA * 6 / 10
            alto_cuerpo = ALTO_CELDA * 5 / 16

            ancho_ojos = 2 * ancho_antenas
            alto_ojos = ancho_ojos

            ancho_boca = 2 * ancho_ojos
            alto_boca = ancho_antenas

            # Dibujar la cabeza
            glColor3f(202 / 255.0, 211 / 255.0, 226 / 255.0)

            glVertex2f(ANCHO_CELDA / 10, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA / 10 + ancho_cabeza, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA / 10 + ancho_cabeza, alto_piernas + alto_cuerpo + alto_cabeza)
            glVertex2f(ANCHO_CELDA / 10, alto_cuerpo + alto_piernas + alto_cabeza)

            # Dibujar antenas
            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 13 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 13 / 20 + ancho_antenas, ALTO_CELDA)
            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA)

            glVertex2f(ANCHO_CELDA * 3 / 20, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 3 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas)
            glVertex2f(ANCHO_CELDA * 3 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas / 3)
            glVertex2f(ANCHO_CELDA * 3 / 20, ALTO_CELDA - alto_antenas / 3)

            # Dibujar mitad de arriba del brazo izquierdo
            glColor3f(163 / 255.0, 168 / 255.0, 175 / 255.0)

            glVertex2f(ANCHO_CELDA * 35 / 40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 8 / 10, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 15 / 20, alto_piernas + alto_cuerpo * 3 / 4)
            glVertex2f(ANCHO_CELDA * 8 / 10, alto_piernas + alto_cuerpo * 3 / 4)

            # Dibujar cuerpo
            glColor3f(202 / 255.0, 211 / 255.0, 226 / 255.0)

            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2 / 10 + ancho_cuerpo, alto_piernas)
            glVertex2f(ANCHO_CELDA * 2 / 10 + ancho_cuerpo, alto_piernas + alto_cuerpo)
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas + alto_cuerpo)

            # Dibujar mitad de abajo de brazo izquierdo
            glColor3f(163 / 255.0, 168 / 255.0, 175 / 255.0)

            glVertex2f(ANCHO_CELDA * 35 / 40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 8 / 10, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 57 / 80, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 5 / 40)
            glVertex2f(ANCHO_CELDA * 15 / 20, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 13 / 80)

            # Dibujar brazo derecho
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas + alto_cuerpo * 3 / 4)
            glVertex2f(ANCHO_CELDA * 5 / 40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA / 20)
            glVertex2f(ANCHO_CELDA * 7 / 40, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 4 / 40)
            glVertex2f(ANCHO_CELDA * 2 / 10, alto_piernas + alto_cuerpo * 3 / 4 - ANCHO_CELDA * 3 / 40)

            # Dibujar piernas
            glVertex2f(ANCHO_CELDA * 6 / 10, 0)
            glVertex2f(ANCHO_CELDA * 6 / 10 + ancho_piernas, 0)
            glVertex2f(ANCHO_CELDA * 6 / 10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 6 / 10, alto_piernas)

            glVertex2f(ANCHO_CELDA * 3 / 10, alto_piernas / 4)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_piernas, alto_piernas / 4)
            glVertex2f(ANCHO_CELDA * 3 / 10 + ancho_piernas, alto_piernas)
            glVertex2f(ANCHO_CELDA * 3 / 10, alto_piernas)

            # Dibujar franja antenas
            glColor3f(62 / 255.0, 106 / 255.0, 181 / 255.0)

            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 13 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas * 3 / 5)
            glVertex2f(ANCHO_CELDA * 13 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas / 5)
            glVertex2f(ANCHO_CELDA * 13 / 20, ALTO_CELDA - alto_antenas / 5)

            glVertex2f(ANCHO_CELDA * 3 / 20, ALTO_CELDA - alto_antenas * 9 / 15)
            glVertex2f(ANCHO_CELDA * 3 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas * 9 / 15)
            glVertex2f(ANCHO_CELDA * 3 / 20 + ancho_antenas, ALTO_CELDA - alto_antenas * 7 / 15)
            glVertex2f(ANCHO_CELDA * 3 / 20, ALTO_CELDA - alto_antenas * 7 / 15)

            # Dibujar ojos
            glColor3f(4 / 255.0, 17 / 255.0, 40 / 255.0)

            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 9 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 9 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)
            glVertex2f(ANCHO_CELDA * 9 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)

            glVertex2f(ANCHO_CELDA * 4 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 4 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2)
            glVertex2f(ANCHO_CELDA * 4 / 20 + ancho_ojos, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)
            glVertex2f(ANCHO_CELDA * 4 / 20, ALTO_CELDA - alto_antenas - alto_cabeza / 2 + alto_ojos)

            # Dibujar boca
            glVertex2f(ANCHO_CELDA * 13 / 40 - ancho_ojos / 2, alto_piernas + alto_cuerpo + ancho_antenas)
            glVertex2f(ANCHO_CELDA * 13 / 40 - ancho_ojos / 2 + ancho_boca, alto_piernas + alto_cuerpo + ancho_antenas)
            glVertex2f(ANCHO_CELDA * 13 / 40 - ancho_ojos / 2 + ancho_boca,
                       alto_piernas + alto_cuerpo + ancho_antenas + alto_boca)
            glVertex2f(ANCHO_CELDA * 13 / 40 - ancho_ojos / 2, alto_piernas + alto_cuerpo + ancho_antenas + alto_boca)

            glEnd()
