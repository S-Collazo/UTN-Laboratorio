import pygame
import random
from constants import *
from auxiliar import Auxiliar
from entity import Entity
from ammo import Ammo
from item import *

class Enemy(Entity):
    def __init__ (self,asset,group,name,x,y,gravity,frame_rate_ms,move_rate_ms,p_scale=0.1) -> None:
        self.asset_type = asset[group][name]
        
        self.direction_value = random.random()
        if (self.direction_value == 0):
            self.direction = DIRECTION_L
        else:
            self.direction = DIRECTION_R
        
        super().__init__(self.asset_type,x,y,gravity,frame_rate_ms,move_rate_ms,self.direction,p_scale)             
        self.x = x
        
        self.can_block = False
        self.can_throw = False
        self.is_alive = True    
                       
    def death (self,lista_items,item_asset):
        if(self.animation != self.death_r and self.animation != self.death_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.death_r
            else:
                self.animation = self.death_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
            
            gem_reward = Gem(asset=item_asset,name="Basic Gem",x=self.rect.x + (self.rect.w / 2),y=self.rect.y + (self.rect.h / 2),p_scale=1,enemy_drop=True)
            lista_items.append(gem_reward)
        
                       
    def update (self,delta_ms,lista_plataformas,lista_items,item_asset):          
        if (self.is_alive):
            super().update(delta_ms,lista_plataformas)
        else:
            self.death(lista_items,item_asset)
        
    def draw (self,screen):
        super().draw(screen)
        
    """
    def events(self,delta_ms,lista_oponente,lista_balas):
        self.tiempo_transcurrido += delta_ms
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas)
            
        if(self.x <= ANCHO_VENTANA / 2):
            self.posicion_extremo_a = 5
            self.posicion_extremo_b = self.x
        else:
            self.posicion_extremo_a = self.x
            self.posicion_extremo_b = ANCHO_VENTANA - (self.rect.w + 5)
        
        #self.shoot(asset=self.asset,lista_balas=lista_balas,on_off=False)
        #self.attack(False)
        #self.block(False)
         
        for oponente in lista_oponente:
            self.player_position_x = oponente.rect.x
            self.player_position_y = oponente.rect.y
            self.distance_difference_x = self.rect.x - (oponente.rect.x - oponente.rect.w)
            self.distance_difference_y = self.rect.y - (oponente.rect.y - oponente.jump_height)
            
            if(abs(self.distance_difference_x) > 500 or abs(self.distance_difference_y) > 50):
                if(self.rect.x >= self.posicion_extremo_a and self.rect.x <= self.posicion_extremo_b):
                    super().walk(self.direction)
                else:
                    if(self.rect.x < self.posicion_extremo_a):
                        super().walk(DIRECTION_R)
                    if(self.rect.x > self.posicion_extremo_b):
                        super().walk(DIRECTION_L)
            else:
                if(abs(self.distance_difference_x) > 10):
                    if(self.distance_difference_x >= 0):
                        super().walk(DIRECTION_L)

                    else:
                        super().walk(DIRECTION_R)
                   
                    if(self.can_throw and self.is_shooting == False):
                        if((self.tiempo_transcurrido - self.tiempo_last_shoot) > (self.interval_time_shoot)):
                            super().shoot(self.asset_type,lista_balas)
                            self.tiempo_last_shoot = self.tiempo_transcurrido
                else:
                    if(oponente.is_attack and self.can_block):
                        if((self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                            self.block()
                            self.tiempo_last_block = self.tiempo_transcurrido
                    elif((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                        self.attack()
                        self.tiempo_last_attack = self.tiempo_transcurrido
                    
                for bala in lista_balas:
                    if(self.can_block):
                        if(abs(self.rect.x - bala.rect.x) <= (self.rect.w + 50)):
                            if((self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                                self.block()
                                self.tiempo_last_block = self.tiempo_transcurrido
    """
        