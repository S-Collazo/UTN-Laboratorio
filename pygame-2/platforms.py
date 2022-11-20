import pygame
from constants import *
from auxiliar import Auxiliar

class Platforms:
    def __init__ (self,x,y,w,h,type=0,p_scale=1,collition_enabled=True):
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\tileset\\creepy_forest\\Tiles\\Tile ({0}).png",17,flip=False,scale=p_scale,w=w,h=h)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.collition_enabled = collition_enabled

        if(self.collition_enabled):
            self.rect_collition = pygame.Rect(self.rect)
            self.rect_ground_collition = pygame.Rect(self.rect)
            self.rect_ground_collition.height = GROUND_COLLIDE_H
    
    def draw (self,screen):        
        if(DEBUG):
            if(self.collition_enabled):
                pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)
        
    def create_plaforms(lista_plataformas,x,y,w,h,step=1,tile_total=2,p_scale=1,tile_type=0,collition_enabled=True,add_bottom=False):              
        scale = p_scale * GLOBAL_SCALE
        
        type_start = tile_type
        type_mid = type_start + 1
        type_end = type_mid + 1
        
        lista_plataformas.append(Platforms(x=x,y=y,w=w,h=h,type=type_start,p_scale=scale,collition_enabled=collition_enabled))
        for n in range(step,tile_total - 1):
            tile_separation = (w * scale) * n
            lista_plataformas.append(Platforms(x=x + tile_separation,y=y,w=w,h=h,type=type_mid,p_scale=scale,collition_enabled=collition_enabled))
        tile_separation = (w * scale) * (tile_total - 1)
        lista_plataformas.append(Platforms(x=x + tile_separation,y=y,w=w,h=h,type=type_end,p_scale=scale,collition_enabled=collition_enabled))

        if(add_bottom):
            tile_range = int((GROUND_LEVEL - y) / h)

            for n in range(step,tile_range):
                y_position = y + (h * n)
                Platforms.create_plaforms(lista_plataformas,x=x,y=y_position,w=w,h=h,tile_total=tile_total,p_scale=scale,tile_type=3,collition_enabled=False)