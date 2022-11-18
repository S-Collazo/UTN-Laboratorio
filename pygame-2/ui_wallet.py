import pygame
from pygame.locals import *
from constants import *
from ui_widget import Widget
from auxiliar import Auxiliar

class Wallet (Widget):
    def __init__(self,player,master_surface,x=(ANCHO_VENTANA-10),y=10,w=100,h=25,background_color=None,border_color=None,background_image=None,text="NULL",font="Times",font_size=20,font_color=BLACK,bold=True):
        self.text = "{0}".format(player.currency)
        super().__init__(master_surface,x,y,w,h,background_color,border_color,background_image,self.text,font,font_size,font_color,True)
        self.render()
         
    def render(self):
        super().render()

    def update(self,lista_eventos,player):
        self._text = "{0}".format(player.currency)
        self.render()
