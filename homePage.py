import numpy as np
import pygame
import sys
import math
import random
import asyncio
import subprocess
 
# Set up Pygame
pygame.init()
 
# Set up the screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")
 
# Set up fonts
font = pygame.font.Font(None, 36)
 
# Set up buttons
button_width = 175
button_height = 50
button_spacing = 5  
 
button_color = (0, 100, 255)
button_hover_color = (0, 200, 0)
 
play_button = pygame.Rect(
    screen_width // 2 - button_width // 2,
    screen_height // 3,
    button_width,
    button_height,
    border_radius=10  # Set border radius for rounded corners
)
 
quit_button = pygame.Rect(
    screen_width // 2 - button_width // 2,
    screen_height // 3 + button_height + button_spacing,
    button_width,
    button_height,
    border_radius=10  # Set border radius for rounded corners
)

instructions_button = pygame.Rect(
    screen_width // 2 - button_width // 2,
    screen_height // 3 + 2 * (button_height + button_spacing),
    button_width,
    button_height,
    border_radius=10  # Set border radius for rounded corners
)
 
# Define game states
HOME_PAGE = 0
 
 
# Initial game state
current_game_state = HOME_PAGE
 
 
# Add a background image
background_image = pygame.image.load("mazePic.jpeg")  # Replace "background.jpg" with your image file
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
 
 
while True:  # Outer loop for restarting the game
 
    while True:  # Inner loop for each game session
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_game_state == HOME_PAGE:
                    # Check if multiplayer button is clicked on the home page
                    if play_button.collidepoint(event.pos):
                        print("Play button clicked")
                        # Use subprocess to run twoplayer.py
                        subprocess.run(["python", "maze.py"])
                        #pygame.quit()
                        #subprocess.run(["python", "homePage.py"])
 
                    # Check if quit button is clicked on the home page
                    elif quit_button.collidepoint(event.pos):
                        if quit_button.collidepoint(event.pos):
                            print("Quit button clicked")
                            pygame.quit()
                            sys.exit()
                            

                    # Check if instructions button is clicked on the home page
                    elif instructions_button.collidepoint(event.pos):
                        print("Instructions button clicked")
                        # Display instructions page or perform any other action
                        subprocess.run(["python", "instructions.py"])


 
        if current_game_state == HOME_PAGE:
            screen.blit(background_image, (0, 0))
            # Draw welcome message
            welcome_text = font.render("Welcome to the Maze Game!", True, (0, 0, 0))
            screen.blit(welcome_text, (screen_width // 2 - welcome_text.get_width() // 2, screen_height // 5))
  
            # Draw the play again button
            pygame.draw.rect(screen, (0, 0, 0), play_button)  # Black background
            play_text = font.render("Play", True, (255, 255, 255))  # White text
            text_rect = play_text.get_rect(center=play_button.center)
            screen.blit(play_text, text_rect.topleft)
 
            # Draw the quit button
            pygame.draw.rect(screen, (0, 0, 0), quit_button)  # Black background
            quit_text = font.render("Quit", True, (255, 255, 255))  # White text
            text_rect = quit_text.get_rect(center=quit_button.center)
            screen.blit(quit_text, text_rect.topleft)
            
            # Draw the instructions button
            pygame.draw.rect(screen, (0, 0, 0), instructions_button)  # Black background
            instructions_text = font.render("Instructions", True, (255, 255, 255))  # White text
            text_rect = instructions_text.get_rect(center=instructions_button.center)
            screen.blit(instructions_text, text_rect.topleft)
 
        pygame.display.flip()
        pygame.time.Clock().tick(30)
 
        # Check if the user wants to exit the game session
        if current_game_state == HOME_PAGE:
            break  # Break out of the inner loop and return to the outer loop
 
    # After exiting the game session, reset the game state to HOME_PAGE
    current_game_state = HOME_PAGE

 
 
## pip install pygame
## pip install numpy
 
 

## add a button that opens up a page with instructions
## add comments and do the report

## have user input how happy they are on a scale of 1-10 and give them a number of boxes to collect in order to win the game (cant finish until u collect them all)
## happiness score depending on how many boxes they pick up

