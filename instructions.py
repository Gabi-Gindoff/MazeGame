import pygame  # Import Pygame for game development
import sys  # Import sys for system-specific parameters and functions

# Constants for the screen/ display and colors
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE, BLACK, RED, GREEN, BLUE, YELLOW = (
    (255, 255, 255),
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0)
)

# Background image
background_image = pygame.image.load("mazePic.jpeg") 
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Pygame setup
pygame.init() # Initialize pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialize game window
pygame.display.set_caption("Instructions") # Set window caption

# Display background image
screen.blit(background_image, (0, 0))

# Font setup
font = pygame.font.Font(None, 25)

# Instruction text
instructions = [
    "Welcome to the Maze Game!",
    "",
    "Instructions:",
    "1. Use arrow keys to navigate through the maze.",
    "2. Collect yellow squares (packages) for fun jokes.",
    "3. Reach the red square to complete the maze.",
    "4. Have fun and enjoy the game!",
    "",
    "HINT: Press the space bar to reveal the shortest path!",
    " ",
    "Press 'Play' on the home page to start the Maze Game.",
    "Press 'Quit' on the home page to exit the Application."
]

# Display instructions using loop 
for i, line in enumerate(instructions):
    text = font.render(line, True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4 + i * 25))

# Update the pygame display
pygame.display.flip()

# Wait for any key press to exit the instruction screen
waiting_for_key = True
while waiting_for_key:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            waiting_for_key = False

# Quit the application
pygame.quit()
sys.exit()
