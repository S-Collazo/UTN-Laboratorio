import pygame
import sys
from pygame.locals import *
from constants import *
from ui_start_main import StartMain
from ui_start_options import StartOptions
from ui_start_level_selector import LevelSelector

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\background.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()

clock = pygame.time.Clock()

start_main = StartMain(name="main",master_surface = screen,x=300,y=250,w=400,h=300,background_color=None,border_color=None,active=True)
start_options = StartOptions(name="options",master_surface = screen,x=300,y=200,w=400,h=300,background_color=BLACK,border_color=None,active=False)
level_selector = LevelSelector(name="level_selector",master_surface = screen,x=300,y=200,w=400,h=300,background_color=None,border_color=None,active=False)

while True:
    lista_eventos =pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
                    
    delta_ms = clock.tick(FPS)
    
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
        
    if(start_main.active):
        start_main.update(lista_eventos)
        start_main.draw()

    elif(start_options.active):
        start_options.update(lista_eventos)
        start_options.draw()
        
    elif(level_selector.active):
        level_selector.update(lista_eventos)
        level_selector.draw()
    
    pygame.display.flip()