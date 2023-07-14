import pygame
from pygame.locals import *
import pygame.sprite
import pygame.mixer
from auxiliares import draw_text
from player import Player
from world import World,snek_group,lava_group,coin_group,exit_group,dummy_coin_group
from trampas import Coin, Heart
from constantes import *
from button import Button
from niveles import *

pygame.init()
pygame.mixer.init()

#Inicializa pantalla
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Carpinchos en fuga")

#BGM
pygame.mixer.music.load(ruta_carnavalito)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1, 0.0, 0)

# Define fuentes
font_score = pygame.font.SysFont("Tahoma", 30)
font_big = pygame.font.SysFont("Bauhaus 93", 70)
font_title = pygame.font.SysFont("Impact", 70)

# Reinicia la instancia de world y sus componentes
def reset_level(level):
    player.reset(50, screen_height - 100)
    snek_group.empty()
    lava_group.empty()
    coin_group.empty()
    exit_group.empty()
    if level == 1:
        world_data = level_1
        world = World(world_data)
    if level == 2:
        world_data = level_2
        world = World(world_data)
    if level == 3:
        world_data = level_3
        world = World(world_data)

    return world

# Define instancia del mundo
if level == 1:
    world_data = level_1
    world = World(world_data)
if level == 2:
    world_data = level_2
    world = World(world_data)
if level == 3:
    world_data = level_3
    world = World(world_data)

# Instancia del jugador
player = Player(100,screen_height - 200)

# Crear botones
restart_button = Button(310, 350, restart_normal,restart_hover)
start_button = Button(310, 200, start_normal,start_hover)
exit_button = Button(310, 400, exit_normal,exit_hover)

# Moneda del contador
score_coin = Coin(10, 10)
heart_icon = Heart(150,10)
dummy_coin_group.add(score_coin)
dummy_coin_group.add(heart_icon)

# Bucle principal
run = True

while run:

    clock.tick(fps)

    # Dibuja fondo
    world.draw_bg(screen)

    # Menú principal al comenzar
    if main_menu == True:
        draw_text(screen,"Carpinchos en fuga!", font_title, "White", 130,50)
        draw_text(screen,"Escapá del Delta antes de que te coman!", font_score, "White", 140,130)
        # Botón de salir
        if exit_button.draw(screen):
            run = False
        # Botón de comenzar
        if start_button.draw(screen):
            main_menu = False
    else:
        # Dibuja tiles del mundo
        world.draw(screen)

        # Si el personaje está vivo
        if game_over == 0:

            # Actualiza todos los grupos
            snek_group.update()
            lava_group.update(screen)
            coin_group.update(screen)
            dummy_coin_group.update(screen)

            # Si colisiona con monedas
            if pygame.sprite.spritecollide(player,coin_group, True):
                sound_coin.play()
                score += 1
                player.score_objetivo += 1
            draw_text(screen,"X " + str(score), font_score, white, 70, 13)
            draw_text(screen,"X " + str(player.lives), font_score, white, 210, 13)

        # Dibuja todos los grupos    
        snek_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)
        dummy_coin_group.draw(screen)

        # Actualiza jugador y define estado del juego
        game_over = player.update(game_over,screen,world)

        # Si el jugador muere y quedan vidas
        if game_over == -1 and player.lives > 0:
            draw_text(screen,"-1 LIFE :(", font_big, red, 250,200)
            # Boton de reinicio
            if restart_button.draw(screen):
                # Se reinicia instancia del jugador
                player.reset(10, screen_height - 200)
                game_over = 0
        # Si el jugador muere y NO quedan vidas
        elif game_over == -1 and player.lives == 0:
            draw_text(screen,"GAME OVER :(", font_big, red, 250,200)
            # Boton de reinicio
            if restart_button.draw(screen):
                level = 1
                #reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0
                player.lives = 2

        # Si el jugador completa el nivel
        if game_over == 1:
            player.score_objetivo = 0
            level += 1
            # Reinicia instancia del mundo y pasa al siguiente
            if level <= 3:
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                # Si es el último nivel reinicia al primero.
                draw_text(screen,"CARPINCHULATIONS!", font_big, green, 150,80)
                draw_text(screen,"Pudiste escapar del delta", font_big, "White", 110,120)
                draw_text(screen,"tomando el 453 ramal 2!", font_big, "White", 110,160)
                if restart_button.draw(screen):
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #DEBUG

    print(player.score_objetivo)

    pygame.display.update()

pygame.quit()