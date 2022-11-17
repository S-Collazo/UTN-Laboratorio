import pygame
import random
import copy
from item import *
from constants import *
from auxiliar import Auxiliar

class Chest:
    def __init__ (self,x,y,w,h,p_scale=1):
        self.p_scale = p_scale * GLOBAL_SCALE
                
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\tileset\\creepy_forest\\Objects\\chest_{:03d}.png",2,step=0,flip=False,scale=self.p_scale,w=w,h=h)
        self.chest_closed = self.image_list[0]
        self.chest_open = self.image_list[1]
        
        self.image = self.chest_closed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)

    def get_loot (self,lista_items):
        max_items = len(lista_items) - 1
        loot_number = random.randrange(0,max_items)
        
        if (loot_number % 0):
            loot_reward = Gem(x=self.rect.x + (self.rect.w / 2),y=self.rect.y + (self.rect.h / 2),w=100,h=200,units=1,p_scale=1,enemy_drop=True)
        else:
            loot_reward = Health_Potion(x=self.rect.x + (self.rect.w / 2),y=self.rect.y + (self.rect.h / 2),w=100,h=100,units=1,p_scale=1.5)

        lista_items.append(loot_reward)

    def update (self,lista_personajes):
        pass
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)