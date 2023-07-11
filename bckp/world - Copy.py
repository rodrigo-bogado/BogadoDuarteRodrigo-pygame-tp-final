import pygame
from pygame.locals import *
from constantes import *
from enemigos import Enemy,snek_group
from trampas import Lava,lava_group

# Carga de imágenes

sky_img = pygame.image.load("sprites\BG\sky.png")
cloud_img = pygame.image.load("sprites\BG\cloud.png")
mountain_img = pygame.image.load("sprites\BG\mountain.png")
grass_img = pygame.image.load("sprites\BG\grass.png")
floor_tile_img = pygame.image.load("sprites\Tiles\Sliced\Tile_02.png")

# Reescalado de imágenes

sky_img = pygame.transform.scale(sky_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
cloud_img = pygame.transform.scale_by(cloud_img,3)
mountain_img = pygame.transform.scale_by(mountain_img,3)
grass_img = pygame.transform.scale_by(grass_img,4)

# Diseño mapa

world_data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,1,1,3,3,1,0,2,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class World():
    def __init__(self,data):

        self.tile_list = []
        
        row_count = 0

        # Almacena rects según el world_data
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1: # Bloque de tierra
                    img = pygame.transform.scale(floor_tile_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()

                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE

                    tile = (img,img_rect) # Arma tupla de imagen y rectangulo
                    self.tile_list.append(tile) # Guarda tuplas en lista
                if tile == 2: # Mob 1 (snek)
                    snek = Enemy(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    snek_group.add(snek)
                if tile == 3: # Fuego
                    lava = Lava(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    lava_group.add(lava)
                col_count += 1
            row_count += 1

    # Dibuja fondo
    def draw_bg(self,screen):
        screen.blit(sky_img,(0,0)) # Cielo
        for x in range(0,SCREEN_WIDTH,cloud_img.get_width()):
            screen.blit(cloud_img,(x,0)) # Nubes
        for x in range(0,SCREEN_WIDTH,mountain_img.get_width()):
            screen.blit(mountain_img,(x,0)) # Montañas
        for x in range(0,SCREEN_WIDTH,grass_img.get_width()):
            screen.blit(grass_img,(x,SCREEN_HEIGHT - grass_img.get_height())) # Pasto
    
    # Dibuja piso y plataformas
    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1]) # Tile[0] = img, Tile[1] = rect

    
    # Dibuja grilla de rects
    '''
    def draw_grid(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, "White",tile[1], 2)
    '''
    