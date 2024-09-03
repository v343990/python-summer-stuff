import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move the Red Rectangle")
clock = pygame.time.Clock()  # Create a clock object


# Surfaces
score = 0
character_surf = pygame.image.load('hammad.jpeg')
enemy_surf = pygame.image.load('enemyhammad.jpg')
score_text = pygame.font.Font('poxel-font.ttf', 35)
score_surf = score_text.render(str(score),False,(128,128,128))
score_rect = score_surf.get_rect(center = (640, 120))

# Get rects from surfaces
character_rect = character_surf.get_rect()
enemy_rect = enemy_surf.get_rect(topleft=(1000, 500))  # Set initial position

# Set initial positions for the character
rect_width, rect_height = character_rect.width, character_rect.height
rect_x = 30
rect_y = 30
rect_speed = 5
renderEnemy = True


# Main loop
gameLive = True
while gameLive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLive = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the rectangle
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Keep sprite in window
    if rect_x < 0:
        rect_x = 0
    if rect_x + rect_width > width:
        rect_x = width - rect_width
    if rect_y < 0:
        rect_y = 0
    if rect_y + rect_height > height:
        rect_y = height - rect_height

    window.fill((0, 0, 0))  # stops the square from staying on screen after moving
                            # Doesn't look glitchy

    # Collision check UwU x
    if character_rect.colliderect(enemy_rect):
        score += 1
        score_surf = score_text.render(str(score), False, (128, 128, 128))  # updates the score
        enemy_rect.x = random.randint(0,1280)
        enemy_rect.y = random.randint(0,720)

        # makes sure it doesn't half off the screen
        if enemy_rect.x + enemy_rect.width > width:
            enemy_rect.x = width - enemy_rect.width
        if enemy_rect.x < 0:
            enemy_rect.x = 0
        if enemy_rect.y < 0:
            enemy_rect.y = 0
        if enemy_rect.y + enemy_rect.height > height:
            enemy_rect.y = height - enemy_rect.height
        

    # Renders enemy spritey tighty if no collide
    if renderEnemy:
        window.blit(enemy_surf, enemy_rect)

    
    # Render main spritey tighty
    character_rect.topleft = (rect_x, rect_y)
    window.blit(character_surf, character_rect)
    window.blit(score_surf, score_rect)

# All elements in here
# Everything updated    
    pygame.display.update()
    clock.tick(60)  # No more than 60 frames per second

# Quit PyGame
pygame.quit()
