
from arkanoid import ANCHO, ALTO
from arkanoid.game import Arkanoid

if __name__ == "__main__":
    print(f"El tamaño es {ANCHO} x {ALTO}")
    juego = Arkanoid()
    juego.jugar()
