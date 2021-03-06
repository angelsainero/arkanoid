import os
from re import A
import pygame as pg
# importamos esta también para no tener que poner pygame.sprite y poder poner sprite
from pygame.sprite import Sprite
from . import ALTO, ANCHO, FPS


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
    velocidad = 5
    fps_animacion = 12
    # cada 5 cambios de posición hay cambio de imagen
    limite_iteracion = FPS // fps_animacion
    iteracion = 0  # nos guardamos la iteracion

    def __init__(self):
        super().__init__()

        # construimos la animación de la raqueta iterando
        self.sprites = []
        for i in range(3):
            self.sprites.append(
                pg.image.load(
                    os.path.join("arkanoid", "resources",
                                 "images", f"electric0{i}.png")
                )
            )

        self.siguiente_imagen = 0
        self.image = self.sprites[self.siguiente_imagen]

        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))
        # quiero obtener el rectángulo de la imagen

    # creamos este condicional para darle movimiento a la electricidad de la raqueta.

    def update(self):
        # damos movimiento a la paleta y limitamos con las propiedades de rect para que no se salga.
        pulsado = pg.key.get_pressed()
        if pulsado[pg.K_RIGHT]:
            self.rect.x = self.rect.x + self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if pulsado[pg.K_LEFT]:
            self.rect.x = self.rect.x - self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0

    # Animamos el rayo de la raqueta (creamos un bucle para que cambie de imagen cada FPS / fps animacion (5 bucles))

                # fps_animacion = 12
                # cada 5 cambios de posición hay cambio de imagen
                # limite_iteracion = FPS / fps_animacion
                # iteracion = 0

        self.iteracion += 1
        if self.iteracion == self.limite_iteracion:
            self.siguiente_imagen += 1
            # cuando llega a la tercera imagen vuelve a 0
            if self.siguiente_imagen >= len(self.sprites):
                self.siguiente_imagen = 0
            self.image = self.sprites[self.siguiente_imagen]
            self.iteracion = 0


'''
1 Crear una clase ladrillo que hereda de Sprite
2 Importar las imágenes
3 Crear objetos "ladrillo" y darles posición
    "calcular para cada ladrillo su posición respecto al anterior para no solapar"
'''


class Ladrillo(Sprite):
    def __init__(self, fila, columna):  # necesitaremos la x e y para posicionarlos en el muro
        super().__init__()

        ladrillo_verde = os.path.join(
            "arkanoid", "resources", "images", "greenTile.png")
        self.image = pg.image.load(ladrillo_verde)
        ancho = self.image.get_width()
        alto = self.image.get_height()
        self.rect = self.image.get_rect(x=columna * ancho, y=fila * alto)


class Pelota(Sprite):

    velocidad_x = 5
    velocidad_y = -5

    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(
            os.path.join("arkanoid", "resources", "images", "ball1.png")
        )
        self.rect = self.image.get_rect(**kwargs)

    def update(self, raqueta, juego_iniciado):
        if not juego_iniciado:
            self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)
        else:  # damos movimiento a la pelotita tras iniciar el juego con Space
            self.rect.x += self.velocidad_x
            if self.rect.right > ANCHO or self.rect.left < 0:
                # si se sale de la pantalla rebota, con el cambio de signo en la x y en la y
                self.velocidad_x = -self.velocidad_x
            self.rect.y += self.velocidad_y
            if self.rect.top <= 0:
                self.velocidad_y = -self.velocidad_y

            if self.rect.top > ALTO:
                self.pierdes()
                self.reset()

    def pierdes(self):
        print("Pierdes una vida")

    def reset(self):
        print("Recolocamos la pelota a su posición inicial")
