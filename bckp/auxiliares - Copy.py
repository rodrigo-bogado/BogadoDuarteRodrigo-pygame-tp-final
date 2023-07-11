import pygame
from pygame.locals import *
from constantes import *

def spritesheet_a_surfaces(ruta,columnas, filas,flip,escala):
    '''
    Convierte una imagen de sprites en una lista de superficies individuales.

    Parámetros:
        ruta (str): Ruta de la imagen de sprites.
        columnas (int): Número de columnas en la hoja de sprites.
        filas (int): Número de filas en la hoja de sprites.
        flip (bool): Indica si se debe voltear horizontalmente cada superficie.
        escala (float): Factor de escala para redimensionar la imagen de sprites.

    Retorna:
        list: Lista de superficies individuales de cada fotograma.    
    '''
    #flip = False
    lista_fotogramas = []
    surface_imagen = pygame.image.load(ruta)

    surface_imagen = pygame.transform.scale(surface_imagen, (surface_imagen.get_width() * escala, surface_imagen.get_height() * escala))

    fotograma_ancho = int(surface_imagen.get_width() / columnas)
    fotograma_alto = int(surface_imagen.get_height() / filas)

    x = 0

    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            if flip == True:
                surface_fotograma_espejado = pygame.transform.flip(surface_fotograma,True,False)
                lista_fotogramas.append(surface_fotograma_espejado)
            else:
                lista_fotogramas.append(surface_fotograma)

    return lista_fotogramas

class Fade(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.display.get_surface().get_rect()
        self.image = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
        self.alpha = 0
        self.direction = 8

    def update(self):
        self.image.fill((0, 0, 0, self.alpha))
        self.alpha += self.direction
        if self.alpha > 200:
            self.alpha = 200  # Limita el valor máximo de transparencia