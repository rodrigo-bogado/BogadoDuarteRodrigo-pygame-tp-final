import pygame
from pygame.locals import *
from constantes import *

class Button():
    def __init__(self, x, y, normal, hover):
        # Carga imágenes
        self.image_normal = pygame.image.load(normal)
        self.image_hover = pygame.image.load(hover)
        # Rect imagen
        self.rect = self.image_normal.get_rect()
        # Posición
        self.rect.x = x
        self.rect.y = y
        # Estados del botón
        self.is_hovered = False
        self.is_clicked = False

    def draw(self,screen):
        action = False
        # Posicion Mouse
        mouse_pos = pygame.mouse.get_pos()  
        # Mouse sobre botón
        if self.rect.collidepoint(mouse_pos): 
            self.is_hovered = True
            # Mouse clickea botón
            if pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked: 
                action = True
                self.is_clicked = True
        else:
            self.is_hovered = False
        # Permite un solo click a la vez
        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False
        # Cambia imagen según estado del botón
        if self.is_hovered:
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image_normal, self.rect)
        
        return action