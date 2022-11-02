import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemigo

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()

clock = pygame.time.Clock()
delta_ms = clock.tick(FPS)

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\images\\locations\\city\\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player1 = Player(x=400,y=0,speed_walk=4,speed_run=8,gravity=10,jump_power=25,jump_height=150,frame_rate_ms=80,move_rate_ms=40)

enemy1 = Enemigo(x=800,y=0,speed_walk=2,speed_run=4,gravity=10,frame_rate_ms=80,move_rate_ms=40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    keys = pygame.key.get_pressed()
        
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    
    player1.events(delta_ms,keys)   
    player1.update(delta_ms)
    player1.draw(screen)

    enemy1.update(delta_ms)
    enemy1.draw(screen)
     
    pygame.display.flip()
    