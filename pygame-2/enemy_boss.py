import pygame
from constants import *
from enemy import Enemy
from ammo import Ammo
from auxiliar import Auxiliar

class Boss(Enemy):
    def __init__(self, asset, x, y, gravity, frame_rate_ms, move_rate_ms, p_scale=1.2):
        self.asset = asset
        self.asset_name = asset["name"]
        super().__init__(self.asset, "Bosses", self.name["name"], x, y, gravity,frame_rate_ms, move_rate_ms, p_scale)

        self.attack_special_r = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=False,p_scale=self.p_scale)
        self.attack_special_l = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=True,p_scale=self.p_scale)

    def update(self, delta_ms, lista_plataformas, lista_oponente, lista_balas, lista_items,item_asset):
        super().update(delta_ms, lista_plataformas, lista_items,item_asset)
        self.events(delta_ms, lista_oponente)

    def draw(self, screen):
        super().draw(screen)

    def events(self, delta_ms, lista_oponente):
        self.tiempo_transcurrido += delta_ms

        if(self.x <= ANCHO_VENTANA / 2):
            self.posicion_extremo_a = 5
            self.posicion_extremo_b = self.x
        else:
            self.posicion_extremo_a = self.x
            self.posicion_extremo_b = ANCHO_VENTANA - (self.rect.w + 25)

        for oponente in lista_oponente:
            self.player_position_x = oponente.rect_body_collition.x
            self.player_position_y = oponente.rect.y
            self.distance_difference_x = self.rect_body_collition.x - oponente.rect_body_collition.x
            self.distance_difference_y = self.rect.y - oponente.rect.y

            self.attack(False)

            if(abs(self.distance_difference_x) <= 500 and abs(self.distance_difference_y) <= 50):
                if(abs(self.distance_difference_x) <= 100):
                    if ((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                        self.attack()
                        self.tiempo_last_attack = self.tiempo_transcurrido
                else:
                    if(self.distance_difference_x >= 0):
                        super().walk(DIRECTION_L)
                    else:
                        super().walk(DIRECTION_R)
            else:
                if(self.rect.x >= self.posicion_extremo_a and self.rect.x <= self.posicion_extremo_b):
                    super().walk(self.direction)
                else:
                    if(self.rect.x < self.posicion_extremo_a):
                        super().walk(DIRECTION_R)
                    if(self.rect.x > self.posicion_extremo_b):
                        super().walk(DIRECTION_L)