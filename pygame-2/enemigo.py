import pygame
from constantes import *
from auxiliar import Auxiliar
from entidad import Entity

class Enemy(Entity):
    def __init__ (self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L) -> None:
        self.asset_folder = "\\players\\{0}".format(asset)
        
        super().__init__(self.asset_folder,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,0.2)        
        self.speed_walk = int(ANCHO_VENTANA / 400)
        self.speed_run = int(ANCHO_VENTANA / 400)
        
        self.posicion_extremo_a = x
        self.posicion_extremo_b = x - (ANCHO_VENTANA / 2)
        self.validador_posicion = False
        
        self.lives = 3
        self.score = 0
        self.entity_type = ENEMY
       
    def update (self,delta_ms,lista_plataformas,lista_oponente):
            self.events(delta_ms)
            super().update(delta_ms,lista_plataformas,lista_oponente)
        
    def draw (self,screen):
            super().draw(screen)
        
    def events(self,delta_ms):
        self.tiempo_transcurrido += delta_ms
         
        if(self.rect.x < self.posicion_extremo_a and self.rect.x > self.posicion_extremo_b):
            super().walk(self.direction)
        else:
            if(self.rect.x >= self.posicion_extremo_a):
                super().stay()
                self.direction = DIRECTION_L
                super().add_x(-1)
            if(self.rect.x <= self.posicion_extremo_b):
                super().stay()
                self.direction = DIRECTION_R
                super().add_x(1)
