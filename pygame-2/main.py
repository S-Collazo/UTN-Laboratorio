import pygame
import sys
from pygame.locals import *
from constants import *
from player import Player
from enemy import Enemy
from enemy_goblin import *
from plataform import Platform
from bullet import Bullet
from trap import Trap
from level import Level
from item import Health_Potion
from auxiliar import Auxiliar

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\locations\\set_bg_06\\creepy_forest.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_list = Auxiliar.readJson("player_list.json")
lista_personajes = []
player_1 = Player(asset=player_list,name="Iron Knight",x=400,y=GROUND_LEVEL-100,gravity=10,frame_rate_ms=60,move_rate_ms=40)
lista_personajes.append(player_1)

enemy_list = Auxiliar.readJson("enemy_list.json")
lista_enemigos = []
enemy_1 = Goblin_Standard(asset=enemy_list,x=501,y=GROUND_LEVEL-100,gravity=10,frame_rate_ms=60,move_rate_ms=40,p_scale=0.2)
enemy_2 = Goblin_Grunt(asset=enemy_list,x=550,y=50,gravity=10,frame_rate_ms=80,move_rate_ms=40,p_scale=0.2)
enemy_3 = Goblin_Shaman(asset=enemy_list,x=100,y=1,gravity=10,frame_rate_ms=80,move_rate_ms=40,p_scale=0.2)
lista_enemigos.append(enemy_1)
lista_enemigos.append(enemy_2)
lista_enemigos.append(enemy_3)

lista_entidades = lista_personajes + lista_enemigos

lista_plataformas = []
lista_plataformas.append(Platform(x=0,y=GROUND_LEVEL,w=ANCHO_VENTANA,h=GROUND_RECT_H,type=1))
Level.create_plaforms(lista_plataformas,x=250,y=550,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=400,y=500,w=100,h=100,tile_total=10,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=900,y=450,w=100,h=100,tile_total=3,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=725,y=375,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=350,y=350,w=100,h=100,tile_total=7,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=200,y=275,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=400,y=200,w=100,h=100,tile_total=17,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=0,y=125,w=100,h=100,tile_total=7,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=0,y=450,w=100,h=100,tile_total=3,p_scale=0.4,collition_enabled=True)

lista_trampas = []
trampa_1 = Trap(x=10,y=375,w=50,h=50,p_scale=0.4)
lista_trampas.append(trampa_1)

lista_items = []
potion_1 = Health_Potion(path="\\chemistry\\essence_of_rookswort\\essence_of_rookswort",x=50,y=75,w=100,h=100,units=1,p_scale=1.5)
lista_items.append(potion_1)

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
        
    for trampa in lista_trampas:
        Trap.draw(trampa,screen)
        Trap.update(trampa,lista_entidades)
        
    for item in lista_items:
        if (item.units > 0):
            Health_Potion.draw(item,screen)
            Health_Potion.update(item,lista_personajes)
       
    player_1.events(delta_ms,keys,lista_balas)
    player_1.update(delta_ms,lista_plataformas,lista_enemigos)
    player_1.draw(screen)
    print(player_1.hitpoints)
    
    for bala in lista_balas:
        Bullet.draw(bala,screen)
        Bullet.update(bala,delta_ms,lista_entidades,lista_plataformas,lista_trampas,lista_balas)

    for enemy in lista_enemigos:
        if(enemy.hitpoints > 0):
            enemy.update(delta_ms,lista_plataformas,lista_personajes,lista_balas)
            enemy.draw(screen)
                        
    if(DEBUG):
        Auxiliar.drawGrid(screen,100)
   
    # screen.fill(FILTER_PURPLE,imagen_fondo.get_rect(),BLEND_RGBA_ADD)
         
    pygame.display.flip()