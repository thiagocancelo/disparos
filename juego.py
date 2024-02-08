import pygame

from plataforma import Plataforma
from pelota import Ball
from bloque import Muro
import sys
import sqlite3
import datetime 

class Juego:

    fps = pygame.time.Clock()  # es el fotograma por segundo

    ventana = pygame.display.set_mode([800,600]) #crear ventana
    pygame.display.set_caption("juego de bloques gallardo - lema - cancelo") # muestra el titulo de la ventana

    plataforma = Plataforma() 
    pelota = Ball()
    muro= Muro(60)

    vida = 3

    Puntaje = 0


    def guardar_datos(self):
        fecha=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") #muestra la hora y fecha actual
        print(fecha)
        con = sqlite3.connect("disparo")

        con.execute("insert into disparo(fecha, puntos) values (?,?)", (fecha, self.Puntaje)) # inserta los valores de la tabla 


        con.commit() # deja guardado los valores actualizados
        con.close() # cierra la conexion 


    def mostrar_Puntaje(self):   # muestra el puntaje en la ventana
        letra30 = pygame.font.SysFont("Arial", 20)
        imagenTextoPresent = letra30.render("puntaje: " +str(self.Puntaje) , True, (255,255,255) )
        rectanguloTextoPresent = imagenTextoPresent.get_rect()
        rectanguloTextoPresent.x = 500
        rectanguloTextoPresent.y = 30
        self.ventana.blit(imagenTextoPresent, rectanguloTextoPresent)


    def mostrar_vida(self):
        letra30 = pygame.font.SysFont("Arial", 20)
        imagenTextoPresent = letra30.render("VIDA: " +str(self.vida) , True, (255,255,255) )
        rectanguloTextoPresent = imagenTextoPresent.get_rect()
        rectanguloTextoPresent.x = 700
        rectanguloTextoPresent.y = 30
        self.ventana.blit(imagenTextoPresent, rectanguloTextoPresent)

    def mostrar_gameover(self):
        letra30 = pygame.font.SysFont("Arial", 80)
        imagenTextoPresent = letra30.render("Game Over" , True, (255,0,0) )
        rectanguloTextoPresent = imagenTextoPresent.get_rect()
        rectanguloTextoPresent.x = 200
        rectanguloTextoPresent.y = 300
        self.ventana.blit(imagenTextoPresent, rectanguloTextoPresent)
        pygame.display.flip()

    def iniciar_juego(self):
        pygame.init()       # inicializa pygame 
        pygame.mixer.init()

        sonido_fondo = pygame.mixer.Sound("./assets/sonidos/ambiente.mp3")
        pygame.mixer.Sound.play(sonido_fondo, -1) # ejecuta el sonido de fondo
        
        while True:

            
           

            for  event in pygame.event.get():
               if event.type== pygame.KEYDOWN:
                   if event.key== pygame.K_RIGHT: # hace que se mueva la plata forma a la derecha 
                       print("tecla derecha")
          
               if event.type == pygame.MOUSEBUTTONDOWN:
                  
                   pass
              


               if event.type == pygame.QUIT:
                   pygame.quit(self)      # cierra el juego 
                   sys.exit(self)
            
            self.ventana.fill((40, 230, 110))

            #self.muro.draw(self.ventana)

            
            self.ventana.blit(self.plataforma.image, self.plataforma.rect) # carga el sprite en la ventana 

                
            self.ventana.blit(self.pelota.image, self.pelota.rect)
            
            
            self.muro.draw(self.ventana) # dibuja todos los bloques en la ventana 

            
            #dibujar en la ventana del juego un sprite

            #self.Puntaje = self.pelota.actualizar_posicion(self.plataforma, self.muro, self.Puntaje)

            if self.pelota.rect.y >= 580: # limite de ventana
                if self.vida > 0:
                    self.vida -= 1         
                self.pelota.rect.x=400 #hace que la pelota aparezca 
                self.pelota.rect.y=300 #en el medio de la ventana
                
            

            if self.pelota.rect.colliderect(self.plataforma.rect):
                self.pelota.velocidad[1] = -self.pelota.velocidad[1]
                # verifica que la pelota choca con la plata forma 
                # e invierte la velocidad

            sprite = pygame.sprite.spritecollideany(self.pelota, self.muro)
            
            if sprite:
                print("choco muro")
                self.pelota.velocidad[1] = -self.pelota.velocidad[1] #invierte la direccion de la pelota en el eje y 
                sprite.kill() #elimina el bloque que choco la pelota
                self.Puntaje += 5


            if self.pelota.rect.top <= 0:
                # invertir la posicion del eje y 
                self.pelota.velocidad[1] = -self.pelota.velocidad[1]
            elif self.pelota.rect.top >= 800: 
                # invertir la posicion del eje x
                self.pelota.velocidad[0] = -self.pelota.velocidad[0]


            
            elif self.pelota.rect.right >= 800:
    
                # invertir la posicion del eje y 
                self.pelota.velocidad[0] = -self.pelota.velocidad[0]
    

            elif self.pelota.rect.left <= 0:

                # invertir la posicion del eje y 
                self.pelota.velocidad[0] = -self.pelota.velocidad[0]
            

            self.pelota.rect.move_ip(self.pelota.velocidad)
            self.pelota.image.set_colorkey((0,0,0))


            if self.vida == 0:
                self.mostrar_gameover()
                

                self.guardar_datos()
                pygame.time.delay(3000)

                
                sys.exit()

            #if vida:
            #    self.vida = vida


            self.plataforma.administrar_eventos(event)

            self.mostrar_vida()
            self.mostrar_Puntaje()
        
           
            
            pygame.display.flip()
            self.fps.tick(30)

        

       
        
            
            
juego = Juego()
juego.iniciar_juego()