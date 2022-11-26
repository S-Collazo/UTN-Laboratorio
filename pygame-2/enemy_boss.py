import pygame
from constants import *
from enemy import Enemy
from ammo import Ammo
from auxiliar import Auxiliar

class Boss(Enemy):
    def __init__(self, asset, name, x, y, gravity, frame_rate_ms, move_rate_ms, p_scale=1.2):
        self.asset = asset
        super().__init__(self.asset, "Bosses", name, x, y, gravity,frame_rate_ms, move_rate_ms, p_scale)
        
        self.direction = DIRECTION_L

        self.attack_special_r = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=False,p_scale=self.p_scale)
        self.attack_special_l = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=True,p_scale=self.p_scale)

    def update(self, delta_ms, lista_plataformas, lista_oponente, lista_balas, lista_items,item_asset):
        super().update(delta_ms, lista_plataformas, lista_items,item_asset)
        self.events(delta_ms,lista_oponente,lista_balas)

    def draw(self, screen):
        super().draw(screen)

    def events(self, delta_ms,lista_oponente,lista_balas):
        self.tiempo_transcurrido += delta_ms
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas,asset=self.asset_type)

        for oponente in lista_oponente:
            self.player_position_x = oponente.rect_body_collition.x
            self.player_position_y = oponente.rect.y
            self.distance_difference_x = self.rect_body_collition.x - oponente.rect_body_collition.x
            self.distance_difference_y = self.rect.y - oponente.rect.y

            self.attack(False)
            self.block(False)
            self.shoot(lista_balas,False)

            if(abs(self.distance_difference_x) <= (ANCHO_VENTANA - 100)):
                if (abs(self.distance_difference_x) <= 300):
                    if(self.is_shooting == False and ((self.tiempo_transcurrido - self.tiempo_last_shoot) > self.interval_time_shoot)):
                        self.shoot(lista_balas)
                        self.tiempo_last_shoot = self.tiempo_transcurrido
                
                elif(abs(self.distance_difference_x) <= 50):
                    if(oponente.is_attack and (self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                        self.block()
                        self.tiempo_last_block = self.tiempo_transcurrido
                    else:
                        if ((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                            self.attack()
                            self.tiempo_last_attack = self.tiempo_transcurrido
                                
                else:
                    if(self.distance_difference_x >= 0):
                        super().walk(DIRECTION_L)
                    else:
                        super().walk(DIRECTION_R)
         
                for bala in lista_balas:
                    if(abs(self.rect.x - bala.rect.x) <= (self.rect.w + 50)):
                        if((self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                            self.block()
                            self.tiempo_last_block = self.tiempo_transcurrido