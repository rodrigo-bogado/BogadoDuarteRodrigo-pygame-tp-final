import pygame
from pygame.locals import *
from constantes import *
from auxiliares import spritesheet_a_surfaces,draw_text
from world import snek_group,lava_group,exit_group,coin_group

class Player():
    def __init__(self,x,y):
        self.reset(10,screen_height - 200)
        # Vidas
        self.lives = 3
        self.score_objetivo = 0

    def update(self,game_over,screen,world):
        dx = 0
        dy = 0
        animation_cooldown = 2

        if game_over == 0:
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
                sound_jump.play()
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

            # Animación Salto
            if self.jumped == True:
                self.counter += 1
                if self.direction == True:
                    self.image = self.images_jump_right[self.index]
                else:
                    self.image = self.images_jump_left[self.index]

            # Delimita velocidad animación
            if self.counter > animation_cooldown: 
                self.counter = 0
                self.index += 1
                # Verifica que indice no exceda el límite
                if self.index >= len(self.images_walk_right): 
                    self.index = 0
                # Dirección derecha
                if self.direction == True: 
                    if self.idle == True:
                        self.image = self.images_idle_right[self.index] # Idle derecha
                    elif self.jumped == True:
                        self.image = self.images_jump_right[self.index] # Salta derecha
                    else:
                        self.image = self.images_walk_right[self.index] # Camina derecha
                # Dirección izquierda
                else:
                    if self.idle == True:
                        self.image = self.images_idle_left[self.index] # Idle izquierda
                    elif self.jumped == True:
                        self.image = self.images_jump_left[self.index] # Salta izquierda
                    else:
                        self.image = self.images_walk_left[self.index] # Camina izquierda

            # Gravedad

            # Gravedad aumenta linealmente
            self.vel_y += 3 

            # Velocidad límite
            if self.vel_y > 30: 
                self.vel_y = 30

            # Movimiento vertical afectado por gravedad
            dy += self.vel_y 
            
            # Detectar colisión con piso
            self.in_air = True
            for tile in world.tile_list: # Tile[0] = img, Tile[1] = Rect
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
                sound_death.play()
                game_over = -1
                self.index = 0
                self.lives -= 1

            # Detectar colisión con trampas
            if pygame.sprite.spritecollide(self, lava_group, False):
                sound_death.play()
                game_over = -1
                self.index = 0
                self.lives -= 1

            # Detectar colisión con salida
            if pygame.sprite.spritecollide(self, exit_group, False) and self.score_objetivo == 3:
                game_over = 1
            elif pygame.sprite.spritecollide(self, exit_group, False) and self.score_objetivo < 3:
                font_big = pygame.font.SysFont("Bauhaus 93", 50)
                draw_text(screen,"Conseguí todas las monedas", font_big, "Red", 180,200)
                draw_text(screen,"para el bondi antes de salir!", font_big, "Red", 180,300)

            # Limitar movimiento dentro de la zona de la pantalla
            if self.rect.left + dx < 0:  # Límite izquierdo
                dx = -self.rect.left
            elif self.rect.right + dx > screen_width:  # Límite derecho
                dx = screen_width - self.rect.right

            if self.rect.top + dy < 0:  # Límite superior
                dy = -self.rect.top

            # Actualiza posición jugador
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
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

        # Dibuja al jugador
        screen.blit(self.image, self.rect)

        # Retorna estado del juego
        return game_over

    def reset(self, x, y):
        # Lista de sprites
        ruta_carpincho_idle = "sprites\Carpincho\capi_idle.png"
        ruta_carpincho_walk = "sprites\Carpincho\capi_walk.png"
        ruta_carpincho_jump = "sprites\Carpincho\capi_jump.png"
        ruta_carpincho_death = "sprites\Carpincho\capi_death.png"
        # Idle
        self.images_idle_right = spritesheet_a_surfaces(ruta_carpincho_idle,5, 1,False,3)
        self.images_idle_left = spritesheet_a_surfaces(ruta_carpincho_idle,5, 1,True,3)
        # Walk
        self.images_walk_right = spritesheet_a_surfaces(ruta_carpincho_walk,5, 1,False,3)
        self.images_walk_left = spritesheet_a_surfaces(ruta_carpincho_walk,5, 1,True,3)
        # Jump
        self.images_jump_right = spritesheet_a_surfaces(ruta_carpincho_jump,5, 1,False,3)
        self.images_jump_left = spritesheet_a_surfaces(ruta_carpincho_jump,5, 1,True,3)
        # Death
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
