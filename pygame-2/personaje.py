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
        self.jump_height = int(ALTO_VENTANA / 4)
        self.is_jump = False
        self.y_start_jump = y
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.direction = direction_inicial
        self.direction_change = False
        
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H,self.rect.w / 2,self.rect.h / 8)
        self.rect_body_front_collition = pygame.Rect(self.rect.x + self.rect.w, self.rect.y,self.rect.w / 4,self.rect.h)
        self.rect_body_back_collition = pygame.Rect(self.rect.x, self.rect.y,self.rect.w / 4,self.rect.h)
    
    def walk (self,direction):
        if self.direction != direction or self.animation != self.walk_r and self.animation != self.walk_l:
            self.frame = 0
            self.direction = direction
            self.direction_change = True
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
                    
    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
                                  
            if(abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.add_x(self.move_x)
            self.add_y(self.move_y)
            
            if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)          
            elif (self.is_jump):
                self.is_jump = False
                                
    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
    
    def damage(self,lista_enemigos):
        for enemigo in lista_enemigos:
            if(self.rect_body_front_collition.colliderect(enemigo.rect_body_front_collition) or self.rect_body_back_collition.colliderect(enemigo.rect_body_front_collition)):
                self.lives -= 1
                if(self.rect.x <= (ANCHO_VENTANA / 2)):
                    self.add_x(-100)
                    enemigo.add_x(100)
                else:
                    self.add_x(100)
                    enemigo.add_x(-100)
                break
            if(self.rect_body_front_collition.colliderect(enemigo.rect_body_back_collition)):
                enemigo.enemy_lives -= 1
                if(enemigo.rect.x <= (ANCHO_VENTANA / 2)):
                    self.add_x(-100)
                    enemigo.add_x(100)
                else:
                    self.add_x(100)
                    enemigo.add_x(-100)
                break
            
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
                
    def do_animation (self,delta_ms,frame_rate_ms):
        self.tiempo_transcurrido_anim += delta_ms
        self.frame_rate_ms = frame_rate_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
        
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                 self.frame = 0
                                             
    def update(self,delta_ms,lista_plataformas,lista_enemigos):
        self.do_animation(delta_ms,self.frame_rate_ms)
        self.do_movement(delta_ms,lista_plataformas)
        self.damage(lista_enemigos)
        if(self.lives > 0):
                print(self.lives)
    
    def draw (self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            pygame.draw.rect(screen,PURPLE,self.rect_body_front_collition)
            pygame.draw.rect(screen,ORANGE,self.rect_body_back_collition)
    
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

        