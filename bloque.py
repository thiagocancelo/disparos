import pygame 
                #hereda la clase padre  
class Block(pygame.sprite.Sprite):
    def __init__(self, posicion):
        # llama al constructor de la clase padre 
        super().__init__()

        #cargar la imagen de la pelota 
        self.image = pygame.image.load("assets/sprite/red2.png").convert()

        #obtener rectangulo de la imagen 
        self.rect = self.image.get_rect() 

        self.rect.topleft = posicion 



class Muro(pygame.sprite.Group):           #
    def __init__(self, cantidad_bloques):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 0

        

        for i in range(cantidad_bloques): # c
            bloque = Block((pos_x, pos_y)) 
            self.add(bloque)
            pos_x += bloque.rect.width
            # una vez llegue al ancho maximo de la ventana, 
            # vuelva a la posicion (0) del eje (x),
            #  y empieza otra vez un bloque abajo
            if pos_x >= 800:             
                pos_x= 0
                pos_y += bloque.rect.height # suma la altura del bloque,
                                            #para que baje y empiece otra vez
            
            
            
            
            