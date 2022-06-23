import os
import pygame as pg
# importamos esta también para no tener que poner pygame.sprite y poder poner sprite
from pygame.sprite import Sprite
from . import ALTO, ANCHO


'''
1. Creamos una clase Raqueta
    a. Sea un Sprite
    b. el metudo update es el que se encarga de gestionarla
2. Situarlo con las coordenadas y para eso, obtener el rectangulo
3. método mostrar_paleta para pintar 
4. en el bucle principal llamar a mostrar_paleta

Para animar las imágenes: 
1. Funcion "animar" con una lista de imágenes y las mostramos en bucle
'''


class Raqueta(Sprite):
    margen_inferior = 20

    def __init__(self):
        super().__init__()
        self.sprites = [
            pg.image.load(os.path.join("arkanoid", "resources",
                          "images", "electric00.png")),
            pg.image.load(os.path.join("arkanoid", "resources",
                          "images", "electric01.png")),
            pg.image.load(os.path.join("arkanoid", "resources",
                          "images", "electric02.png")),
        ]

        self.contador = 0
        image_path = os.path.join(
            "arkanoid", "resources", "images", "electric00.png")
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))
        # quiero obtener el rectángulo de la imagen

    # creamos este condicional para darle movimiento a la electricidad de la raqueta.
    def update(self):

        pulsado = pg.key.get_pressed()
        if pulsado[pg.K_LEFT]:
            self.rect.x = self.rect.x - 2
        if pulsado[pg.K_RIGHT]:
            self.rect.x = self.rect.x + 2

        self.image = self.sprites[self.contador]
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
