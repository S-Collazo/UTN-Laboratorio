import pygame
from constantes import *
from auxiliar import Auxiliar

class Bullet:
    def __init__ (self,x,y,move_rate_ms,frame_rate_ms,move=50,direction_inicial=DIRECTION_R,p_scale=1,interval_bullet=FPS*2,distance=ANCHO_VENTANA,type=0):
        self.p_scale = p_scale * GLOBAL_SCALE
        
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\elements\\shield\\knight_shield_{0}.png",1,flip=False,step=0,scale=self.p_scale,w=100,h=100)
        self.frame = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)
        
        self.delta_x = move
        self.move_rate_ms = move_rate_ms * 350
        self.frame_rate_ms = frame_rate_ms / 2
        
        self.direction = direction_inicial
        
        self.distance = distance
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_anim = 0
        self.interval_bullet = interval_bullet
        
        self.is_shooting = True
        self.collition_enabled = True
    
    def damage(self,lista_oponente,lista_plataformas):
        if(self.is_shooting):  
            for oponente in lista_oponente:
                if(self.rect_collition.colliderect(oponente.rect)):
                        self.is_shooting = False
                        if not (oponente.is_block):
                            oponente.lives -= 1
                                
                        if(self.rect.x <= oponente.rect.x):
                            oponente.add_x(100)
                        else:
                            oponente.add_x(-100)
                            oponente.jump(True)
                break
            
            for plataforma in lista_plataformas:
                if(self.rect_collition.colliderect(plataforma.rect)):
                    self.is_shooting = False
                    print("HIT!")
                break                

    
    def do_movement(self):
        self.tiempo_transcurrido_move += self.interval_bullet
                
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0         

            if((self.rect.x + self.rect.w + self.delta_x) >= 0 and (self.rect.x + self.rect.w + self.delta_x) <= self.distance):
                if(self.direction == DIRECTION_R):
                    self.rect.x += self.delta_x
                    self.rect_collition.x += self.delta_x
                else:
                    self.rect.x -= self.delta_x
                    self.rect_collition.x -= self.delta_x             
            else:
                self.is_shooting = False
                
    def do_animation (self,delta_ms):
        self.tiempo_transcurrido_anim += delta_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
        
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                 self.frame = 0
                
    def update (self,delta_ms,lista_oponente,lista_plataformas):
        self.damage(lista_oponente,lista_plataformas)
        self.do_movement()
        self.do_animation(delta_ms)
       
    def draw (self,screen):        
        if(self.is_shooting):
            if(DEBUG):
                if(self.collition_enabled):
                    pygame.draw.rect(screen,PURPLE,self.rect_collition)
                
            screen.blit(self.image,self.rect)
           