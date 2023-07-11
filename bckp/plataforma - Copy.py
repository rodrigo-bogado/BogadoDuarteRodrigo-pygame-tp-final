import pygame
from constantes import *

class Plataforma:
    def __init__(self,ruta_plataforma) -> None:
        self.surf_plataforma = pygame.image.load(ruta_plataforma)
        self.surf_plataforma = pygame.transform.scale(self.surf_plataforma,(50,50))
        self.rect_plataforma = self.surf_plataforma.get_rect()
        self.plataformas_rect = []

    def dibujar_piso(self, ventana_juego):
        
        x = 0

        # Dibuja piso y genera rect
        for x in range(0, ANCHO_PANTALLA, self.surf_plataforma.get_width()):
            ventana_juego.blit(self.surf_plataforma, (x, ALTO_PANTALLA - self.surf_plataforma.get_height()))
            plataforma_rect = pygame.Rect(x, ALTO_PANTALLA - self.surf_plataforma.get_height(), self.surf_plataforma.get_width(), self.surf_plataforma.get_height())
            self.plataformas_rect.append(plataforma_rect)

        # Dibuja plataforma 1 y genera rect
        for x in range(200, ANCHO_PANTALLA, self.surf_plataforma.get_width()):
            ventana_juego.blit(self.surf_plataforma, (x, ALTO_PANTALLA - self.surf_plataforma.get_height() * 4))
            plataforma_rect = pygame.Rect(x, ALTO_PANTALLA - self.surf_plataforma.get_height() * 4, self.surf_plataforma.get_width(), self.surf_plataforma.get_height())
            self.plataformas_rect.append(plataforma_rect)

        # Dibuja plataforma 2 y genera rect
        for x in range(0, 600, self.surf_plataforma.get_width()):
            ventana_juego.blit(self.surf_plataforma, (x, ALTO_PANTALLA - self.surf_plataforma.get_height() * 8))
            plataforma_rect = pygame.Rect(x, ALTO_PANTALLA - self.surf_plataforma.get_height() * 8, self.surf_plataforma.get_width(), self.surf_plataforma.get_height())
            self.plataformas_rect.append(plataforma_rect)

		