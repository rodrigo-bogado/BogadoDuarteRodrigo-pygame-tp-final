import pygame
from pygame.locals import *
import pygame.sprite
from constantes import *
from world import World,world_data
from player import Player
from enemigos import Enemy,snek_group
from trampas import Lava,lava_group
from auxiliares import Fade
from button import Button

pygame.init()

# Framerate
clock = pygame.time.Clock()
fps = 60

# Inicialización pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Carpinchos en fuga")

# Definición de instancias
world = World(world_data) # Mapa

player = Player(0,SCREEN_HEIGHT/2)

fade = Fade()

button = Button(300,200)

#Bucle principal
run = True

while run == True:

    clock.tick(fps)

    world.draw_bg(screen) # Dibuja fondo

    world.draw(screen) # Dibuja piso y plataformas

    snek_group.draw(screen) # Dibuja mob (snek)

    lava_group.draw(screen) # Dibuja trampa (lava)

    if player.game_status == 0: # Game On

        snek_group.update(screen) # Actualiza animación mob (snek)

        lava_group.update(screen) # Actualiza animación lava

    #world.draw_grid(screen) # Dibuja grilla

    player.update(screen) # Dibuja personaje

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if player.game_status == -1: # Game OFF
        
         fade.update()
         screen.blit(fade.image, fade.rect)
         button.draw(screen)

         if button.is_clicked == True:
             player.game_status = 0
             player.reset(0,SCREEN_HEIGHT/2)

    # Debug

    #print("C ",player.counter,"I ",player.index,"D ",player.direction)
    #for enemy in snek_group:
    #    print(enemy.index)
    #print(player.jumped)
    #print("Direction: ",player.direction,"Idle: ",player.idle,"Jumped: ",player.jumped)
    #print(player.rect)
    #print(button.is_hovered)
    #print(player.vel_y)

    pygame.display.update()

pygame.quit()