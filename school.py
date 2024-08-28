import pygame

screen = pygame.display.set_mode((640,280))
backgrd = 'GRAY'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                backgrd = 'RED'
            if event.key == pygame.K_RIGHT:
                backgrd = 'ORANGE'
            if event.key == pygame.K_UP:
                backgrd = 'YELLOW'
            if event.key == pygame.K_DOWN:
                backgrd = 'Blue'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                backgrd = 'GRAY'
    screen.fill(backgrd)
    pygame.display.update()
pygame.quit()
