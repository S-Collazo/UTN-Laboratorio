import pygame

class Damage_Control:
    def __init__(self, lista_personajes, lista_enemigos, lista_balas, lista_trampas):
        self.lista_personajes = lista_personajes
        self.lista_enemigos = lista_enemigos
        self.lista_entidades = lista_personajes + lista_enemigos
        self.lista_balas = lista_balas
        self.lista_trampas = lista_trampas

    def damage(self, lista_atacante, lista_atacado):
        for atacante in lista_atacante:
            for atacado in lista_atacado:
                if not (atacado.is_block) and (atacante.is_attack or atacante.is_shoot) and not (atacado.asset_name == atacante.asset_name):
                    if((atacante.rect_body_collition.colliderect(atacado.rect_collition))):
                        atacado.hitpoints -= atacante.attack_power
                        
                        if(atacante.rect.x <= atacado.rect.x):
                            atacado.add_x(25)
                        else:
                            atacado.add_x(-25)    
                        
                        if(atacado.hitpoints - atacante.attack_power <= 0):
                            atacado.is_alive = False
    
    def damage_bullet (self,lista_atacante,lista_atacado):
        self.lista_entidades_edit = lista_atacado
        for atacante in lista_atacante:
            for atacado in lista_atacado:
                    self.lista_entidades_edit.remove(atacado)
                    break
        return self.lista_entidades_edit
                        
    def update(self):
        self.damage(self.lista_personajes, self.lista_enemigos)
        self.damage(self.lista_enemigos, self.lista_personajes)
        self.damage(self.lista_trampas, self.lista_entidades)
        #self.damage_bullet(self.lista_balas, self.lista_entidades)
        self.damage(self.lista_balas, self.lista_entidades)
        
