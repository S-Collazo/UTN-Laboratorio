import pygame
from constants import *
from auxiliar import Auxiliar
from enemy import Enemy
                            
class Goblin_Standard (Enemy):
    def __init__ (self,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1):
        self.enemy_asset = "\\goblin\\goblin_standard"
        super().__init__(self.enemy_asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
        
        self.hitpoints = 50
        self.attack_power = 10
        
        self.can_block = False
        self.can_throw = False
                    
    def update (self,delta_ms,lista_plataformas,lista_oponente,lista_balas):
        super().update(delta_ms,lista_plataformas,lista_oponente,lista_balas)
            
    def draw (self,screen):
        super().draw(screen)
            
    def events(self,delta_ms,lista_oponente,lista_balas):
        super().events(delta_ms,lista_oponente,lista_balas)
        
class Goblin_Grunt (Enemy):
    def __init__ (self,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1):
        self.enemy_asset = "\\goblin\\goblin_grunt"
        super().__init__(self.enemy_asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
        
        self.hitpoints = 70
        self.attack_power = 10
        
        self.can_block = True
        self.can_throw = False
                    
    def update (self,delta_ms,lista_plataformas,lista_oponente,lista_balas):
        super().update(delta_ms,lista_plataformas,lista_oponente,lista_balas)
            
    def draw (self,screen):
        super().draw(screen)
            
    def events(self,delta_ms,lista_oponente,lista_balas):
        super().events(delta_ms,lista_oponente,lista_balas)
        
class Goblin_Shaman (Enemy):
    def __init__ (self,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1):
        self.enemy_asset = "\\goblin\\goblin_shaman"
        super().__init__(self.enemy_asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
                
        self.hitpoints = 30
        self.attack_power = 30
        
        self.posicion_extremo_a = x
        self.posicion_extremo_b = x - (ANCHO_VENTANA / 4)
        
        self.can_block = False
        self.can_throw = True
        
        self.bullet_aseet = "skull"
                    
    def update (self,delta_ms,lista_plataformas,lista_oponente,lista_balas):
        super().update(delta_ms,lista_plataformas,lista_oponente,lista_balas)
            
    def draw (self,screen):
        super().draw(screen)
            
    def events(self,delta_ms,lista_oponente,lista_balas):
        super().events(delta_ms,lista_oponente,lista_balas)