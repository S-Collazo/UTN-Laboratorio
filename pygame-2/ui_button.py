import pygame
from pygame.locals import *
from constants import *
from auxiliar import Auxiliar
from ui_widget import Widget
    
class Button(Widget):
    def __init__ (self,master_surface,x,y,w,h,background_color,border_color,on_click,on_click_param,text,font,font_size,font_color):
        super().__init__(master_surface,x,y,w,h,background_color,border_color)
        pygame.font.init()
        
        self.on_click = on_click
        self.on_click_param = on_click_param
        
        self._text = text
        self.font_sys = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        
        self.render()
            
    def render (self):
        image_text = self.font_sys.render(self._text,True,self.font_color,self.background_color)
        
        self.slave_surface = pygame.surface.Surface((self.w,self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        
        self.slave_rect_collition = pygame.Rect(self.slave_rect)
        self.slave_rect_collition.x += self.master_form.x
        self.slave_rect_collition.y += self.master_form.y
        
        self.slave_surface.fill(self.background_color)
        self.slave_surface.blit(image_text,(5,5))
        # self.border = pygame.draw.rect(self.slave_surface,self.border_color,self.slave_rect)
                 
    def update (self,lista_eventos):
        for evento in lista_eventos:
            if (evento.type == pygame.MOUSEBUTTONDOWN):
                if (self.slave_rect_collition.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)
        
        self.render()