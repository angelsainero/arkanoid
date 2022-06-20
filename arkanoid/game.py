import pygame as pg  # ponemos este alias para no escribir pygame todo el rato
from arkanoid import ALTO, ANCHO
import os
# Directorio del juego
carpeta_juego = os.path.dirname(__file__)
carpeta_recursos = os.path.join(carpeta_juego, "resources")
carpeta_recursos_imagenes = os.path.join(carpeta_recursos, "images")
pg.display.set_caption('ARKANOID')
Icon = pg.image.load(os.path.join(
    carpeta_recursos_imagenes, "arkanoid_name.png"))
pg.display.set_icon(Icon)


class Arkanoid:
    def __init__(self) -> None:
        print("Arranca el juego!!")
        pg.init()  # inicializar
        self.display = pg.display.set_mode((ANCHO, ALTO))  # definir pantalla

    def jugar(self):  # bucle principal
        salir = False
        while not salir:  # mientras no tengamos que salir nos quedamos en el bucle
            for event in pg.event.get():  # detectamos los eventos
                if event.type == pg.QUIT:  # si el tipo de evento es el del QUIT saliamos del bucle
                    salir = True

            self.display.fill((99, 99, 99))  # pintamos la pantalla de un color
            pg.display.flip()  # para ver lo que pintamos
