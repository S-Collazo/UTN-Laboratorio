import pygame
import sys
from constantes import *
from personaje import Player
from enemigo import Enemy
from plataforma import Platform

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()

clock = pygame.time.Clock()
delta_ms = clock.tick(FPS)

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\images\\locations\\city\\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(x=400,y=0,gravity=10,frame_rate_ms=80,move_rate_ms=40)

enemy_1 = Enemy(x=800,y=0,speed_walk=2,speed_run=4,gravity=10,frame_rate_ms=80,move_rate_ms=40)

lista_enemigos = []
lista_enemigos.append(enemy_1)

lista_plataformas = []
lista_plataformas.append(Platform(500,500,50,50,1))
lista_plataformas.append(Platform(550,500,50,50,1))
lista_plataformas.append(Platform(0,GROUND_LEVEL,ANCHO_VENTANA,GROUND_RECT_H,1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    keys = pygame.key.get_pressed()
        
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
        
    if(player_1.lives > 0):
        player_1.events(delta_ms,keys)   
        player_1.update(delta_ms,lista_plataformas,lista_enemigos)
        player_1.draw(screen)

        if(enemy_1.enemy_lives > 0):
            enemy_1.update(delta_ms,lista_plataformas)
            enemy_1.draw(screen)
        
        for plataforma in lista_plataformas:
            Platform.draw(plataforma,screen)
    else:
        screen.fill(BLACK)
         
    pygame.display.flip()
    