import pygame
import sys
import re
import random
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox
from database import Database

class HighscoreRegister(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 4
               
        self.score = 0
                  
        self.txt1 = TextBox(master_surface=self,x=self.menu_x-100,y=100,w=300,h=50,background_color=None,border_color=None,background_image=None,text="Nombre (cuatro letras):",font="Verdana",font_size=15,font_color=WHITE)
        self.txt2 = TextBox(master_surface=self,x=self.menu_x,y=200,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_M_08.png",text="",font="Verdana",font_size=15,font_color=BLACK)
        
        self.lista_widget = [self.txt1,self.txt2]
        
        self.game_state = GAME_END
        self.exit = False
        
    def register_name (self):
        self.nombre = self.txt2._text
        self.nombre = self.nombre.upper()
        
        if not (re.match("^[A-Z]{4}$",self.nombre) == None):            
            old_player = Database.check_registered_highscore(self.nombre)
            
            if(old_player):
                higher_score = Database.compare_highscore(self.nombre,self.score)
                if (higher_score):
                    Database.update_highscore(self.nombre,self.score)
            else:
                id_num = random.randrange(1000,9999)
                Database.add_highscore(id_num,self.nombre,self.score)
                
            self.set_active("highscore_table")
        else:
            self.txt2._text = ""
    
    def update(self, lista_eventos,score):
        self.score = score
        
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.txt2._text = ""
                    self.set_active("highscore_table")
                elif event.key == pygame.K_RETURN:
                    self.register_name()
                    
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()