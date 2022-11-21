import pygame
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_progressbar import *
from ui_textbox import TextBox
from ui_wallet import Wallet
from ui_timer import Timer

class ScreenInfo(Form):
    def __init__(self,entity,name,master_surface,x,y,w,h,background_color=None,border_color=None,active=True):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
                        
        self.hp_bar = HitpointBar(player=entity,master_surface=self,x=10,y=10,w=200,h=25)
        self.wallet = Wallet(player=entity,master_surface=self,x=(ANCHO_VENTANA-80),y=10,w=75,h=25)
        self.timer = Timer(master_surface=self,x=450,y=10,w=100,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_M_09.png",font="Verdana",font_size=20,font_color=BLACK)
               
        self.lista_widget = [self.hp_bar,self.wallet,self.timer]
        
    def update(self,lista_eventos,player,timer):     
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos,player,timer)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()