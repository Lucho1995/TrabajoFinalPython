import pygame,sys
from pygame.locals import *
red =(255,0,0)
pygame.init()
ventana = pygame.display.set_mode((600,500))
pygame.display.set_caption("hola")
#pygame.display.flip()
#ventana.fill(red)
imagen = pygame.image.load("imagenes/mano.png").convert()
posX,posY=50,50
ventana.blit(imagen,(200,1))
while True:
    for evento in pygame.event.get():
        if evento.type ==QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
slrgjoidfgoi´sjgposMGPORWJGPORMG
slrgjoidfgoi´sjgposMGPORWJGPORMGSG
slrgjoidfgoi´sjgposMGPORWJGPORMGSGSBS
RB