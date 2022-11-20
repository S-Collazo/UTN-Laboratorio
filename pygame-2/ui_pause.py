import pygame
import sys
from pygame.locals import *
from constants import *
from ui_pause_main import PauseMain
from ui_pause_options import PauseOptions

class Pause:
    def __init__ (self,screen):
        self.screen = screen
        self.pause_main = PauseMain(name="pause_main",master_surface = screen,x=300,y=200,w=400,h=300,background_color=GREY,border_color=None,active=True)
        self.pause_options = PauseOptions(name="pause_options",master_surface = screen,x=300,y=200,w=400,h=300,background_color=GREY,border_color=None,active=False)
        
    def pause_level (self,delta_ms,lista_eventos):
        self.pause_status = True
        
        for event in lista_eventos:
            for event in lista_eventos:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause_status = False
                                    
        if(self.pause_main.active):
            self.pause_main.update(lista_eventos)
            self.pause_main.draw()
        else:
            self.pause_options.update(lista_eventos)
            self.pause_options.draw()
                    
        return self.pause_status