import pygame, time, random

snake_speed = 15

# VENTANA
VENTANA_X = 720
VENTANA_Y = 480

# COLORES
negro  = pygame.Color(0, 0, 0)
blanco = pygame.Color(255, 255, 255)
rojo   = pygame.Color(255, 0, 0)
verde  = pygame.Color(0, 255, 0)
azul   = pygame.Color(0, 0, 255)


pygame.init()


pygame.display.set_caption('Juega un rato con Snake')
game_window = pygame.display.set_mode(VENTANA_X, VENTANA_Y)


fps = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]


# FRUTA
fruit_position = [random.randrange(1, (VENTANA_X//10)) * 10,
                  random.randrange(1, (VENTANA_Y//10)) * 10]

fruit_spawn = True
direction = 'RIGHT'
change_to = direction


# PUNTAJE

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Puntuación: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
    

# GAME-OVER

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Tú PUNTAJE ES: ' + str(score), True, rojo)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (VENTANA_X/2, VENTANA_Y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
    

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
        
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (VENTANA_X//10)) * 10,
                          random.randrange(1, (VENTANA_Y//10)) * 10]
    
    fruit_spawn = True
    game_window.fill(negro)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, verde, pygame.Rect(
            pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(game_window, blanco, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    
    # Condición Game Over
    if snake_position[0] < 0 or snake_position[0] > VENTANA_X-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > VENTANA_Y-10:
        game_over()
        
    for block in snake_body[1:]:
        if snake_position[0] ==block[0] and snake_position[1] ==block[1]:
            game_over()
    
    show_score(1, blanco, 'times new roman', 20)
    
    pygame.display.update()
    
    fps.tick(snake_speed)