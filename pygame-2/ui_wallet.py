import pygame
from pygame.locals import *
from constants import *
from ui_widget import Widget
from auxiliar import Auxiliar

class Wallet (Widget):
    def __init__(self,player,master_surface,x=(ANCHO_VENTANA-10),y=10,w=100,h=25,background_color=None,border_color=None,font="Times",font_size=20,font_color=BLACK,bold=True):
        self.text = "{0}".format(player.currency)
        self.background_image = PATH_RECURSOS + "\gui\set_gui_01\Paper\Elements\Element08.png"
        super().__init__(master_surface,x,y,w,h,background_color,border_color,self.background_image,self.text,font,font_size,font_color,True)
        self.render()
         
    def render(self):
        super().render()

    def update(self,lista_eventos,player,timer):
        self._text = "{0}".format(player.currency)
        self.render()
