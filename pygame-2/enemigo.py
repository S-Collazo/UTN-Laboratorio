import pygame
from constantes import *
from auxiliar import Auxiliar
from entidad import Entity

class Enemy(Entity):
    def __init__ (self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L,p_scale=0.1) -> None:
        self.asset_folder = "\\bosses\\{0}".format(asset)
        
        super().__init__(self.asset_folder,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)        
        self.speed_walk = int(ANCHO_VENTANA / 400)
        self.speed_run = int(ANCHO_VENTANA / 400)
        
        self.posicion_extremo_a = x
        self.posicion_extremo_b = x - (ANCHO_VENTANA / 2)
        self.validador_posicion = False
        
        self.lives = 3
        self.score = 0
        self.entity_type = ENEMY
               
    def update (self,delta_ms,lista_plataformas,lista_oponente):
            super().update(delta_ms,lista_plataformas,lista_oponente)
            self.events(delta_ms,lista_oponente)
        
    def draw (self,screen):
            super().draw(screen)
        
    def events(self,delta_ms,lista_oponente):
        self.tiempo_transcurrido += delta_ms
         
        for oponente in lista_oponente:
            self.player_position_x = oponente.rect.x
            self.player_position_y = oponente.rect.y
            self.distance_difference_x = self.rect.x - oponente.rect.x
            self.distance_difference_y = self.rect.y - (oponente.rect.y - oponente.jump_height)
            
            if(abs(self.distance_difference_x) > 300 or abs(self.distance_difference_y) > 100):
                if(self.rect.x < self.posicion_extremo_a and self.rect.x > self.posicion_extremo_b):
                    super().walk(self.direction)
                else:
                    if(self.rect.x >= self.posicion_extremo_a):
                        super().walk(DIRECTION_L)
                    if(self.rect.x <= self.posicion_extremo_b):
                        super().walk(DIRECTION_R)
            else:
                if(self.distance_difference_x >= 0):
                    super().walk(DIRECTION_L)

                else:
                    super().walk(DIRECTION_R)
                if(abs(self.distance_difference_x) <= (oponente.rect.w + 50)):
                        super().attack()