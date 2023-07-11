import pygame
from pygame.locals import *
import pygame.sprite
from constantes import *
from auxiliares import spritesheet_a_surfaces

ruta_fire = r"sprites\Animated_Objects\fire\fire.png"

lava_group = pygame.sprite.Group()

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Lista de sprites
        self.images_raw = spritesheet_a_surfaces(ruta_fire,4, 1,True,4)
        self.images = []
        for image in self.images_raw:
            image = pygame.transform.scale(image,(50,50))
            self.images.append(image)
        # Indice de sprites
        self.index = 0 
        # Contador de animación
        self.counter = 0 
        # Sprite actual según índice
        self.image = self.images[self.index]
        # Rect del personaje
        self.rect = self.image.get_rect()
        # Posicion
        self.rect.x = x
        self.rect.y = y
        
    def update(self,screen):
        # Animacion
        animation_cooldown = 3
        if self.counter > animation_cooldown: # Delimita velocidad animación
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images): # Verifica que indice no exceda el límite
                self.index = 0
            self.image = self.images[self.index] # Cambia de fotograma (Der)

        self.counter += 1