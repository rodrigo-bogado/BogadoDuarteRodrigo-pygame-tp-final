import pygame
from pygame.locals import *
import pygame.sprite
from auxiliares import spritesheet_a_surfaces
from constantes import *

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

    def update(self):
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

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Carga y escalado de imagen
        self.image = pygame.image.load(ruta_exit)
        self.image = pygame.transform.scale(self.image,(50,50))
        # Rect de la salida
        self.rect = self.image.get_rect()
        # Posicion
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Lista de sprites
        self.images_raw = spritesheet_a_surfaces(ruta_coin,5, 1,False,4)
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

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Sprite actual según índice
        self.image = heart_img
        # Rect del personaje
        self.rect = self.image.get_rect()
        # Posicion
        self.rect.x = x
        self.rect.y = y