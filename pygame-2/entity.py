import pygame
import re
from constants import *
from auxiliar import Auxiliar
from ammo import Ammo

class Entity:
    def __init__ (self,asset_folder,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_R,p_scale=1,interval_time=FPS) -> None:  
        self.p_scale = p_scale * GLOBAL_SCALE
        
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_IDLE\\_IDLE_{:03d}.png",2,flip=False,step = 0,scale=self.p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_IDLE\\_IDLE_{:03d}.png",2,flip=True,step = 0,scale=self.p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_JUMP\\_JUMP_{:03d}.png",4,flip=False,step = 0,scale=self.p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_JUMP\\_JUMP_{:03d}.png",4,flip=True,step = 0,scale=self.p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_RUN\\_RUN_{:03d}.png",3,flip=False,step = 0,scale=self.p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_RUN\\_RUN_{:03d}.png",3,flip=True,step = 0,scale=self.p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_THROW\\_THROW_{:03d}.png",6,flip=False,step = 0,scale=self.p_scale,repeat_frame=1)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_THROW\\_THROW_{:03d}.png",6,flip=True,step = 0,scale=self.p_scale,repeat_frame=1)
        self.attack_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_ATTACK\\_ATTACK_{:03d}.png",4,flip=False,step = 0,scale=self.p_scale,repeat_frame=1)
        self.attack_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_ATTACK\\_ATTACK_{:03d}.png",4,flip=True,step = 0,scale=self.p_scale,repeat_frame=1)
        self.block_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_BLOCK\\_BLOCK_{:03d}.png",3,flip=False,step = 0,scale=self.p_scale,repeat_frame=1)
        self.block_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_BLOCK\\_BLOCK_{:03d}.png",3,flip=True,step = 0,scale=self.p_scale,repeat_frame=1)
        self.frame = 0
                
        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_anim = 0
        self.tiempo_transcurrido_move = 0
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time
        self.tiempo_last_attack = 0
        self.interval_time_attack = interval_time * 2
        self.tiempo_last_shoot = 0
        self.interval_time_shoot = interval_time
        self.tiempo_last_block = 0
        self.interval_time_block = interval_time * 5
        
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = int((ANCHO_VENTANA / 100))
        self.speed_run = self.speed_walk * 2
        self.gravity = gravity
        self.jump_height = int((ALTO_VENTANA / 14))
        self.jump_power = self.jump_height / 2
        self.y_start_jump = y
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_attack = False
        self.is_block = False
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
            
        self.direction = direction_inicial
                
        self.rect_collition = pygame.Rect(x+self.rect.width / 3,y,self.rect.width / 3,self.rect.height)
        self.rect_ground_collition = pygame.Rect(self.rect_collition)
        self.rect_ground_collition.height = GROUND_COLLIDE_H
        self.rect_ground_collition.y = y + self.rect.height - GROUND_COLLIDE_H
                
        self.rect_body_collition = pygame.Rect(x,y,self.rect.width/2,self.rect.height)
            
    def walk (self,direction_walk):        
        if(self.is_jump == False and self.is_fall == False):
            if (self.direction != direction_walk or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction_walk
                if (direction_walk == DIRECTION_R):
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
                self.move_y = -self.jump_height
                self.move_x = self.jump_power
            else:
                self.animation = self.jump_l
                self.move_y = -self.jump_height
                self.move_x = -self.jump_power
                
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()
    
    def stay(self):  
        if not (self.animation == self.stay_r and not self.animation == self.stay_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0 
      
    def attack(self,on_off = True):
        self.is_attack = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.attack_r and self.animation != self.attack_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.attack_r
                else:
                    self.animation = self.attack_l
            
    def block(self,on_off = True):
        self.is_block = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.block_r and self.animation != self.block_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.block_r
                else:
                    self.animation = self.block_l    
            
    def shoot(self,lista_balas,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l
                    
            Ammo(lista_balas=lista_balas,x=self.rect.x,y=self.rect.y,frame_rate_ms=self.frame_rate_ms,move_rate_ms=self.move_rate_ms,direction=self.direction,p_scale=self.p_scale)
                                                                        
    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect_ground_collition.bottom >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(plataforma.collition_enabled and self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
                
    def add_x(self,delta_x):        
        if((self.rect.x + delta_x) >= 0 and (self.rect.x + self.rect.w + delta_x) <= ANCHO_VENTANA):
            self.rect.x += delta_x
            self.rect_collition.x += delta_x
            self.rect_ground_collition.x += delta_x
            self.rect_body_collition.x += delta_x
        
        if(self.direction == DIRECTION_R):
            self.rect_body_collition.x = self.rect.x + 5 + (self.rect_body_collition.width)
        else:
            self.rect_body_collition.x = self.rect.x - 5
        
                
    def add_y(self,delta_y):
        if((self.rect.y + delta_y) >= 0 and (self.rect.y + self.rect.h + delta_y) <= ALTO_VENTANA):
            self.rect.y += delta_y
            self.rect_collition.y += delta_y
            self.rect_ground_collition.y += delta_y
            self.rect_body_collition.y += delta_y
    
    def damage(self,lista_oponente):
        if(self.lives > 0 and self.is_attack):
            for oponente in lista_oponente:
                if(self.rect_body_collition.colliderect(oponente.rect) or self.rect_body_collition.colliderect(oponente.rect_body_collition) and not oponente.is_block):
                        oponente.lives -= 1
                                
                        if(self.rect.x <= oponente.rect.x):
                            oponente.add_x(100)
                        else:
                            oponente.add_x(-100)
                            oponente.jump(True)
                                        
                break
                      
    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
                                  
            if(abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.add_x(self.move_x)
            self.add_y(self.move_y)
            
            if not(self.is_on_platform(lista_plataformas)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.add_y(self.gravity)          
            else:
                if(self.is_jump):
                    self.jump(False)
                self.is_fall = False
                
    def do_animation (self,delta_ms,frame_rate_ms):
        self.tiempo_transcurrido_anim += delta_ms
        self.frame_rate_ms = frame_rate_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
        
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                 self.frame = 0
                                           
    def update(self,delta_ms,lista_plataformas,lista_oponente):
        if(DEBUG):
            if(self.lives >= 10):
                    print(self.lives)
                    
        self.do_animation(delta_ms,self.frame_rate_ms)
        self.do_movement(delta_ms,lista_plataformas)
        self.damage(lista_oponente)
    
    def draw (self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            if(self.is_attack or self.is_block):
                pygame.draw.rect(screen,PURPLE,self.rect_body_collition)
    
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

        