import pygame

pygame.init()

screen = pygame.display.set_mode((640, 240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 0))
            pygame.display.update()
        elif event.type == pygame.CONTROLLER_BUTTON_A:
            screen.fill((255, 0, 0))
            pygame.display.update()

pygame.quit()