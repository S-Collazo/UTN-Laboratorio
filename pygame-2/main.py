import pygame
import sys
from ui_start import Start
from ui_pause import Pause
from ui_death import Death
from ui_win import Win
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

while True:
    start = Start(screen)
    pause_menu = Pause(screen)
    death = Death(screen)
    
    while (game_state == GAME_MENU):
            lista_eventos = pygame.event.get()
            keys = pygame.key.get_pressed()                
            delta_ms = clock.tick(FPS)
                
            game_state = start.start_menu(delta_ms,lista_eventos,keys)
            
            level_number_value = start.level_number_value
            level_number = "Nivel {0}".format(level_number_value)
            level_difficulty = start.level_difficulty
            
            pygame.display.flip()

    else:
        if (game_state == GAME_RESTART or game_state == GAME_CONTINUE):
            if (game_state == GAME_CONTINUE):
                level_number_value += 1
                level_number = level_number = "Nivel {0}".format(level_number_value)
            game_state = GAME_RUNNING
        
        level = Level(screen,level_number,level_difficulty)
        win = Win(screen,level.lista_personajes[0],level.time_final,level.has_spawner,level.boss_room)
                
        while not (game_state == GAME_MENU or game_state == GAME_RESTART or game_state == GAME_CONTINUE):
            while (game_state == GAME_PAUSE):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                death.death_main.active = True
                            
                game_state = pause_menu.pause_level(delta_ms,lista_eventos)
                
                pygame.display.flip()
                    
            while (game_state == GAME_RUNNING):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                pause_menu.pause_main.active = True
                death.death_main.active = True
                
                game_state = level.run_level(delta_ms,lista_eventos,keys)
                    
                pygame.display.flip()
                
            while (game_state == GAME_DEATH):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                pause_menu.pause_main.active = True
                
                game_state = death.death_screen(delta_ms,lista_eventos)
                
                pygame.display.flip()
                
            while (game_state == GAME_VICTORY):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                pause_menu.pause_main.active = True
                death.death_main.active = True
                
                game_state = win.win_screen(delta_ms,lista_eventos,level.lista_personajes[0],level.time_final)
                
                pygame.display.flip()


        
            