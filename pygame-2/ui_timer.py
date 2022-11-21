import pygame
from pygame.locals import *
from constants import *
from auxiliar import Auxiliar
from ui_widget import Widget

class Timer(Widget):
    def __init__ (self,master_surface,x,y,w=100,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_M_09.png",font="Verdana",font_size=15,font_color=BLACK):
        self.timer_sec = 0
        self.timer_min = 0
        self.text = "{0}:{1}".format(self.timer_min,self.timer_sec)
        
        super().__init__ (master_surface,x,y,w,h,background_color,border_color,background_image,self.text,font,font_size,font_color)

        self.render()
            
    def render (self):
        super().render()
        
    def update(self,lista_eventos,player,timer):
        self.timer_sec = int(timer / 1000 % 60)
        self.timer_min = int(timer/60000 % 24)
        
        self._text = "{:02d}:{:02d}".format(self.timer_min,self.timer_sec)
        self.render()
        
        super().update()
    
    def draw(self):
        super().draw()