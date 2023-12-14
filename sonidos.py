import pygame
from pantalla_inicio import *




pygame.mixer.init()




def sonido_proyectil():
    sonido = pygame.mixer.Sound("sonido\Disparo .mp3")
    sonido.set_volume(1)#10
    sonido.play()

def sonido_juego():
            sonido = pygame.mixer.Sound("sonido\Space Sound Arreglo.mp3")
            sonido.set_volume(0.1)#0.8
            sonido.play()

def sonido_explosion():
        sonido = pygame.mixer.Sound("sonido\Explosion .mp3")
        sonido.set_volume(1)#100
        sonido.play()
