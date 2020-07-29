import pygame
root = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pygame Base Settings made easy")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()