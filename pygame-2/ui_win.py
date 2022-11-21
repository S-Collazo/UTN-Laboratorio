import pygame
import sys
from pygame.locals import *
from constants import *
from ui_win_main import WinMain

class Win:
    def __init__ (self,screen,player,time):
        self.screen = screen
        self.win_main = WinMain(player,time,name="win_main",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=GREY,border_color=None,active=True)
        
        self.exit = False
        
    def win_screen (self,delta_ms,lista_eventos,player,time):
        self.game_state = GAME_VICTORY
            
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                         
        if(self.win_main.active):
            self.win_main.update(lista_eventos,player,time)
            self.win_main.draw()
            self.exit = self.win_main.exit
        else:
            if (self.exit):
                self.game_state = GAME_MENU
                return self.game_state
            else:
                self.game_state = GAME_RESTART
                return self.game_state
                    
        return self.game_state