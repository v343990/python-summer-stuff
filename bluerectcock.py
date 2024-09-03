import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch Falling Boy")
clock = pygame.time.Clock()  # Create a clock object

randomColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

renderRect = True
renderNewRect = False
# Main loop
gameLive = True
while gameLive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLive = False

    # just to give it nice juicy background
    window.fill((255,255,255))
    # rectangle/square can be called by name xo
    
    if renderRect:
        rectangle = pygame.draw.rect(window, (200, 0, 0), (300, 200, 200, 200))

    if renderNewRect:
        pygame.draw.rect(window, randomColour, (300, 200, 200, 200))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if rectangle.collidepoint(event.pos):
            randomColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            renderRect = False
            renderNewRect = True

# All elements in here
# Everything updated    
    pygame.display.update()
    clock.tick(60)  # No more than 60 frames per second

# Quit PyGame
pygame.quit()
