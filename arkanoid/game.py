import pygame
from arkanoid import ALTO, ANCHO

class Arkanoid:
    def __init__(self) -> None:
        print("Arranca el juego!!")
        pygame.init() #inicializar 
        self.display=pygame.display.set_mode((ANCHO, ALTO)) #definir pantalla 
    
    def jugar(self): #bucle principal
        salir = False 
        while not salir: #mientras no tengamos que salir nos quedamos en el bucle
            for event in pygame.event.get(): #detectamos los eventos 
                if event.type == pygame.QUIT: #si el tipo de evento es el del QUIT saliamos del bucle
                    salir=True

            self.display.fill((99,99,99)) #pintamos la pantalla de un color
            pygame.display.flip() #para ver lo que pintamos 


