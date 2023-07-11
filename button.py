import pygame
from pygame.locals import *
from constantes import *

class Button():
    def __init__(self, x, y, normal, hover):
        self.image_normal = pygame.image.load(normal)
        self.image_hover = pygame.image.load(hover)
        self.rect = self.image_normal.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_hovered = False
        self.is_clicked = False

    def draw(self,screen):

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
            if pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked:
                self.is_clicked = True
        else:
            self.is_hovered = False

        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False
        
        if self.is_hovered:
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image_normal, self.rect)