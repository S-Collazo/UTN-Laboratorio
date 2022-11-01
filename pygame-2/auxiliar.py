import pygame

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas,flip=False, step = 1):
        lista_sprite = []
        surface_image = pygame.image.load(path)
        
        fotograma_ancho = int(surface_image.get_width() / columnas)
        fotograma_alto = int(surface_image.get_height() / filas)

        for columna in range(0,columnas,step):
            for fila in range(filas):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_image.subsurface(x,y,fotograma_ancho,fotograma_alto)
                
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                
                lista_sprite.append(surface_fotograma)
                
        return lista_sprite
