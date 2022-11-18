import pygame
import sys
import ui_main
from pygame.locals import *
from constants import *
from player import Player
from enemy_goblin import *
from platforms import Platforms
from bullet import Bullet
from trap import Trap
from level import Level
from item import Health_Potion
from loot import *
from damage_control import *
from sc_info import Screen_Info
from auxiliar import Auxiliar

flags = DOUBLEBUF

pause = False

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
enemy_1 = Goblin_Standard(asset=enemy_list,x=501,y=GROUND_LEVEL-100,gravity=10,frame_rate_ms=80,move_rate_ms=40,p_scale=0.2)
enemy_2 = Goblin_Grunt(asset=enemy_list,x=550,y=150,gravity=10,frame_rate_ms=80,move_rate_ms=40,p_scale=0.2)
enemy_3 = Goblin_Shaman(asset=enemy_list,x=100,y=100,gravity=10,frame_rate_ms=80,move_rate_ms=40,p_scale=0.2)
lista_enemigos.append(enemy_1)
lista_enemigos.append(enemy_2)
lista_enemigos.append(enemy_3)

lista_plataformas = []
lista_plataformas.append(Platforms(x=0,y=GROUND_LEVEL,w=ANCHO_VENTANA,h=GROUND_RECT_H,type=1))
Level.create_plaforms(lista_plataformas,x=250,y=650,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=400,y=600,w=100,h=100,tile_total=10,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=900,y=550,w=100,h=100,tile_total=3,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=725,y=475,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=350,y=450,w=100,h=100,tile_total=7,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=200,y=375,w=100,h=100,tile_total=2,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=400,y=300,w=100,h=100,tile_total=17,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=0,y=225,w=100,h=100,tile_total=7,p_scale=0.4,collition_enabled=True)
Level.create_plaforms(lista_plataformas,x=0,y=550,w=100,h=100,tile_total=3,p_scale=0.4,collition_enabled=True)

lista_trampas = []
trampa_1 = Trap(x=10,y=475,w=50,h=50,p_scale=0.4)
lista_trampas.append(trampa_1)

lista_items = []
potion_1 = Health_Potion(x=50,y=175,w=100,h=100,units=1,p_scale=1.5)
lista_items.append(potion_1)

lista_chests = []
chest_1 = Chest(x=850,y=200,w=200,h=100,p_scale=0.5)
lista_chests.append(chest_1)

lista_balas = []

damage_control = Damage_Control(lista_personajes,lista_enemigos,lista_balas,lista_trampas)

screen_info = Screen_Info(entity=player_1,name="Screen Info",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=None,border_color=None,active=True)

while True:
    if pause:
        pause = ui_main.ui_main()
    else:
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                            
        keys = pygame.key.get_pressed()
        
        delta_ms = clock.tick(FPS)
                
        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        
        for plataforma in lista_plataformas:
            Platforms.draw(plataforma,screen)
            
        for trampa in lista_trampas:
            Trap.draw(trampa,screen)
        
        for chest in lista_chests:
            chest.update(lista_personajes,lista_items)
            chest.draw(screen)
            
        for item in lista_items:
            if (item.units < 1):
                lista_items.remove(item)
                break
            else:
                item.draw(screen)
                item.update(lista_personajes)
                    
        player_1.events(delta_ms,keys,lista_eventos,lista_balas)
        player_1.update(delta_ms,lista_plataformas)
        player_1.draw(screen)
            
        for bala in lista_balas:
            if not (bala.is_shoot):
                lista_balas.remove(bala)
                break
            else:
                Bullet.draw(bala,screen)
                Bullet.update(bala,delta_ms,lista_personajes,lista_enemigos,lista_plataformas,lista_trampas,lista_balas)

        for enemy in lista_enemigos:
            if (enemy.hitpoints < 1):
                enemy.death(lista_items)
                lista_enemigos.remove(enemy)
                break
            else:
                enemy.update(delta_ms,lista_plataformas,lista_personajes,lista_balas,lista_items)
                enemy.draw(screen)
                            
        damage_control.update()
        
        if(screen_info.active):
            screen_info.update(lista_eventos,player_1)
            screen_info.draw()
                                     
        if(DEBUG):
            Auxiliar.drawGrid(screen,100)
            
        pygame.display.flip()