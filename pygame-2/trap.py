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
   
    def damage (self,lista_personajes,lista_enemigos):        
        for personaje in lista_personajes:
            if(self.rect_collition.colliderect(personaje.rect_collition)):
                        personaje.lives = 0
            break
        
        for enemigo in lista_enemigos:
            if(self.rect_collition.colliderect(enemigo.rect_collition)):
                        enemigo.lives = 0
            break
        
    def update (self,lista_personajes,lista_enemigos):
        self.damage(lista_personajes,lista_enemigos)
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)
        
