import pygame

class Plataforma(pygame.sprite.Sprite):

    def __init__(self):
       super().__init__()
       self.spritesheet_x=pygame.image.load ("assets/sprite/paddle.png").convert_alpha()
       self.spritesheet_x.set_clip(pygame.Rect(0,0, 70, 25))
       self.image=self.spritesheet_x.subsurface(self.spritesheet_x.get_clip())  


       self.rect = self.image.get_rect()
       self.rect.x = 400
       self.rect.y = 520

    def update(self, direccion):
        
        if direccion == "derecha":
            
            #self.clip(self.frames_derecha)
            if self.rect.x >= 1500:
                self.rect.x = 0
            else:
                self.rect.x +=8
        
        elif direccion == "izquierda":
            #self.clip(self.frames_izquierda)
            if self.rect.x <= 0:
                self.rect.x = 500
            self.rect.x -=8
        

        self.image = self.spritesheet_x.subsurface(self.spritesheet_x.get_clip())

    
    def administrar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_RIGHT:
          
                self.update("derecha")
            
            if evento.key == pygame.K_LEFT:
                self.update("izquierda")
            
