import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__ (self,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_R) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\walk.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\idle.png",16,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\jump.png",33,1,False,2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\jump.png",33,1,True,2)
        self.frame = 0
        
        self.lives = 5
        self.score = 0
        self.tiempo_transcurrido_anim = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = int(ANCHO_VENTANA / 200)
        self.speed_run = int(ANCHO_VENTANA / 100)
        self.gravity = gravity
        self.jump_power = int((ALTO_VENTANA * 4) / 100)
        self.jump_height = int(ALTO_VENTANA / 5)
        self.is_jump = False
        self.y_start_jump = y
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.direction = direction_inicial
    
    def walk (self,direction):
        if self.direction != direction or self.animation != self.walk_r and self.animation != self.walk_l:
            self.frame = 0
            self.direction = direction
            if (direction == DIRECTION_R):
                self.animation = self.walk_r
                self.move_x = self.speed_walk
            else:
                self.animation = self.walk_l
                self.move_x = -self.speed_walk
            
    def jump (self, on_off = True):
        if (on_off  and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if (self.direction == DIRECTION_R):
                self.animation = self.jump_r
                self.move_y = -self.jump_power
                self.move_x = self.jump_power
            else:
                self.animation = self.jump_l
                self.move_y = -self.jump_power
                self.move_x = -self.jump_power
                
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()
    
    def stay(self):  
        if not self.animation == self.stay_r and not self.animation == self.stay_l:
            if (self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0 
        
    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
                      
            if(abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.rect.x += self.move_x
            self.rect.y += self.move_y
            
            if(self.rect.y < 600):
                self.rect.y += self.gravity            
            elif (self.is_jump):
                self.is_jump = False
        
    def do_animation (self,delta_ms,frame_rate_ms):
        self.tiempo_transcurrido_anim += delta_ms
        self.frame_rate_ms = frame_rate_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
        
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                 self.frame = 0
                                             
    def update(self,delta_ms):
        self.do_animation(delta_ms,self.frame_rate_ms)
        self.do_movement(delta_ms)
    
    def draw (self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        
    def events(self,delta_ms,keys):
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()   
        if(keys[pygame.K_SPACE] or keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]):
            self.jump(True)

        