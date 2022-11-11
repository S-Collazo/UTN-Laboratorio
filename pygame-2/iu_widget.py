import pygame
from constantes import *
from auxiliar import Auxiliar

class Widget:
    def __init__ (self,master_surface,x,y,w,h,background_color=WHITE,border_color=RED):
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.background_color = background_color
        self.border_color = border_color
    
    def render (self):
        pass
            
    def update (self,lista_eventos):
        pass
    
    def draw (self):
        self.master_surface.blit(self.slave_surface,self.slave_rect)