import pygame
import sys
from constantes import *
from player import Player

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()

clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\01.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player1 = Player(0,0,4,8,0,16)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1.control("walk_r",5)
            if event.key == pygame.K_LEFT:
                player1.control("walk_l",-5)
            if event.key == pygame.K_SPACE:
                player1.control("JUMP_R")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player1.control("stay_r")
            if event.key == pygame.K_LEFT:
                player1.control("stay_l")
    
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
       
    player1.update()
    player1.draw(screen)
    
    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)
    