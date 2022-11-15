import pygame
from constants import *
from enemy import Enemy
from ammo import Ammo
                                    
class Goblin_Standard (Enemy):
    def __init__(self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1):
        super().__init__ (asset,"Goblins","Goblin Standard",x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
        
    def update (self,delta_ms,lista_plataformas,lista_oponente,lista_balas):
        super().update(delta_ms,lista_plataformas,lista_oponente,lista_balas)
        self.events(delta_ms,lista_oponente)
        
    def draw (self,screen):
        super().draw(screen)
        
    def events(self,delta_ms,lista_oponente):
        self.tiempo_transcurrido += delta_ms
            
        if(self.x <= ANCHO_VENTANA / 2):
            self.posicion_extremo_a = 5
            self.posicion_extremo_b = self.x
        else:
            self.posicion_extremo_a = self.x
            self.posicion_extremo_b = ANCHO_VENTANA - (self.rect.w + 5)

        self.attack(False)
         
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
        
                else:
                    if((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                        self.attack()
                        self.tiempo_last_attack = self.tiempo_transcurrido
                        
class Goblin_Grunt (Enemy):
    def __init__(self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1):
        super().__init__ (asset,"Goblins","Goblin Grunt",x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
        self.can_block = True
        
    def update (self,delta_ms,lista_plataformas,lista_oponente,lista_balas):
        super().update(delta_ms,lista_plataformas,lista_oponente,lista_balas)
        self.events(delta_ms,lista_oponente,lista_balas)
        
    def draw (self,screen):
        super().draw(screen)
        
    def events(self,delta_ms,lista_oponente,lista_balas):
        self.tiempo_transcurrido += delta_ms
            
        if(self.x <= ANCHO_VENTANA / 2):
            self.posicion_extremo_a = 5
            self.posicion_extremo_b = self.x
        else:
            self.posicion_extremo_a = self.x
            self.posicion_extremo_b = ANCHO_VENTANA - (self.rect.w + 5)

        self.attack(False)
        self.block(False)
         
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
                                
class Goblin_Shaman (Enemy):
    def __init__(self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1):
        super().__init__ (asset,"Goblins","Goblin Shaman",x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
        self.can_throw = True
        
    def update (self,delta_ms,lista_plataformas,lista_oponente,lista_balas):
        super().update(delta_ms,lista_plataformas,lista_oponente,lista_balas)
        self.events(delta_ms,lista_oponente,lista_balas)
        
    def draw (self,screen):
        super().draw(screen)
        
    def events(self,delta_ms,lista_oponente,lista_balas):
        self.tiempo_transcurrido += delta_ms
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas)
                    
        self.shoot(lista_balas=lista_balas,on_off=False)
         
        for oponente in lista_oponente:
            self.player_position_x = oponente.rect.x
            self.player_position_y = oponente.rect.y
            self.distance_difference_x = self.rect.x - (oponente.rect.x - oponente.rect.w)
            self.distance_difference_y = self.rect.y - (oponente.rect.y - oponente.jump_height)
                      
            if(abs(self.distance_difference_x) <= 500 and abs(self.distance_difference_y) <= 50):
                if(self.is_shooting == False and ((self.tiempo_transcurrido - self.tiempo_last_shoot) > self.interval_time_shoot)):
                    if(self.distance_difference_x > 0):
                        self.direction = DIRECTION_L
                    else:
                        self.direction = DIRECTION_R
                    super().shoot(lista_balas)
                    self.tiempo_last_shoot = self.tiempo_transcurrido