import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox

class WinMain(Form):
    def __init__(self,player,time,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 3
        
        self.time = "Tiempo: {0}".format(time)
        self.score = "Puntuación: {0}".format(player.currency)
        self.time_bonus = "Bonificación por tiempo: {0}".format(0)
        self.score_final = "Puntuación Final: {0}".format(player.currency)
                
        self.button_continue = Button(master_surface=self,x=self.menu_x + 50,y=540,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_M_07.png",on_click=self.on_click_button_continue,on_click_param="level_selector",text="Siguiente Nivel",font="Verdana",font_size=20,font_color=BLACK)
        self.button_restart = Button(master_surface=self,x=self.menu_x + 50,y=600,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_L_08.png",on_click=self.on_click_button_restart,on_click_param="ScreenInfo",text="Reiniciar Nivel",font="Verdana",font_size=20,font_color=WHITE)
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=660,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_L_06.png",on_click=self.on_click_button_exit,on_click_param=None,text="Menu Principal",font="Verdana",font_size=20,font_color=WHITE)
              
        self.txt1 = TextBox(master_surface=self,x=self.menu_x,y=100,w=300,h=150,background_color=None,border_color=None,background_image=None,text="VICTORIA",font="Verdana",font_size=60,font_color=BLACK)
        self.txt2 = TextBox(master_surface=self,x=self.menu_x,y=350,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.time,font="Verdana",font_size=15,font_color=BLACK)
        self.txt3 = TextBox(master_surface=self,x=self.menu_x,y=300,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.score,font="Verdana",font_size=15,font_color=BLACK)
        self.txt4 = TextBox(master_surface=self,x=self.menu_x,y=400,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.time_bonus,font="Verdana",font_size=15,font_color=BLACK)
        self.txt5 = TextBox(master_surface=self,x=self.menu_x + 25,y=450,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.score_final,font="Verdana",font_size=15,font_color=BLACK)
        
        self.lista_widget = [self.button_continue,self.button_restart,self.button_exit,self.txt1,self.txt2,self.txt3,self.txt4,self.txt5]
        
        self.game_state = GAME_VICTORY
        self.exit = False

    def on_click_button_continue(self,parametro) -> bool:
        self.set_active(parametro)
        self.exit = True

    def on_click_button_restart(self,parametro) -> bool:
        self.set_active(parametro)
        self.exit = False
    
    def on_click_button_exit (self, parametro):
        self.set_active(parametro)
        self.exit = True

    def bonus (self,time_sec,time_min):
        if (time_min == 0):    
            if (time_sec <= 30):
                self.bonus_value = 2
            elif (time_sec <= 20):
                self.bonus_value = 3
            elif (time_sec <= 10):
                self.bonus_value = 4
        else:
            self.bonus_value = 1 
        
        return self.bonus_value

    def update(self, lista_eventos,player,time):
        self.timer_sec = int(time / 1000 % 60)
        self.timer_min = int(time/60000 % 24)
        
        self.bonus_time = self.bonus(self.timer_sec,self.timer_min)
        self.score_final = int(player.currency * self.bonus_time)
    
        self.txt2._text = "Tiempo: {:02d}:{:02d}".format(self.timer_min,self.timer_sec)
        self.txt3._text = "Puntuación: {0}".format(player.currency)
        self.txt4._text = "Bonus por tiempo: x{0}".format(self.bonus_time)
        self.txt5._text = "Puntuación Final: {0}".format(self.score_final)
        
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()