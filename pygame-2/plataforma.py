import pygame
from constantes import *
from auxiliar import Auxiliar

class Platform:
    def __init__ (self,x,y,w,h,type=0):
        
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\tileset\\forest\\Tiles\\{0}.png",18,flip=False,w=w,h=h)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)
        self.rect_ground_collition = pygame.Rect(self.rect)
        self.rect_ground_collition.height = GROUND_COLLIDE_H
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect_collition)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            
        screen.blit(self.image,self.rect)