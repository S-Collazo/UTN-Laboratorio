import pygame
from constantes import *
from auxiliar import Auxiliar
from iu_widget import Widget
from iu_boton import Button

class Form (Widget):
    def __init__ (self,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(master_surface,x,y,w,h,background_color,border_color)
        self.slave_surface = pygame.Surface((w,h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.active = active
            
    def render (self):
        pass
            
    def update (self,lista_eventos):
        pass
    
class FormMenu(Form):
    def __init__ (self,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(master_surface,x,y,w,h,background_color,border_color,active)
        
        self.button_1 = Button(master_surface=self.slave_surface,x=200,y=50,w=200,h=50,background_color=BLUE,border_color=GREEN,on_click="0",on_click_param="1",text="Hola",font="Verdana",font_size=20,font_color=PURPLE)
        self.lista_botones = [self.button_1]
     
    def on_click_buton_1(self,parameter):
        print(parameter)
        
    def update(self,lista_eventos):
        super().update(lista_eventos=lista_eventos)
        for aux_boton in self.lista_botones:
            aux_boton.update(lista_eventos)
        
    def draw (self):
        super().draw()
        for aux_boton in self.lista_botones:
            aux_boton.draw()