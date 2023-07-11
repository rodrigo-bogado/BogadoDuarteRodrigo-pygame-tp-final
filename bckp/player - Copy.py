import pygame
from pygame.locals import *
from constantes import *
from auxiliares import spritesheet_a_surfaces
from world import World,world_data
from enemigos import snek_group
from trampas import lava_group

ruta_carpincho_idle = "sprites\Carpincho\capi_idle.png"
ruta_carpincho_walk = "sprites\Carpincho\capi_walk.png"
ruta_carpincho_jump = "sprites\Carpincho\capi_jump.png"
ruta_carpincho_death = "sprites\Carpincho\capi_death.png"

world = World(world_data)

class Player:
    def __init__(self, x, y):
        self.init_player(x,y)
    
    def init_player(self,x,y):    
        # Lista de sprites
        self.images_idle_right = spritesheet_a_surfaces(ruta_carpincho_idle,5, 1,False,3)
        self.images_idle_left = spritesheet_a_surfaces(ruta_carpincho_idle,5, 1,True,3)
        self.images_walk_right = spritesheet_a_surfaces(ruta_carpincho_walk,5, 1,False,3)
        self.images_walk_left = spritesheet_a_surfaces(ruta_carpincho_walk,5, 1,True,3)
        self.images_jump_right = spritesheet_a_surfaces(ruta_carpincho_jump,5, 1,False,3)
        self.images_jump_left = spritesheet_a_surfaces(ruta_carpincho_jump,5, 1,True,3)
        self.images_death_right = spritesheet_a_surfaces(ruta_carpincho_death,5, 1,False,3)
        self.images_death_left = spritesheet_a_surfaces(ruta_carpincho_death,5, 1,True,3)
        # Indice de sprites
        self.index = 0 
        # Contador de animación
        self.counter = 0 
        # Sprite actual según índice
        self.image = self.images_walk_right[self.index]
        # Rect del personaje
        self.rect = self.image.get_rect()
        # Posicion
        self.rect.x = x
        self.rect.y = y
        # Velocidad vertical
        self.vel_y = 0
        # Flag de salto
        self.jumped = False
        # Dirección PJ (True=Right, False=Left)
        self.direction = True
        # Flag anti-doble salto
        self.in_air = True
        # Idle
        self.idle = True
        # Estado del juego (0 = Activo, -1 = Perdido)
        self.game_status = 0

    def reset(self,x,y):
            self.init_player(x,y)

    def update(self,screen):

        # Delta X/Y (Dirección y magnitud horizontal y vertical)
        dx = 0
        dy = 0
        animation_cooldown = 2

        if self.game_status == 0:

            # Verifica teclas presionadas
            key = pygame.key.get_pressed()

            if key[pygame.K_RIGHT]: # Movimiento Derecha
                dx += 10
                
                self.direction = True
                self.idle = False
                if not self.jumped:
                    self.counter += 1
                    self.image = self.images_walk_right[self.index]
            if key[pygame.K_LEFT]:# Movimiento Izquierda
                dx -= 10
                
                self.direction = False
                self.idle = False
                if not self.jumped:
                    self.counter += 1
                    self.image = self.images_walk_left[self.index]
            if key[pygame.K_SPACE] and self.vel_y == 0 and not self.jumped and not self.in_air: # Salto
                self.vel_y = -30
                self.jumped = True
                self.idle = False
                #self.counter += 1
                self.index = 0
                if self.direction == True:
                    self.image = self.images_jump_right[self.index]
                else:
                    self.image = self.images_jump_left[self.index]
            if key[pygame.K_SPACE] == False: # !Salto
                self.jumped = False
            if  key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and self.jumped == False:
                self.idle = True
                self.counter += 1

            # Animación

            if self.jumped == True:
                self.counter += 1
                if self.direction == True:
                    self.image = self.images_jump_right[self.index]
                else:
                    self.image = self.images_jump_left[self.index]
            
            if self.counter > animation_cooldown: # Delimita velocidad animación
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_walk_right): # Verifica que indice no exceda el límite
                    self.index = 0
                if self.direction == True: # Dirección derecha
                    if self.idle == True:
                        self.image = self.images_idle_right[self.index]
                    elif self.jumped == True:
                        self.image = self.images_jump_right[self.index]
                    else:
                        self.image = self.images_walk_right[self.index] # Define fotograma actual (Der)
                else:
                    if self.idle == True:
                        self.image = self.images_idle_left[self.index]
                    elif self.jumped == True:
                        self.image = self.images_jump_left[self.index]
                    else:
                        self.image = self.images_walk_left[self.index] # Define fotograma actual (Izq)

            # Gravedad
            self.vel_y += 3 # Gravedad aumenta linealmente

            if self.vel_y > 30: # Velocidad límite
                self.vel_y = 30

            dy += self.vel_y # Movimiento vertical afectado por gravedad

            # Detectar colisión
            self.in_air = True
            for tile in world.tile_list:
                # Verificar colisión en eje X
                if tile[1].colliderect(self.rect.x + dx, self.rect.y,self.image.get_width(),self.image.get_height()):
                    dx = 0
                # Verificar colisión en eje Y
                if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.image.get_width(), self.image.get_height()):
                    # Verifica si está saltando
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top # Detiene movimiento al chocar con techo
                        self.vel_y = 0
                    # Verifica si está cayendo
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom # Detiene movimiento al chocar con piso
                        self.vel_y = 0
                        self.jumped = False
                        self.in_air = False

            # Detectar colisión con enemigos
            if pygame.sprite.spritecollide(self, snek_group, False):
                self.game_status = -1
                self.index = 0
            # Detectar colisión con trampas
            if pygame.sprite.spritecollide(self, lava_group, False):
                self.game_status = -1
                self.index = 0

            # Actualiza posición jugador
            self.rect.x += dx
            self.rect.y += dy

            self.valor_dx = dx

        elif self.game_status == -1:

            # Animacion muerte
            self.counter += 1
            self.animation_cooldown = 3
            if self.counter > animation_cooldown: # Delimita velocidad animación
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_death_right): # Verifica que indice no exceda el límite
                    self.index = 4
                if self.direction == True: # Dirección derecha
                    self.image = self.images_death_right[self.index]
                else:
                    self.image = self.images_death_left[self.index]

            # Gravedad

            self.vel_y += 3

            if self.vel_y > 30:
                self.vel_y = 30

            dy += self.vel_y

            # Detectar colisión con el piso
            on_ground = False
            if dy > 0:
                for tile in world.tile_list:
                    # Verificar colisión en eje Y
                    if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.image.get_width(), self.image.get_height()):
                        dy = tile[1].top - self.rect.bottom # Detiene movimiento al chocar con piso
                        on_ground = True
                        break

            # Detener movimiento vertical si está en el suelo
            if on_ground:
                self.vel_y = 0
            else:
                self.rect.y += dy

        # Muestra jugador
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen,"White",self.rect,2)
