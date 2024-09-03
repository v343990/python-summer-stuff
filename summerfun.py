import pygame

pygame.init()
screen_width = 1280 # set screen height
screen_height = 600 # and width
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Summer Fun") # sets the display caption
icon = pygame.image.load('hammad.jpeg') # loads the icon
pygame.display.set_icon(icon) # sets icon
clock = pygame.time.Clock() # Create a clock object
blue = (0, 0, 255)
green = (0, 255, 0)

gamelive = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # When we call pygame.quit
            pygame.quit() # Quit the screen
            exit()
   
    pygame.draw.ellipse(screen, blue, pygame.Rect(640, 150, 50, 50))
    pygame.draw.rect(screen, green, pygame.Rect(510, 200, 300, 250))
    pygame.draw.rect(screen, blue, pygame.Rect(410, 300, 100, 50))
    pygame.draw.rect(screen, blue, pygame.Rect(810, 300, 100, 50))
    pygame.draw.rect(screen, blue, pygame.Rect(540, 450, 50, 80))
    pygame.draw.rect(screen, blue, pygame.Rect(720, 450, 50, 80))
    pygame.draw.polygon(screen, blue, [[520, 300], [800, 300], [660, 400]])
    pygame.display.flip()