import pygame
from pygame.locals import *
from auxiliares import *
from trampas import Enemy,Lava,Exit,Coin

# Group
snek_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
dummy_coin_group = pygame.sprite.Group()

class World():
    def __init__(self, data):
        # Lista donde se almacenan los bloques  
        self.tile_list = [] 
        # Carga imagenes
        grass_tile_img = pygame.image.load("sprites\Tiles\Sliced\Tile_02.png")
        dirt_tile_img = pygame.image.load("sprites\Tiles\Sliced\Tile_14.png")
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
                    img = pygame.transform.scale(grass_tile_img,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    # Define posición en la grilla
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # Arma tupla de imagen y rectangulo
                    tile = (img,img_rect) 
                    # Guarda tuplas en lista
                    self.tile_list.append(tile) 
                # 1 = Bloque de tierra
                if tile == 2:
                    # Crea imagen y rect del tile
                    img = pygame.transform.scale(dirt_tile_img,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    # Define posición en la grilla
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # Arma tupla de imagen y rectangulo
                    tile = (img,img_rect) 
                    # Guarda tuplas en lista
                    self.tile_list.append(tile) 
                
                # 3 = Enemigo (Snek)
                if tile == 3: 
                    snek = Enemy(col_count * tile_size, row_count * tile_size)
                    snek_group.add(snek)
                # 4 = Trampa (Fuego)
                if tile == 4:
                    lava = Lava(col_count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
                # 5 = Salida (Exit)
                if tile == 5:
                    exit = Exit(col_count * tile_size, row_count * tile_size)
                    exit_group.add(exit)
                # 6 = Moneda (coin)
                if tile == 6:
                    coin = Coin(col_count * tile_size, row_count * tile_size)
                    coin_group.add(coin)                    
                
                col_count += 1
            row_count += 1

    # Dibuja piso
    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1]) # Tile[0] = img, Tile[1] = rect
    # Dibuja fondo
    def draw_bg(self,screen):
        screen.blit(sky_img,(0,0)) # Cielo
        for x in range(0,screen_width,cloud_img.get_width()):
            screen.blit(cloud_img,(x,0)) # Nubes
        for x in range(0,screen_width,mountain_img.get_width()):
            screen.blit(mountain_img,(x,0)) # Montañas
        for x in range(0,screen_width,grass_img.get_width()):
            screen.blit(grass_img,(x,screen_height - grass_img.get_height())) # Pasto