import pygame
import sys
from pygame.locals import *
from constantes import *
from personaje import Player
from enemigo import Enemy
from plataforma import Platform
from bala import Bullet
from nivel import Level
from auxiliar import Auxiliar

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\images\\locations\\set_bg_06\\creepy_forest.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(asset="knight_main",x=400,y=GROUND_LEVEL-100,gravity=10,frame_rate_ms=50,move_rate_ms=20)

enemy_1 = Enemy(asset="bronze_knight",x=800,y=0,gravity=10,frame_rate_ms=50,move_rate_ms=20)

lista_personajes = []
lista_personajes.append(player_1)

lista_enemigos = []
lista_enemigos.append(enemy_1)

lista_plataformas = []
lista_plataformas.append(Platform(x=0,y=GROUND_LEVEL,w=ANCHO_VENTANA,h=GROUND_RECT_H,type=1))
Level.create_plaforms(lista_plataformas,x=250,y=550,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=400,y=500,w=100,h=100,tile_total=10,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=900,y=450,w=100,h=100,tile_total=3,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=725,y=375,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=350,y=350,w=100,h=100,tile_total=7,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=200,y=250,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=400,y=200,w=100,h=100,tile_total=17,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=0,y=125,w=100,h=100,tile_total=7,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=0,y=450,w=100,h=100,tile_total=3,p_scale=0.4,collition_enabled=True)

lista_balas = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    keys = pygame.key.get_pressed()
    
    delta_ms = clock.tick(FPS)
        
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    
    for plataforma in lista_plataformas:
        Platform.draw(plataforma,screen)
       
    player_1.events(delta_ms,keys,lista_balas)
    player_1.update(delta_ms,lista_plataformas,lista_enemigos)
    player_1.draw(screen)
    
    for bala in lista_balas:
        Bullet.draw(bala,screen)
        Bullet.update(bala,delta_ms,lista_enemigos,lista_plataformas)

    if(enemy_1.lives > 0):
        enemy_1.update(delta_ms,lista_plataformas,lista_personajes,lista_balas)
        enemy_1.draw(screen)
                        
    if(DEBUG):
        Auxiliar.drawGrid(screen,100)
   
    # screen.fill(FILTER_PURPLE,imagen_fondo.get_rect(),BLEND_RGBA_ADD)
         
    pygame.display.flip()