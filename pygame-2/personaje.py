import pygame
from constantes import *
from auxiliar import Auxiliar
from entidad import Entity
from municion import Ammo

class Player(Entity):
    def __init__ (self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_R,p_scale=0.1) -> None:
        self.asset_folder = "\\players\\{0}".format(asset)
        
        super().__init__(self.asset_folder,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
                
        self.lives = 5
        self.score = 0
        
        self.entity_type = PLAYER
        self.p_scale = p_scale
                                                                                 
    def update(self,delta_ms,lista_plataformas,lista_oponente):
        super().update(delta_ms,lista_plataformas,lista_oponente)

    def draw (self,screen):
        super().draw(screen)
                
    def events(self,delta_ms,keys,lista_balas):
        self.tiempo_transcurrido += delta_ms
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas)
        
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().stay()   
        if(keys[pygame.K_SPACE] or keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > (self.interval_time_jump)):
                super().jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido
                   
        if(not keys[pygame.K_a]):
            self.shoot(lista_balas,False)  
        if(keys[pygame.K_s] and not keys[pygame.K_a] and self.is_shooting == False):
            self.shoot(lista_balas)
        if(not keys[pygame.K_a]):
            self.attack(False)
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.attack()
