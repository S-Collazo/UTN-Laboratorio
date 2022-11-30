import pygame
import sys
from pygame.locals import *
from constants import *
from ui_highscore_main import HighscoreMain
from ui_highscore_table import HighscoreTable

class Highscore:
    def __init__ (self,screen):
        self.screen = screen
        
        #self.background_image = pygame.image.load(PATH_RECURSOS + "\\background.png")
        #self.background_image = pygame.transform.scale(self.background_image,(ANCHO_VENTANA,ALTO_VENTANA))
        
        self.highscore_main = HighscoreMain(name="highscore_main",master_surface=screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=PURPLE,border_color=None,active=True)
        self.highscore_table = HighscoreTable(name="highscore_table",master_surface=screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=PURPLE,border_color=None,active=False)
        
        self.score = 0
        self.exit = False
        
    def highscore_screen (self,delta_ms,lista_eventos,score_list):
        self.game_state = GAME_END
            
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #self.screen.blit(self.background_image,self.background_image.get_rect())
                                         
        if(self.highscore_main.active):
            self.highscore_main.update(lista_eventos,score_list)
            self.highscore_main.draw()
            self.score = self.highscore_main.final
            self.exit = self.highscore_main.exit
        elif(self.highscore_table.active):
            self.highscore_table.update(lista_eventos,self.score)
            self.highscore_table.draw()
            self.exit = self.highscore_table.exit
        else:
            if (self.exit):
                self.game_state = GAME_MENU
                return self.game_state
                    
        return self.game_state