import pygame
from constants import *
from auxiliar import Auxiliar

class Trap:
    def __init__ (self,x,y,w,h,type=0,p_scale=1,):
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\traps\\creepy_forest\\spikes_{:02d}.png",1,step=0,flip=False,scale=p_scale,w=w,h=h)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)
   
    def damage (self,lista_entidades):        
        for entidad in lista_entidades:
            if(self.rect_collition.colliderect(entidad.rect_collition)):
                        entidad.hitpoints = 0
            break
        
    def update (self,lista_entidades):
        self.damage(lista_entidades)
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)
        
