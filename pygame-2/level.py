import pygame
import sys
import random
import ui_pause
from pygame.locals import *
from constants import *
from player import Player
from bullet import Bullet
from enemy_goblin import *
from platforms import Platforms
from trap import Trap
from item import Health_Potion
from loot import *
from damage_control import *
from ui_screen_info import ScreenInfo
from auxiliar import Auxiliar

class Level:
    def __init__(self,screen,level,difficulty):
        self.screen = screen
        self.level_number = level
        self.difficulty = difficulty
                           
        level_list = Auxiliar.readJson("level_list.json")
        level_info = level_list[self.level_number]

        lv_gravity = level_info["gravity"]
        lv_frame_rate_ms = level_info["frame_rate_ms"]
        lv_move_rate_ms = level_info["move_rate_ms"]

        player_info = level_info["player"]
        enemy_info = level_info["enemy"]
        platform_info = level_info["platform"]
        trap_info = level_info["trap"]
        item_info = level_info["item"]
        chest_info = level_info["chest"]

        self.background_image = pygame.image.load(PATH_RECURSOS + level_info["background_image"])
        self.background_image = pygame.transform.scale(self.background_image,(ANCHO_VENTANA,ALTO_VENTANA))

        self.player_list = Auxiliar.readJson(player_info["player_list"])
        self.lista_personajes = []
        for n in range(player_info["player_quantity"][self.difficulty]):
            player_coordinates = Auxiliar.splitIntoInt(player_info["player_starter_position"],",")
            self.lista_personajes.append(Player(asset=self.player_list,name="Iron Knight",x=player_coordinates[0],y=player_coordinates[1],gravity=lv_gravity,frame_rate_ms=lv_frame_rate_ms,move_rate_ms=lv_move_rate_ms))

        self.enemy_list = Auxiliar.readJson(enemy_info["enemy_list"])
        self.lista_enemigos = []
        for n in range(enemy_info["enemy_quantity"][self.difficulty]):
            enemy_type = Auxiliar.splitIntoString(enemy_info["enemy_type"][self.difficulty],"/")
            enemy_coordinates = Auxiliar.splitIntoInt(enemy_info["enemy_starter_position"][n],",")
            if (enemy_type[n] == "Standard"):
                self.lista_enemigos.append(Goblin_Standard(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=lv_gravity,frame_rate_ms=lv_frame_rate_ms,move_rate_ms=lv_move_rate_ms,p_scale=enemy_info["p_scale"]))  
            elif (enemy_type[n] == "Grunt"):
                self.lista_enemigos.append(Goblin_Grunt(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=lv_gravity,frame_rate_ms=lv_frame_rate_ms,move_rate_ms=lv_move_rate_ms,p_scale=enemy_info["p_scale"]))  
            else:
                self.lista_enemigos.append(Goblin_Shaman(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=lv_gravity,frame_rate_ms=lv_frame_rate_ms,move_rate_ms=lv_move_rate_ms,p_scale=enemy_info["p_scale"]))

        self.lista_plataformas = []
        if (platform_info["floor_state"]):
            self.lista_plataformas.append(Platforms(x=0,y=GROUND_LEVEL,w=ANCHO_VENTANA,h=GROUND_RECT_H,type=1))
        for n in range(platform_info["platform_quantity"][self.difficulty]):
            platform_coordinates = Auxiliar.splitIntoInt(platform_info["platform_position_length"][n],",")
            platform_dimensions = Auxiliar.splitIntoInt(platform_info["platform_dimensions"],",")
            Platforms.create_plaforms(self.lista_plataformas,x=platform_coordinates[0],y=platform_coordinates[1],w=platform_dimensions[0],h=platform_dimensions[1],tile_total=platform_coordinates[2],p_scale=platform_info["p_scale"])

        self.lista_trampas = []
        for n in range(trap_info["trap_quantity"][self.difficulty]):
            trap_coordinates = Auxiliar.splitIntoInt(trap_info["trap_position"][n],",")
            trap_dimensions = Auxiliar.splitIntoInt(trap_info["trap_dimensions"],",")
            self.lista_trampas.append(Trap(x=trap_coordinates[0],y=trap_coordinates[1],w=trap_dimensions[0],h=trap_dimensions[1],p_scale=trap_info["p_scale"]))

        self.item_list = Auxiliar.readJson(item_info["item_list"])
        self.lista_items = []
        if (item_info["item_quantity"][self.difficulty] > 0):
            for n in range(item_info["item_quantity"][self.difficulty]):
                item_type = random.randrange(item_info["item_quantity"][self.difficulty])
                item_coordinates = Auxiliar.splitIntoInt(item_info["item_position"][n],",")
                if (item_type % 2 == 0):
                    self.lista_items.append(Gem(asset=self.item_list,name="Basic Gem",x=item_coordinates[0],y=item_coordinates[1],p_scale=item_info["p_scale"]))
                else:
                    self.lista_items.append(Health_Potion(asset=self.item_list,name="Basic Health Potion",x=item_coordinates[0],y=item_coordinates[1]))

        self.lista_chests = []
        if(chest_info["chest_quantity"][self.difficulty] > 0):
            for n in range(chest_info["chest_quantity"][self.difficulty]):
                chest_coordinates = Auxiliar.splitIntoInt(chest_info["chest_position"][n],",")
                chest_dimensions = Auxiliar.splitIntoInt(chest_info["chest_dimensions"],",")
                self.lista_chests.append(Chest(item_asset=self.item_list,x=chest_coordinates[0],y=chest_coordinates[1],w=chest_dimensions[0],h=chest_dimensions[1],p_scale=chest_info["p_scale"]))

        self.lista_balas = []

        self.damage_control = Damage_Control(self.lista_personajes,self.lista_enemigos,self.lista_balas,self.lista_trampas)

        self.screen_info = ScreenInfo(entity=self.lista_personajes[0],name="ScreenInfo",master_surface=self.screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=None,border_color=None,active=True)
         
    def run_level (self,delta_ms,lista_eventos,keys):
        self.game_state = GAME_RUNNING
        
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GAME_PAUSE
                                                
        self.screen.blit(self.background_image,self.background_image.get_rect())
        
        for plataforma in self.lista_plataformas:
            Platforms.draw(plataforma,self.screen)
            
        for trampa in self.lista_trampas:
            Trap.draw(trampa,self.screen)
        
        for chest in self.lista_chests:
            chest.update(self.lista_personajes,self.lista_items)
            chest.draw(self.screen)
            
        for item in self.lista_items:
            if (item.used):
                self.lista_items.remove(item)
                break
            else:
                item.draw(self.screen)
                item.update(self.lista_personajes)
                    
        for player in self.lista_personajes:
            player.events(delta_ms,keys,lista_eventos,self.lista_balas)
            player.update(delta_ms,self.lista_plataformas)
            player.draw(self.screen)
            
        for bala in self.lista_balas:
            if not (bala.is_shoot):
                self.lista_balas.remove(bala)
                break
            else:
                Bullet.draw(bala,self.screen)
                Bullet.update(bala,delta_ms,self.lista_personajes,self.lista_enemigos,self.lista_plataformas,self.lista_trampas,self.lista_balas)

        for enemy in self.lista_enemigos:
            if (enemy.hitpoints < 1):
                enemy.death(self.lista_items,self.item_list)
                self.lista_enemigos.remove(enemy)
                break
            else:
                enemy.update(delta_ms,self.lista_plataformas,self.lista_personajes,self.lista_balas,self.lista_items,self.item_list)
                enemy.draw(self.screen)
                            
        self.damage_control.update()
        
        if(self.screen_info.active):
            self.screen_info.update(lista_eventos,self.lista_personajes[0])
            self.screen_info.draw()
                                    
        if(DEBUG):
            Auxiliar.drawGrid(self.screen,100)
            
        return self.game_state