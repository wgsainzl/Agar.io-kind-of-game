#Importar librerias

import pygame

from pygame.locals import *

import random

#Pygame setup

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

running = True

dt = 0

c=0

p=0

collide=False

ctemp=0

ttemp=0

direct_y=0

direct_x=0

puntos=0

tam_rect=30

tam_player=30

tam_puntos=10

mov_malo_y=.4

mov_malo_x=1

malo1_mov=0

malo2_mov=0

malo3_mov=0

malo4_mov=0

mov_malo1_y=.4

mov_malo2_y=-.4

mov_malo3_x=1

mov_malo4_x=-1

 

#Inicializar cuadros de puntos

amarillo_pos=[]

for i in range(15):

    amarillo_pos_temp=[]

    amarillo_pos_temp.append(random.randrange(1280))

    amarillo_pos_temp.append(random.randrange(720))

    amarillo_pos.append(amarillo_pos_temp)

morado_pos=[]

for i in range(10):

    morado_pos_temp=[]

    morado_pos_temp.append(random.randrange(1280))

    morado_pos_temp.append(random.randrange(720))

    morado_pos.append(morado_pos_temp)

green_pos=[]

for i in range(5):

    green_pos_temp=[]

    green_pos_temp.append(random.randrange(1280))

    green_pos_temp.append(random.randrange(720))

    green_pos.append(green_pos_temp)

st="False"

my_font = pygame.font.SysFont('Comic Sans MS', 30)

 

#Posición original de los cuadros

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

malo1_pos=pygame.Vector2(screen.get_width() / 4, screen.get_height() /2)

malo2_pos=pygame.Vector2(3*screen.get_width() / 4, screen.get_height() /2)

malo3_pos=pygame.Vector2(screen.get_width() / 2, screen.get_height() /4)

malo4_pos=pygame.Vector2(screen.get_width() / 2, 3*screen.get_height() /4)

 

#Graficar botón de cerrado

close_button = pygame.Rect(1170, 10, 100, 40)

 

while running:

    #Checar eventos

    #Cerrar si se le pica a la 'x' o al botón de cerrar

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if close_button.collidepoint(event.pos):

                running = False

 

    #Llenar la pantalla de blanco y borrar todo lo anterior

    screen.fill("white")

    pygame.draw.rect(screen, (255, 0, 0), close_button)

    text_surface_c = my_font.render("Cerrar", st, (255, 255, 255))

    screen.blit(text_surface_c, (1170, 10))

 

    #Crear los 5 personajes

    player=Rect(player_pos.x, player_pos.y, tam_player, tam_player)

    malo1=Rect(malo1_pos.x, malo1_pos.y, tam_rect, tam_rect)

    malo2=Rect(malo2_pos.x, malo2_pos.y, tam_rect, tam_rect)

    malo3=Rect(malo3_pos.x, malo3_pos.y, tam_rect, tam_rect)

    malo4=Rect(malo4_pos.x, malo4_pos.y, tam_rect, tam_rect)

 

    #Graficar todos los puntos, aumentar los puntos y tamaño con la respectiva colisión

    for i in range(15):

        amarillo=Rect(amarillo_pos[i][0], amarillo_pos[i][1], tam_puntos, tam_puntos)

        pygame.draw.rect(screen, 'yellow', amarillo)

        if pygame.Rect.colliderect(player,amarillo):

            amarillo_pos[i][0]=random.randrange(1280)

            amarillo_pos[i][1]=random.randrange(720)

            puntos+=5

            tam_player+=0.5

    for i in range(10):

        morado=Rect(morado_pos[i][0], morado_pos[i][1], tam_puntos, tam_puntos)

        pygame.draw.rect(screen, 'purple', morado)

        if pygame.Rect.colliderect(player,morado):

            morado_pos[i][0]=random.randrange(1280)

            morado_pos[i][1]=random.randrange(720)

            puntos+=10

            tam_player+=1

    for i in range(5):

        green=Rect(green_pos[i][0], green_pos[i][1], tam_puntos, tam_puntos)

        pygame.draw.rect(screen, 'green', green)

        if pygame.Rect.colliderect(player,green):

            green_pos[i][0]=random.randrange(1280)

            green_pos[i][1]=random.randrange(720)

            puntos+=15

            tam_player+=1.5

 

    #Graficar los 5 personajes

    pygame.draw.rect(screen, 'blue', player)

    pygame.draw.rect(screen, 'red', malo1)

    pygame.draw.rect(screen, 'red', malo2)

    pygame.draw.rect(screen, 'red', malo3)

    pygame.draw.rect(screen, 'red', malo4)

 

    #Movimiento del personaje WASD y verifica que este dentro de la pantalla

    if collide == False:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and player.top>=0:

            player_pos.y -= 300 * dt

        if keys[pygame.K_s] and player.bottom<=720:

            player_pos.y += 300 * dt

        if keys[pygame.K_a] and player.left>=0:

            player_pos.x -= 300 * dt

        if keys[pygame.K_d] and player.right<=1280:

            player_pos.x += 300 * dt

    if collide==False:

        c+=1

        #Tiempo en segundos

        t=round((c*1.6667/100),0)

        #Contador temporal

        ctemp+=1

        ttemp=round((ctemp*1.6667/100),0)

 

    #Si el objeto se desborda redondear al límite

    if malo1.bottom>720:

        malo1.bottom=720

    if malo1.top<0:

        malo1.top=0

    if malo2.bottom>720:

        malo2.bottom=720

    if malo2.top<0:

        malo2.top=0

    if malo3.right>1280:

        malo3.right=1280

    if malo3.left<0:

        malo3.left=0

    if malo4.right>1280:

        malo4.right=1280

    if malo4.left<0:

        malo4.left=0

   

    #Mantener objetos dentro de la pantalla

    if malo1.top==0 or malo1.bottom==720:

        mov_malo1_y=mov_malo1_y*(-1)

        malo1_pos.y+=mov_malo1_y

    if malo2.top==0 or malo2.bottom==720:

        mov_malo2_y=mov_malo2_y*(-1)

        malo2_pos.y+=mov_malo2_y

    if malo3.right==1280 or malo3.left==0:

        mov_malo3_x=mov_malo3_x*(-1)

        malo3_pos.x+=mov_malo3_x

    if malo4.right==1280 or malo4.left==0:

        mov_malo4_x=mov_malo4_x*(-1)

        malo4_pos.x+=mov_malo4_x

 

    malo1_pos.y+=mov_malo1_y

    malo2_pos.y+=mov_malo2_y

    malo3_pos.x+=mov_malo3_x

    malo4_pos.x+=mov_malo4_x

   

    #Colisión jugador con cuadros rojos

    if pygame.Rect.colliderect(player,malo1) or pygame.Rect.colliderect(player,malo2) or pygame.Rect.colliderect(player,malo3) or pygame.Rect.colliderect(player,malo4):

        collide=True

 

    #Acelerar objetos malos cada 5 segundos

    if ttemp==4 and collide==False:

        tam_rect+=1.5

        mov_malo3_x*=1.1

        mov_malo4_x*=1.1

        mov_malo1_y*=1.1

        mov_malo2_y*=1.1

        ctemp=0

 

    #Si hay choque se frena todo

    if collide:

        mov_malo3_x=0

        mov_malo4_x=0

        mov_malo1_y=0

        mov_malo2_y=0

    pygame.font.init() # Abrir texto
    text_surface = my_font.render("Maurick Sáinz", False, (0, 0, 0))
    screen.blit(text_surface, (0,0))
    text_surface2 = my_font.render(f'Tiempo: {str(t)} segs', False, (0, 0, 0))
    screen.blit(text_surface2, (0,40))
    text_surface3 = my_font.render(f'Puntos: {puntos}', False, (0, 0, 0))
    screen.blit(text_surface3, (0,80))
    #Activar el display
    pygame.display.flip()
    #Limitar FPS a 60
    #dt es delta tiempo en segundos desde el útimo frame
    dt = clock.tick(60) / 1000

pygame.quit()