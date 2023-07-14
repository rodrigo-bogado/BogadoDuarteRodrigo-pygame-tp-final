import pygame.mixer

pygame.mixer.init()

# Dimensiones pantalla

screen_width = 800
screen_height = 600

# Variables de tiempo
clock = pygame.time.Clock()
fps = 60

# Define variables

tile_size = 50
game_over = 0
main_menu = True
level = 1
score = 0
#score_objetivo = 0
#flag_objetivo = False

# Ruta imagenes
ruta_snek_idle = "sprites\enemies\snek_idle.png"
ruta_fire = r"sprites\Animated_Objects\fire\fire.png"
ruta_exit = r"sprites\door.png"
ruta_coin = r"sprites\Animated_Objects\Coin\Coin.png"

# inicialización BGM y efectos
ruta_carnavalito = r"sounds\carnavalito.mp3"
ruta_marchafunebre = r"sounds\gameover.mp3"
ruta_jump = r"sounds\jump.mp3"
ruta_death = r"sounds\death.mp3"

sound_jump = pygame.mixer.Sound("sounds\jump.mp3")
sound_death = pygame.mixer.Sound("sounds\death.mp3")
sound_coin = pygame.mixer.Sound("sounds\coin.mp3")
sound_marchafunebre = pygame.mixer.Sound("sounds\gameover.mp3")

# Define colores
white = (255,255,255)
green = (34,139,34)
red = (255,0,0)

# Carga de imágenes
sky_img = pygame.image.load("sprites\BG\sky.png")
cloud_img = pygame.image.load("sprites\BG\cloud.png")
mountain_img = pygame.image.load("sprites\BG\mountain.png")
grass_img = pygame.image.load("sprites\BG\grass.png")
heart_img = pygame.image.load("sprites\heart.png")

# Reescalado de imágenes
sky_img = pygame.transform.scale(sky_img,(screen_width,screen_height))
cloud_img = pygame.transform.scale_by(cloud_img,3)
mountain_img = pygame.transform.scale_by(mountain_img,3)
grass_img = pygame.transform.scale_by(grass_img,4)

# Carga de imágenes botones
restart_normal = r"sprites\restart_normal.png"
restart_hover = r"sprites\restart_hover.png"
start_normal = r"sprites\start_normal.png"
start_hover = r"sprites\start_hover.png"
exit_normal = r"sprites\exit_normal.png"
exit_hover = r"sprites\exit_hover.png"
