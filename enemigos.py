import pygame
from pygame.locals import *
import pygame.sprite
from constantes import *
from auxiliares import spritesheet_a_surfaces

ruta_snek_idle = "sprites\Carpincho\snek_idle.png"

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Lista de sprites
        self.images_idle_left = spritesheet_a_surfaces(ruta_snek_idle,10, 1,True,4)
        self.images_idle_right = spritesheet_a_surfaces(ruta_snek_idle,10, 1,False,4)
        # Indice de sprites
        self.index = 0 
        # Contador de animación
        self.counter = 0 
        # Sprite actual según índice
        self.image = self.images_idle_left[self.index]
        # Rect del personaje
        self.rect = self.image.get_rect()
        # Posicion
        self.rect.x = x
        self.rect.y = y
        # Dirección de movimiento ([+] -> Derecha)
        self.move_direction = 1
        self.move_counter = 0

    def update(self,screen):
        # Animacion
        animation_cooldown = 2
        if self.counter > animation_cooldown: # Delimita velocidad animación
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_idle_left): # Verifica que indice no exceda el límite
                self.index = 0
        if self.move_direction > 0:
            self.image = self.images_idle_right[self.index] # Cambia de fotograma (Der)
        else:
            self.image = self.images_idle_left[self.index] # Cambia de fotograma (Izq)
        self.counter += 1

        # Movimiento

        self.rect.x += self.move_direction # Mueve enemigo
        self.move_counter += 1
        if self.move_counter > 100: # Distancia de movimiento
            self.move_direction *= -1 # Invierte la dirección
            self.move_counter = 0
