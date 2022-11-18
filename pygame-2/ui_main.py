import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form_menu_A import FormMenuA
from ui_form_menu_B import FormMenuB

def ui_main ():
    flags = DOUBLEBUF
    
    pause = True

    screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

    pygame.init()

    clock = pygame.time.Clock()

    form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=100,y=100,w=800,h=400,background_color=(255,255,0),border_color=(255,0,255),active=True)
    form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=100,y=100,w=800,h=400,background_color=(0,255,255),border_color=(255,0,255),active=False)

    while (pause):
        lista_eventos =pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
        
        keys = pygame.key.get_pressed()
                        
        delta_ms = clock.tick(FPS)
            
        if(form_menu_A.active):
            form_menu_A.update(lista_eventos)
            form_menu_A.draw()

        elif(form_menu_B.active):
            form_menu_B.update(lista_eventos)
            form_menu_B.draw()
        
        pygame.display.flip()
    
    return pause