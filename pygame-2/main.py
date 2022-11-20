import pygame
import sys
from ui_start import Start
from ui_pause import Pause
from level import Level
from pygame.locals import *
from constants import *
from loot import *
from damage_control import *

flags = DOUBLEBUF

game_state = GAME_MENU

level_number = "Nivel 1"
level_difficulty = 0

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()


pause_menu = Pause(screen)
start = Start(screen)
while True:
    while (game_state == GAME_MENU):
            lista_eventos = pygame.event.get()
            keys = pygame.key.get_pressed()                
            delta_ms = clock.tick(FPS)
                
            game_state = start.start_menu(delta_ms,lista_eventos,keys)
            
            level_number = start.level_number
            level_difficulty = start.level_difficulty
            
            pygame.display.flip()

    else:
        level = Level(screen,level_number,level_difficulty)
        
        while not (game_state == GAME_MENU):
            while (game_state == GAME_PAUSE):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                game_state = pause_menu.pause_level(delta_ms,lista_eventos)
                
                pygame.display.flip()
                    
            while (game_state == GAME_RUNNING):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                pause_menu.pause_main.active = True
                game_state = level.run_level(delta_ms,lista_eventos,keys)
                    
                pygame.display.flip()


        
            