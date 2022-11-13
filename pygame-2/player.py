import pygame
from constants import *
from auxiliar import Auxiliar
from entity import Entity
from ammo import Ammo

class Player(Entity):
    def __init__ (self,asset,name,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_R,p_scale=0.1) -> None:
        self.asset = asset["Player"][name]
        
        super().__init__(self.asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
    
        self.score = 0
                                                                                     
    def update(self,delta_ms,lista_plataformas,lista_oponente):
        super().update(delta_ms,lista_plataformas,lista_oponente)

    def draw (self,screen):
        super().draw(screen)
                
    def events(self,delta_ms,keys,lista_balas):
        self.tiempo_transcurrido += delta_ms
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas)
        
        self.shoot(asset=self.asset,lista_balas=lista_balas,on_off=False)
        self.attack(False)
        self.block(False)
        
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().stay()   
        if(keys[pygame.K_SPACE] or keys[pygame.K_LEFT] and keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > (self.interval_time_jump)):
                super().jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido
                   
        if(not keys[pygame.K_a]):
            self.shoot(self.asset,lista_balas,False)  
        if(keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d] and self.is_shooting == False):
            if((self.tiempo_transcurrido - self.tiempo_last_shoot) > (self.interval_time_shoot)):
                self.shoot(self.asset,lista_balas)
                self.tiempo_last_shoot = self.tiempo_transcurrido
        if(not keys[pygame.K_a]):
            self.attack(False)
        if(keys[pygame.K_a] and not (keys[pygame.K_s] or keys[pygame.K_d])):
            if((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                self.attack()
                self.tiempo_last_attack = self.tiempo_transcurrido
        if(not keys[pygame.K_d]):
            self.block(False)
        if(keys[pygame.K_d] and not (keys[pygame.K_s] or keys[pygame.K_a])):
            if((self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                self.block()
                self.tiempo_last_block = self.tiempo_transcurrido
