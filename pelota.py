import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # llama al constructor de la clase padre

        # cargo la imagen de la pelota
        self.image = pygame.image.load("assets/sprite/ball.png").convert()

        #obtener rect de la imagen
        self.rect = self.image.get_rect()

        # posicion la pelota en el centro de la ventana
        self.rect.centerx = 600 / 2 
        self.rect.centery = 800 / 2

        # defino la velocidad del objeto pelota
        self.velocidad = [5, 5] # es el valor de la velocidad 
                                # en el eje(x) e (y)


        