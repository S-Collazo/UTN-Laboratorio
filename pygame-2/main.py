import pygame
import sys
from pygame.locals import *
from constantes import *
from personaje import Player
from enemigo import Enemy
from plataforma import Platform

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()
delta_ms = clock.tick(FPS)

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\images\\locations\\set_bg_01\\city\\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(asset="cowgirl",x=400,y=0,gravity=10,frame_rate_ms=80,move_rate_ms=40)

enemy_1 = Enemy(asset="cowgirl",x=800,y=0,gravity=10,frame_rate_ms=80,move_rate_ms=40)

lista_personajes = []
lista_personajes.append(player_1)

lista_enemigos = []
lista_enemigos.append(enemy_1)

lista_plataformas = []
lista_plataformas.append(Platform(0,GROUND_LEVEL,ANCHO_VENTANA,GROUND_RECT_H,1))
lista_plataformas.append(Platform(x=400,y=500,w=50,h=50,type=0))
lista_plataformas.append(Platform(x=450,y=500,w=50,h=50,type=1))
lista_plataformas.append(Platform(x=500,y=500,w=50,h=50,type=2))   
lista_plataformas.append(Platform(x=600,y=430,w=50,h=50,type=12))
lista_plataformas.append(Platform(x=650,y=430,w=50,h=50,type=14))
lista_plataformas.append(Platform(x=750,y=360,w=50,h=50,type=12))
lista_plataformas.append(Platform(x=800,y=360,w=50,h=50,type=13))
lista_plataformas.append(Platform(x=850,y=360,w=50,h=50,type=13))
lista_plataformas.append(Platform(x=900,y=360,w=50,h=50,type=14))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    keys = pygame.key.get_pressed()
        
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
        
    player_1.events(delta_ms,keys)   
    player_1.update(delta_ms,lista_plataformas,lista_enemigos)
    player_1.draw(screen)

    if(enemy_1.lives > 0):
        enemy_1.update(delta_ms,lista_plataformas,lista_personajes)
        enemy_1.draw(screen)
        
    for plataforma in lista_plataformas:
        Platform.draw(plataforma,screen)
         
    pygame.display.flip()