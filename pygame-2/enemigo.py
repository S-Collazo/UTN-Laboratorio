import pygame
from constantes import *
from auxiliar import Auxiliar
from personaje import Player

class Enemy(Player):
    def __init__ (self,x,y,speed_walk,speed_run,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_L) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\walk.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\green_hat\\idle.png",16,1,True)
        self.frame = 0
        
        self.enemy_lives = 2
        
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
        self.posicion_extremo_b = x - (ANCHO_VENTANA / 2)
        self.validador_posicion = False
            
        self.direction = direction_inicial
        self.direction_change = False
        
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y + self.rect.h - 16,self.rect.w / 2,self.rect.h / 8)
        self.rect_body_front_collition = pygame.Rect(self.rect.x + self.rect.w, self.rect.y,self.rect.w / 4,self.rect.h)
        self.rect_body_back_collition = pygame.Rect(self.rect.x, self.rect.y,self.rect.w / 4,self.rect.h)
            
    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            
            self.add_x(self.move_x)
            self.add_y(self.move_y)
                
            if(super().is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)                           
    
    def add_x(self,delta_x):
        self.rect_ground_collition.x += delta_x
        self.rect_body_front_collition.x += delta_x
        self.rect_body_back_collition.x += delta_x
            
        if(self.direction_change):
            if (self.direction == DIRECTION_R):
                self.rect_body_front_collition.x = self.rect.x + self.rect.w
                self.rect_body_back_collition.x = self.rect.x
            if (self.direction == DIRECTION_L):
                self.rect_body_front_collition.x = self.rect.x - 5
                self.rect_body_back_collition.x = self.rect.x + self.rect.w - 10
            self.direction_change = False
            
        self.rect.x += delta_x
        
    def add_y(self,delta_y):
        self.rect_ground_collition.y += delta_y
        self.rect_body_front_collition.y += delta_y
        self.rect_body_back_collition.y += delta_y
            
        self.rect.y += delta_y
       
    def update (self,delta_ms,lista_plataformas):
            self.events(delta_ms)
            super().do_animation(delta_ms,self.frame_rate_ms)
            self.do_movement(delta_ms,lista_plataformas)
        
    def draw (self,screen):
            super().draw(screen)
        
    def events(self,delta_ms):
        if(self.rect.x < self.posicion_extremo_a and self.rect.x > self.posicion_extremo_b):
            super().walk(self.direction)
        else:
            if(self.rect.x >= self.posicion_extremo_a):
                super().stay()
                self.direction = DIRECTION_L
                self.add_x(-1)
            if(self.rect.x <= self.posicion_extremo_b):
                super().stay()
                self.direction = DIRECTION_R
                self.add_x(1)
