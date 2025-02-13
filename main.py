import pygame 
import pygame_gui
import sys
import os
import random
import math
import time
import threading

pygame.init()

# Set up screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
inner_screen_width = screen_width*0.75
inner_screen_height = screen_height*0.75
screen.fill(white)

DEFAULT_IMAGE_SIZE = x, y = 100, 100

images = []

for root, dirs, files in os.walk('images/'):
    print(files)

#image_2 = pygame.image.load('images/')
#image_3 = pygame.image.load('images/')
#sound_1 = pygame.mixer.Sound('sounds/')
#sound_2 = pygame.mixer.Sound('sounds/')

#screen.blit(image_2, (50, 40))

def reset_game():
    global circle_Y_positions, increment, points
    circle_Y_positions = [base_posY + (500 * i) for i in range(len(circle_positions))]
    increment = 0.3
    points = 0


# Initial settings
running = True
base_posY = -2600  # Initial Y position for all circles
increment = 0.3  # Speed increase over time
points = 0  # Player points

# Define circles with separate Y-positions
circle_positions = [220 * (i + 1) for i in range(6)]
circle_Y_positions = [base_posY + (500 * i) for i in range(len(circle_positions))]

def process_click(index):
    reset_circle_pos()
    print(f'Circle at {circle_positions[index]} has been clicked')
    increment += 0.001 
    points += 1

def reset_circle_pos(index):
    global increment, points
    circle_Y_positions[index] = -200  # Reset only the clicked circle's Y position
    if points <= 0:
        time.sleep(1)
        reset_game()

def penalty():
    global points
    points -= 1
    if points <= 0:
        time.sleep(1)
        reset_game()

    
def countdown(t): 
    while True:
        while t > 0: 
            time.sleep(1) 
            t -= 1        
        reset_game()


timerThread = threading.Thread(target=lambda: countdown(60))
timerThread.start()

while running:
    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Create counter screen
    mainFont = pygame.font.SysFont("arial", 24)
    
    # Clear screen
    screen.fill([255, 255, 255])

    # Move all circles down
    for i in range(len(circle_Y_positions)):
        circle_Y_positions[i] += increment
        if circle_Y_positions[i] > screen_height:  # Check if circle reaches the bottom
            reset_circle_pos(i)  # Reset the circle when it reaches the bottom


    # Draw circles
    for i, (posX, posY) in enumerate(zip(circle_positions, circle_Y_positions)):
        pygame.draw.circle(screen, [0, 0, 0], (posX, posY), radius=50)

    pointsText = mainFont.render(f"Points: {points}", False, (0,0,0))
    screen.blit(pointsText, (100, 100))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = False
            for i, (posX, posY) in enumerate(zip(circle_positions, circle_Y_positions)):
                distance = math.sqrt((x - posX) ** 2 + (y - posY) ** 2)
                if distance < 50:  # If click is inside a circle
                    process_click(i)
                    clicked = True
                    break
            if not clicked:
                penalty()

    # Update display
    pygame.display.update()

pygame.quit()