from tkinter import Y
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__ (self,x,y,speed_walk,speed_run,gravity,jump) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\walk.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\idle.png",16,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\jump.png",33,1,False,2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\\images\\caracters\\stink\\jump.png",33,1,True,2)
        self.frame = 0
        
        self.lives = 5
        self.score = 0
        
        self.move_x = x
        self.move_y = y
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump = jump
        self.is_jump = False
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
    
    def control(self,action,x=0,y=0):
        if (action == "walk_r"):
            self.animation = self.walk_r
            self.move_x = self.speed_walk
            self.frame = 0
        elif (action == "walk_l"):
            self.animation = self.walk_l
            self.move_x = self.speed_walk
            self.frame = 0
            
        if (action == "jump_r"):
            self.animation = self.jump_r
            self.move_y = -self.jump
            self.move_x = self.speed_walk
            self.frame = 0
            self.is_jump = True
        elif (action == "jump_l"):
            self.animation = self.jump_l
            self.move_y = self.jump
            self.frame = 0
            self.is_jump = True
            
        if (action == "stay_r"):
            self.animation = self.stay_r
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
        if(action == "stay_l"):
            self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0 
        
    def update (self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0
            if(self.is_jump == True):
                self.is_jump = False
                self.move_y = 0
            
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        
        if(self.rect.y < 600):
            self.rect.y += self.gravity
    
    def draw (self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        