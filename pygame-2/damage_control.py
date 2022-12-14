import pygame

class Damage_Control:
    def __init__(self, lista_personajes, lista_enemigos, lista_balas, lista_trampas):
        self.lista_personajes = lista_personajes
        self.lista_enemigos = lista_enemigos
        self.lista_balas = lista_balas
        self.lista_trampas = lista_trampas

    def damage(self, lista_atacante, lista_atacado):
        for atacante in lista_atacante:
            for atacado in lista_atacado:
                if (atacado.is_alive):
                    if not (atacado.is_block or atacado.is_dying or atacado.is_hurt) and (atacante.is_attack or atacante.is_shoot) and not (atacado.asset_name == atacante.asset_name):
                        if((atacante.rect_body_collition.colliderect(atacado.rect_collition))):
                            atacado.hitpoints -= atacante.attack_power
                            
                            if(atacante.rect.x <= atacado.rect.x):
                                atacado.add_x(25)
                            else:
                                atacado.add_x(-25)    
                            
                            if(atacado.hitpoints - atacante.attack_power <= 0):
                                atacado.is_dying = True
                                atacado.death()
                            else:
                                atacado.is_hurt = True
                                atacado.hurt()
                            
    def update(self):
        self.lista_entidades = self.lista_personajes + self.lista_enemigos
        self.damage(self.lista_personajes, self.lista_enemigos)
        self.damage(self.lista_enemigos, self.lista_personajes)
        self.damage(self.lista_trampas, self.lista_entidades)
        self.damage(self.lista_balas, self.lista_entidades)
        
        
