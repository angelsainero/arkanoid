import pygame as pg


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
    def bucle_principal(self):
        salir = False
        while not salir:  # mientras no tengamos que salir nos quedamos en el bucle
            for event in pg.event.get():  # detectamos los eventos
                if event.type == pg.QUIT:  # si el tipo de evento es el del QUIT saliamos del bucle
                    salir = True

            # pintamos la pantalla de un color
            self.pantalla.fill((99, 0, 0))
            pg.display.flip()  # para ver lo que pintamos


class Partida(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:  # mientras no tengamos que salir nos quedamos en el bucle
            for event in pg.event.get():  # detectamos los eventos
                if event.type == pg.QUIT:  # si el tipo de evento es el del QUIT saliamos del bucle
                    salir = True

            # pintamos la pantalla de un color
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()  # para ver lo que pintamos


class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:  # mientras no tengamos que salir nos quedamos en el bucle
            for event in pg.event.get():  # detectamos los eventos
                if event.type == pg.QUIT:  # si el tipo de evento es el del QUIT saliamos del bucle
                    salir = True

            # pintamos la pantalla de un color
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()  # para ver lo que pintamos
