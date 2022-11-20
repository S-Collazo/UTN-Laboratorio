import pygame
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_progressbar import *
from ui_wallet import Wallet

class ScreenInfo(Form):
    def __init__(self,entity,name,master_surface,x,y,w,h,background_color=None,border_color=None,active=True):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
                
        self.hp_bar = HitpointBar(player=entity,master_surface=self,x=10,y=10,w=200,h=25)
        self.wallet = Wallet(player=entity,master_surface=self,x=(ANCHO_VENTANA-80),y=10,w=75,h=25)
               
        self.lista_widget = [self.hp_bar,self.wallet]
        
    def update(self,lista_eventos,player):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos,player)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()