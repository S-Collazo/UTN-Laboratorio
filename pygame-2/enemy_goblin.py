import pygame
from constants import *
from enemy import Enemy
                            
class Goblin (Enemy):
    def __init__ (self,asset,name,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1):  
        super().__init__(asset,"Goblins",name,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)

        if(name == "Goblin Shaman"):
            self.can_block = False
            self.can_throw = True
        elif(name == "Goblin Grunt"):
            self.can_block = True
            self.can_throw = False
        else:
            self.can_block = False
            self.can_throw = False
                    
    def update (self,delta_ms,lista_plataformas,lista_oponente,lista_balas):
        super().update(delta_ms,lista_plataformas,lista_oponente,lista_balas)
            
    def draw (self,screen):
        super().draw(screen)
            
    def events(self,delta_ms,lista_oponente,lista_balas):
        super().events(delta_ms,lista_oponente,lista_balas)