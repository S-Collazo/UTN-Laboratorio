import pygame
from constantes import *
from auxiliar import Auxiliar
from player import Player

class Enemy(Player):
    def __init__ (self,x,y,speed_walk,speed_run,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\walk.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\idle.png",16,1,True)
        self.frame = 0
        
        self.tiempo_transcurrido_anim = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.posicion_extremo_a = x
        self.posicion_extremo_b = x - 800
        self.validador_posicion = False
            
        self.direction = direction_inicial
    
    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            
            self.rect.x += self.move_x    
            self.rect.y += self.move_y
                        
            if(self.rect.y < 600):
                self.rect.y += self.gravity            
        
    def update (self,delta_ms):
        self.events(delta_ms)
        super().do_animation(delta_ms,self.frame_rate_ms)
        self.do_movement(delta_ms)
        
    def draw (self,screen):
        super().draw(screen)
        
    def events(self,delta_ms):
        """
        if(self.rect.x <= self.posicion_extremo_a and self.rect.x >= self.posicion_extremo_b and self.validador_posicion == False):
            super().walk(DIRECTION_L)
        elif(self.rect.x == self.posicion_extremo_b):
            self.validador_posicion == True
            self.rect.x = self.posicion_extremo_b + 1
        elif(self.rect.x <= self.posicion_extremo_a and self.rect.x > self.posicion_extremo_b and self.validador_posicion == True):
            super().walk(DIRECTION_R)
        elif(self.rect.x == self.posicion_extremo_a):
            self.validador_posicion == False
            self.rect.x = self.posicion_extremo_a - 1
        """
        if(self.rect.x < self.posicion_extremo_a and self.rect.x > self.posicion_extremo_b):
            super().walk(self.direction)
        else:
            if(self.rect.x >= self.posicion_extremo_a):
                super().stay()
                self.direction = DIRECTION_L
                self.rect.x -= 1
            if(self.rect.x <= self.posicion_extremo_b):
                super().stay()
                self.direction = DIRECTION_R
                self.rect.x += 1
