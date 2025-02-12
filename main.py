import pygame 
import pygame_gui
import sys
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
screen = pygame.display.set_mode((800, 600))
screen_x, screen_y = screen.get_size()
inner_screen_width = screen_x*0.75
inner_screen_height = screen_y*0.75
screen.fill(white)

pygame.display.flip()

DEFAULT_IMAGE_SIZE = x, y = 100, 100

image_1 = pygame.image.load('images/')
image_2 = pygame.image.load('images/')
image_3 = pygame.image.load('images/')
sound_1 = pygame.mixer.Sound('sounds/')
sound_2 = pygame.mixer.Sound('sounds/')

screen.blit(image_1, (50, 40))
pygame.display.flip()

running = True
while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()