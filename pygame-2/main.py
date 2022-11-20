import pygame
import sys
import ui_start_level_selector
from ui_pause import Pause
from level import Level
from pygame.locals import *
from constants import *
from loot import *
from damage_control import *

flags = DOUBLEBUF

pause_status = False

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()

level = Level(screen,"Nivel 1",1)
pause_menu = Pause(screen)

while True:
    lista_eventos = pygame.event.get()
            
    keys = pygame.key.get_pressed()
            
    delta_ms = clock.tick(FPS)
        
    if(pause_status):
        pause_status = pause_menu.pause_level(delta_ms,lista_eventos)
    else:
        pause_status = level.run_level(delta_ms,lista_eventos,keys)
        
    pygame.display.flip()


        
            