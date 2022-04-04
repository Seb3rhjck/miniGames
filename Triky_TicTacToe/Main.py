from operator import mod
from tkinter import Grid
import  pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Triky")

line_width = 6
marcas = []
clicked = False
pos = []
jugador = 1
ganador = 0
fin_del_juego = False

amarillo = (250, 253, 15)
rojo = (219, 0, 0)
negro = (0, 0, 0)

font = pygame.font.SysFont(None, 40)

rectangulo_denuevo = Rect(screen_width // 2 - 80, screen_height // 2, 190, 50)

for x in range(3):
    row = [0] * 3
    marcas.append(row)

def dibujar_reja():
    colorFondo = (0, 0, 153)
    grid = (250, 250, 250)
    screen.fill(colorFondo)
    for x in range (1, 3):
        pygame.draw.line(screen, grid, (0, x *100), (screen_width, x *100), line_width)
        pygame.draw.line(screen, grid, (x *100, 0), ( x *100, screen_height), line_width)

def dibujar_marca():
    x_pos = 0
    for x in marcas:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, amarillo, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, amarillo, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, rojo, (x_pos * 100 + 50,  y_pos * 100+ 50), 38, line_width)
            y_pos += 1
        x_pos += 1

def confirmar_ganador():
    
    global ganador
    global fin_del_juego
    
    x_pos = 0
    for x in marcas:
        #columnas
        if sum(x) == 3:
            ganador = 1
            fin_del_juego = True
        if sum(x) == -3:
            ganador = 2
            fin_del_juego = True
        
        #filas
        if marcas[0][x_pos] + marcas[1][x_pos] + marcas[2][x_pos] == 3:
            ganador = 1
            fin_del_juego = True
        if marcas[0][x_pos] + marcas[1][x_pos] + marcas[2][x_pos] == -3:
            ganador = 2
            fin_del_juego = True
        x_pos += 1
        
    #cruzado
    if marcas[0][0] + marcas[1][1] + marcas[2][2] == 3 or marcas[2][0] + marcas[1][1] + marcas[0][2] == 3:
        ganador = 1
        fin_del_juego = True
    if marcas[0][0] + marcas[1][1] + marcas[2][2] == -3 or marcas[2][0] + marcas[1][1] + marcas[0][2] == -3:
        ganador = 2
        fin_del_juego = True
        
    #empate
    if fin_del_juego == False:
        empate = True
        for row in marcas:
            for i in row:
                if i == 0:
                    empate = False
        if empate == True:
            fin_del_juego = True
            ganador = 0

def mostrar_ganador(ganador):
    
    if ganador != 0:
        texto_victoria = 'Jugador ' + str(ganador) + ' gano!'
    elif ganador == 0:
        texto_victoria = 'En tablas!'
        
    img_victoria = font.render(texto_victoria, True, negro)
    pygame.draw.rect(screen, amarillo, (screen_width // 2 - 100, screen_height // 2 - 60, 220, 50))
    screen.blit(img_victoria, (screen_width // 2 - 100, screen_height // 2 - 50))
    
    de_nuevo_texto = 'Juego nuevo?'
    de_nuevo_img = font.render(de_nuevo_texto, True, negro)
    pygame.draw.rect(screen, amarillo, rectangulo_denuevo)
    screen.blit(de_nuevo_img, (screen_width // 2 - 80, screen_height // 2 + 10))
    
run = True
while run:
    
    dibujar_reja()
    dibujar_marca()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
        if fin_del_juego == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == clicked  ==False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if marcas[cell_x // 100][cell_y // 100] == 0:
                    marcas[cell_x // 100][cell_y // 100] = jugador    
                    jugador *= -1
                    confirmar_ganador()
    if fin_del_juego == True:
        mostrar_ganador(ganador)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == clicked  ==False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if rectangulo_denuevo.collidepoint(pos):
                marcas = []
                pos = []
                jugador = 1
                ganador = 0
                fin_del_juego = False
                for x in range(3):
                    row = [0] * 3
                    marcas.append(row)

            
    pygame.display.update()
            
pygame.quit()
