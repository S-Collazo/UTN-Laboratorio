import pygame
import sys
from pygame.locals import *
from constantes import *
from iu_formulario import FormMenu

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()

form_menu = FormMenu(master_surface = screen,x=0,y=0,w=500,h=500,background_color=PURPLE,border_color=ORANGE,active=True)

while True:
    lista_eventos =pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
                       
    delta_ms = clock.tick(FPS)
        
    if(form_menu.active):
        form_menu.update(lista_eventos)
        form_menu.draw()
        
    """
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    """
      
    pygame.display.flip()