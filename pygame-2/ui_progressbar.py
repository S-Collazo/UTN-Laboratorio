import pygame
from pygame.locals import *
from ui_widget import Widget
from constants import *

class ProgressBar(Widget):
    def __init__(self,master_surface,x=0,y=0,w=200,h=50,background_color=GREEN,border_color=RED,background_image=None,image_progress=None,value=1,value_max=5):
        super().__init__(master_surface,x,y,w,h,background_color,border_color,background_image,None,None,None,None)
       
        self.surface_element = pygame.image.load(image_progress)
        self.surface_element = pygame.transform.scale(self.surface_element,(w/value_max, h)).convert_alpha()

        self.value = value
        self.value_max = value_max
        self.render()
        
    def render(self):
        super().render()
        for x in range(self.value):
            self.slave_surface.blit(self.surface_element, (x*self.w/self.value_max, 0))

    def update(self,lista_eventos):
        self.render()