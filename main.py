import pygame
from pygame.locals import *
import pygame.sprite
from constantes import *
from world import World,world_data,world_data_2
from player import Player
from enemigos import snek_group
from trampas import lava_group,exit_group
from auxiliares import Fade
from button import Button
import pygame.mixer

pygame.init()
pygame.mixer.init()

# Framerate
clock = pygame.time.Clock()
fps = 60

# Inicialización pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Carpinchos en fuga")

# inicialización BGM y efectos

ruta_carnavalito = r"sounds\carnavalito.mp3"
ruta_jump = r"sounds\jump.mp3"
ruta_death = r"sounds\death.mp3"

sound_jump = pygame.mixer.Sound(ruta_jump)
sound_death = pygame.mixer.Sound(ruta_death)

death_sound_flag = False

# Carga de imágenes botones
restart_normal = r"sprites\restart_normal.png"
restart_hover = r"sprites\restart_hover.png"
start_normal = r"sprites\start_normal.png"
start_hover = r"sprites\start_hover.png"
exit_normal = r"sprites\exit_normal.png"
exit_hover = r"sprites\exit_hover.png"

# Definición de instancias
world = World(world_data) # Mapa
world_2 = World(world_data_2) # Mapa 2
 
player = Player(0,SCREEN_HEIGHT/2) # Jugador

fade = Fade() # Efecto Fade (semi-opaco)

button_restart = Button(300,200, restart_normal, restart_hover) # Botón reinicio
button_start = Button(300,200, start_normal, start_hover) # Botón inicio
button_exit = Button(300,400, exit_normal, exit_hover) # Botón salida

#Bucle principal
run = True

main_menu = True

while run == True:

    clock.tick(fps)

    world.draw_bg(screen) # Dibuja fondo

    if main_menu == True: # Game main menu
        
         button_start.draw(screen) # Botón de Start
         button_exit.draw(screen) # Botón de exit

         if button_start.is_clicked == True: # Click = Game Start
            pygame.mixer.music.load(ruta_carnavalito)
            pygame.mixer.music.play(-1)
            player.game_status = 0 
            main_menu = False
            death_sound_flag = True
            player.reset(0,SCREEN_HEIGHT/2)

         if button_exit.is_clicked == True: # Click = Game Exit
            run = False
    else:

        if player.nivel == 1:
            
            world.draw(screen) # Dibuja piso y plataformas

        elif player.nivel == 2:

            world.generate_world(world_data)

            world_2.draw(screen) # Dibuja piso y plataformas

        snek_group.draw(screen) # Dibuja mob (snek)

        lava_group.draw(screen) # Dibuja trampa (lava)

        exit_group.draw(screen) # Dibuja salida (exit)

        player.update(screen) # Dibuja personaje
 
        if player.game_status == 0: # Game On

            snek_group.update(screen) # Actualiza animación mob (snek)

            lava_group.update(screen) # Actualiza animación lava

        if player.game_status == -1: # Game OFF
            
            if death_sound_flag == True:
                sound_death.play()
                death_sound_flag = False
            fade.update()
            screen.blit(fade.image, fade.rect)
            button_restart.draw(screen)
            button_exit.draw(screen)

            if button_restart.is_clicked == True:
                player.game_status = 0
                death_sound_flag = True
                player.reset(0,SCREEN_HEIGHT/2)

            if button_exit.is_clicked == True:
                run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and player.game_status == 0 and player.in_air == False:
            if event.key == pygame.K_SPACE:
                sound_jump.play()

    # Debug

    #print("C ",player.counter,"I ",player.index,"D ",player.direction)
    #for enemy in snek_group:
    #    print(enemy.index)
    #print(player.jumped)
    #print("Direction: ",player.direction,"Idle: ",player.idle,"Jumped: ",player.jumped)
    #print(player.rect)
    #print(button.is_hovered)
    #print(player.vel_y)
    #print(player.game_status)

    pygame.display.update()

pygame.quit()