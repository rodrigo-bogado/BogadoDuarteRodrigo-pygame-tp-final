import pygame
from pygame.locals import *
from constantes import *
from enemigos import Enemy,snek_group
from trampas import Lava,Exit,lava_group,exit_group

# Carga de imágenes
sky_img = pygame.image.load("sprites\BG\sky.png")
cloud_img = pygame.image.load("sprites\BG\cloud.png")
mountain_img = pygame.image.load("sprites\BG\mountain.png")
grass_img = pygame.image.load("sprites\BG\grass.png")
floor_tile_img = pygame.image.load("sprites\Tiles\Sliced\Tile_02.png")
dirt_tile_img = pygame.image.load("sprites\Tiles\Sliced\Tile_14.png")

# Reescalado de imágenes
sky_img = pygame.transform.scale(sky_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
cloud_img = pygame.transform.scale_by(cloud_img,3)
mountain_img = pygame.transform.scale_by(mountain_img,3)
grass_img = pygame.transform.scale_by(grass_img,4)

# Diseño mapa
# 0 = 
 
world_data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
[0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1],
[0,0,0,1,2,4,4,2,0,3,0,0,0,0,2,2],
[1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1],
]

world_data_2 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class World():
    def __init__(self,data):
        # Lista donde se almacenan los bloques  
        self.tile_list = [] 
        
        # Selecciona y almacena rects según el world_data
        row_count = 0
        # Itera filas
        for row in data: 
            col_count = 0
            # Itera columnas
            for tile in row: 
                # 1 = Bloque de tierra con pasto
                if tile == 1:
                    # Crea imagen y rect del tile
                    img = pygame.transform.scale(floor_tile_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    # Define posición en la grilla
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    # Arma tupla de imagen y rectangulo
                    tile = (img,img_rect) 
                    # Guarda tuplas en lista
                    self.tile_list.append(tile) 
                # 1 = Bloque de tierra
                if tile == 2:
                    # Crea imagen y rect del tile
                    img = pygame.transform.scale(dirt_tile_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    # Define posición en la grilla
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    # Arma tupla de imagen y rectangulo
                    tile = (img,img_rect) 
                    # Guarda tuplas en lista
                    self.tile_list.append(tile) 
                # 3 = Enemigo (Snek)
                if tile == 3: 
                    snek = Enemy(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    snek_group.add(snek)
                # 4 = Trampa (Fuego)
                if tile == 4:
                    lava = Lava(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    lava_group.add(lava)
                # 5 = Salida (Exit)
                if tile == 5:
                    exit = Exit(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    exit_group.add(exit)
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

    def generate_world(self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                # Resto del código para generar los tiles
                # ...
                col_count += 1
            row_count += 1

    
    # Dibuja grilla de rects
    '''
    def draw_grid(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, "White",tile[1], 2)
    '''
    