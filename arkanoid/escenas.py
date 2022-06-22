import os
import pygame as pg
from . import ANCHO, ALTO, COLOR_MENSAJE
import arkanoid  # importo el ancho y alto


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        '''
        este método debe ser implementado por cada una de las escenas
        en funcion de lo que estén esperando hasta la condiciona de salida
        '''
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        # como es una clase que hereda de otra hay que llamar al constructor de la clase padre
        super().__init__(pantalla)
        self.logo = pg.image.load(os.path.join(
            "arkanoid", "resources", "images", "arkanoid_name.png"))
        # importamos la librería "os" para que no tengamos que preocupearnos de las barras "linux/Windows"
        font_file = os.path.join(
            "arkanoid", "resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(font_file, 40)  # cargamos la tipografía

    def pintar_texto(self):
        mensaje = "Pulsa Espacio para empezar"
        # renderizamos un texto con la tipografía, true antialias
        texto = self.tipografia.render(mensaje, True, COLOR_MENSAJE)
        ancho_texto = texto.get_width()  # obtengo el ancho para los calculos
        pos_x = (ANCHO - ancho_texto) / 2
        pos_y = 3/4 * ALTO
        # pintamos.... aunque también podrías ser pg.Surface.blit(.....)
        self.pantalla.blit(texto, (pos_x, pos_y))

    def bucle_principal(self):
        salir = False
        while not salir:  # mientras no tengamos que salir nos quedamos en el bucle
            for event in pg.event.get():  # detectamos los eventos
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:  # si el tipo de evento es el del QUIT saliamos del bucle
                    pg.quit()

            # pintamos la pantalla de un color
            self.pantalla.fill((0, 0, 0))

            self.pintar_logo()
            self.pintar_texto()

            pg.display.flip()  # para ver lo que pintamos

    def pintar_logo(self):
        # creamos un métido para pintar el logo y luego meterlo en el bucle ppal de portada
        ancho_logo = self.logo.get_width()
        # con esto tenemos la posición centrada, me he tenido que importar ANCHO
        pos_x = (ANCHO-ancho_logo) / 2
        pos_y = ALTO / 3
        self.pantalla.blit(self.logo, (pos_x, pos_y))


class Partida(Escena):  # Creamos el constructor de Partida para poner el background
    def __init__(self, pantalla):
        super().__init__(pantalla)
        bg_file = os.path.join(
            "arkanoid", "resources", "images", "background.jpg")
        # nos guardamos self.fondo porque lo usaremos en el método de pintar_fondo
        self.fondo = pg.image.load(bg_file)

    def bucle_principal(self):
        salir = False
        while not salir:  # mientras no tengamos que salir nos quedamos en el bucle
            for event in pg.event.get():  # detectamos los eventos
                if event.type == pg.QUIT:  # si el tipo de evento es el del QUIT saliamos del bucle
                    pg.quit()

            # pintamos la pantalla de un color
            self.pantalla.fill((0, 99, 0))
            self.pintar_fondo()
            pg.display.flip()  # para ver lo que pintamos

    def pintar_fondo(self):
        self.pantalla.blit(self.fondo, (0, 0))


class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:  # mientras no tengamos que salir nos quedamos en el bucle
            for event in pg.event.get():  # detectamos los eventos
                if event.type == pg.QUIT:  # si el tipo de evento es el del QUIT saliamos del bucle
                    pg.quit()

            # pintamos la pantalla de un color
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()  # para ver lo que pintamos
