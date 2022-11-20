import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox

class LevelSelector(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 5
        
        self.lvl1 = Button(master_surface=self,x=self.menu_x,y=10,w=150,h=100,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_XL_06.png",on_click=self.on_click_lvl1,on_click_param="Nivel 1",text="Nivel 1",font="Verdana",font_size=30,font_color=WHITE)
        self.lvl1_easy = Button(master_surface=self,x=self.menu_x,y=35,w=50,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_S_05.png",on_click=self.on_click_lvl1_easy,on_click_param="level_selector",text="Facil",font="Verdana",font_size=10,font_color=BLACK)
        self.lvl1_normal = Button(master_surface=self,x=self.menu_x + 50,y=35,w=50,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_S_08.png",on_click=self.on_click_lvl1_normal,on_click_param="level_selector",text="Normal",font="Verdana",font_size=10,font_color=BLACK)
        self.lvl1_hard = Button(master_surface=self,x=self.menu_x + 100,y=35,w=50,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_S_09.png",on_click=self.on_click_lvl1_hard,on_click_param="level_selector",text="Dificil",font="Verdana",font_size=10,font_color=BLACK)
        
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=205,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_M_05.png",on_click=self.on_click_button_exit,on_click_param="main",text="Volver",font="Verdana",font_size=20,font_color=BLACK)
        
        self.lista_widget = [self.lvl1,self.button_exit]
        
    def on_click_lvl1(self,parametro):
        self.lista_widget.append(self.lvl1_easy)
        self.lista_widget.append(self.lvl1_normal)
        self.lista_widget.append(self.lvl1_hard)
        self.level_number = parametro
    
    def on_click_lvl1_easy(self, parametro):
        self.set_active(parametro)
        self.level_difficulty = 0
    
    def on_click_lvl1_normal (self, parametro):
        self.set_active(parametro)
        self.level_difficulty = 1
        
    def on_click_lvl1_hard (self, parametro):
        self.set_active(parametro)
        self.level_difficulty = 2
        
    def on_click_button_exit (self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()