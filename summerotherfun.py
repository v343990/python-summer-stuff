import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch Falling Boy")
clock = pygame.time.Clock()  # Create a clock object
point_sound = pygame.mixer.Sound("Fart.mp3")
fail_sound = pygame.mixer.Sound("Bruh.mp3")

# Surfaces
score = 0
best_score = 0
character_surf = pygame.image.load('hammad.jpeg')
score_text = pygame.font.Font('poxel-font.ttf', 35)
bestscore_text = pygame.font.Font('poxel-font.ttf', 25)
score_surf = score_text.render(str(score),False,(128,128,128))
score_rect = score_surf.get_rect(center = (400, 120))
bestscore_surf = bestscore_text.render(f'Best Score: {best_score}',False,(128,128,128))
bestscore_rect = bestscore_surf.get_rect(center = (400, 160))

# Get rects from surfaces
character_rect = character_surf.get_rect()

# Set initial positions for the character
rect_width, rect_height = 60, 15
rect_x = 70
rect_y = 520
enemy_y = 0
enemy_x = 60
rect_speed = 10


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

    # Keep rectangle in window
    if rect_x < 0:
        rect_x = 0
    if rect_x + rect_width > width:
        rect_x = width - rect_width
    if rect_y < 0:
        rect_y = 0

    enemy_y += 7
    window.fill((255,255,255))
    enemy = pygame.draw.rect(window, (200, 0, 0), (enemy_x, enemy_y, 25, 25))
    maincharacter = pygame.draw.rect(window, (75,75,75), (rect_x, rect_y, rect_width, rect_height))
    window.blit(score_surf, score_rect)
    window.blit(bestscore_surf, bestscore_rect)

    if enemy.colliderect(maincharacter):
        score += 1
        pygame.mixer.Sound.play(point_sound)
        score_surf = score_text.render(str(score), False, (128, 128, 128))
        enemy_x = random.randint(60, 740)
        enemy_y = 0
    if enemy_y > 600:
        pygame.mixer.Sound.play(fail_sound)
        enemy_x = random.randint(60, 740)
        enemy_y = 0
        if score > best_score:
            best_score = score
        else:
            best_score = best_score
        score = 0
        score_surf = score_text.render(str(score), False, (128, 128, 128))
        bestscore_surf = bestscore_text.render(f'Best Score: {best_score}',False,(128,128,128))



# All elements in here
# Everything updated    
    pygame.display.update()
    clock.tick(60)  # No more than 60 frames per second

# Quit PyGame
pygame.quit()
