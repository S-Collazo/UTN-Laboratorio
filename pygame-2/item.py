import pygame
from constants import *
from auxiliar import Auxiliar

class Item:
    def __init__ (self,path,x,y,w,h,units=1,p_scale=1,type=0):
        self.p_scale = p_scale * GLOBAL_SCALE
        
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + path + "_{:03d}.png",1,step=0,flip=False,scale=self.p_scale,w=w,h=h)
        self.image = self.image_list[type]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)
        
        self.units = units
                    
    def update (self,lista_personajes):
        pass
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)
        
class Health_Potion (Item):
    def __init__ (self,path,x,y,w,h,units=1,p_scale=1):
        super().__init__ (path=path,x=x,y=y,w=w,h=h,units=units,p_scale=p_scale)
        self.healing_power = 20
    
    def healing (self,lista_personajes):        
        for personaje in lista_personajes:
            if(self.rect_collition.colliderect(personaje.rect_collition)):
                        if ((personaje.hitpoints + self.healing_power) <= personaje.hitpoints_max):
                            personaje.hitpoints += self.healing_power
                        else:
                            personaje.hitpoints = personaje.hitpoints_max
                        self.units -= 1
            break
      
    def update (self,lista_personajes):
        self.healing(lista_personajes)
    
    def draw (self,screen):
            super().draw(screen)