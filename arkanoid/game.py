import os
import pygame as pg  # ponemos este alias para no escribir pygame todo el rato
from arkanoid import ALTO, ANCHO
from arkanoid.escenas import Portada, Partida, HallOfFame


class Arkanoid:
    def __init__(self) -> None:
        print("Arranca el juego!!")
        pg.init()  # inicializar
        self.display = pg.display.set_mode((ANCHO, ALTO))  # definir pantalla
        pg.display.set_caption('ARKANOID')
        Icon = pg.image.load(os.path.join(
            "arkanoid", "resources", "images", "ball1.png"))
        # importamos la librería "os" para que no tengamos que preocupearnos de las barras "linux/Windows"
        pg.display.set_icon(Icon)

        # Vamos a instanciar las escenas, pasa el display al constructor de escena "pantalla"
        self.escenas = [
            Portada(self.display),
            Partida(self.display),
            HallOfFame(self.display),
        ]

    def jugar(self):  # bucle principal

        for escena in self.escenas:
            escena.bucle_principal()
