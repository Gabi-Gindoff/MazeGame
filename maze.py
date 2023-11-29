from ast import Try
import pygame
import sys
import random
from queue import Queue
import time

# Constants
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

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")

# Font setup
font = pygame.font.Font(None, 25)

# Maze generation with more dead ends
def generate_maze():
    while True:
        maze = [[random.choices([0, 1], weights=[0.7, 0.3])[0] for _ in range(COLS)] for _ in range(ROWS)]
        maze[0][0] = maze[ROWS - 1][COLS - 1] = 0  # Start and end points are open

        # Add packages (yellow squares)
        for _ in range(11):  # You can adjust the number of packages
            package_row, package_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
            maze[package_row][package_col] = YELLOW

        path = bfs(maze)
        if path:
            return maze, path

# BFS algorithm to find the path
def bfs(maze):
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    queue = Queue()
    queue.put((0, 0, []))  # (row, col, path)

    while not queue.empty():
        row, col, path = queue.get()
        if row == ROWS - 1 and col == COLS - 1:
            return path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if (
                0 <= new_row < ROWS
                and 0 <= new_col < COLS
                and not visited[new_row][new_col]
                and maze[new_row][new_col] == 0
            ):
                queue.put((new_row, new_col, path + [(row, col)]))
                visited[new_row][new_col] = True

    return None  # No path found

# Draw the maze
def draw_maze(maze):
    for row in range(ROWS):
        for col in range(COLS):
            color = maze[row][col]
            if color == YELLOW:
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                color = WHITE if maze[row][col] == 0 else BLACK
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw the path
def draw_path(path):
    if path is not None:
        for row, col in path:
            pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Game loop
maze, ai_path = generate_maze()
user_row, user_col = 0, 0
user_moved = False  # Flag to check if the user moved
ai_path_revealed = False  # Flag to check if the AI path is revealed
victory = False  # Flag to check if the user reached the red square
last_key_press_time = time.time()





# Jokes and answers
jokes_and_answers = [
    ("Why did the computer keep its drink on the windowsill?", "Because it wanted a cold beverage!"),
    ("How do you comfort a JavaScript bug?", "You console it!"),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
    ("What do you call a group of musical hackers?", "A cyberband!"),
    ("Why do programmers always mix up Christmas and Halloween?", "Because Oct 31 == Dec 25!"),
    ("Why did the computer take up gardening?", "It wanted to improve its root access!"),
    ("How do you organize a space party?", "You planet!"),
    ("What's a computer's favorite snack?", "Microchips!"),
    ("Why did the computer go to therapy?", "It had too many bytes of emotional baggage!"),
    ("What's an astronaut's favorite computer key?", "The space bar!"),
    ("Why did the computer cross the road?", "To get to the other website!"),
    ("What do you get when you cross a computer and a lifeguard?", "A screen saver!"),
    ("Why was the computer cold?", "It left its Windows open!"),
    ("How do you catch a computer mouse?", "Use a webcam!"),
    ("Why did the computer go to art school?", "It wanted to improve its pixels!"),
    ("What's a computer's least favorite food?", "Spam!"),
    ("How do you fix a broken website?", "With a web patch!"),
    ("Why did the computer apply for a job?", "It wanted to be a website developer!"),
    ("What's a computer's favorite dance?", "The algorithm!"),
    ("Why did the computer go on a diet?", "It had too many cookies!"),
    ("What's a computer's favorite horror movie?", "The Ctrl-Alt-Delete of the Dead!"),
    ("How many programmers does it take to change a light bulb?", "None, that's a hardware problem!"),
    ("Why was the computer cold?", "It left its Windows open!"),
    ("What's a computer's favorite beat?", "An algo-rhythm!"),
    ("Why did the computer go to therapy?", "It had too many bytes of emotional baggage!"),
    ("What do you call a computer that sings?", "A Dell!"),
    ("How does a computer take its coffee?", "Java!"),
    ("What's a computer's favorite snack?", "Cookies!"),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
    ("How do you comfort a JavaScript bug?", "You console it!"),
    ("What do you call a computer that can sing?", "Adele!"),
    ("Why did the computer keep its cool during the meeting?", "It had a good fan base!"),
    ("How does a computer get drunk?", "It takes too many screenshots!"),
    ("What's a computer's favorite type of exercise?", "Disk-ercise!"),
    ("Why was the computer cold in the winter?", "It left its Windows open!"),
    ("What's a computer's favorite subject in school?", "Algorithms!"),
    ("Why do programmers prefer dark chocolate?", "Because it's bitter, like their code reviews!"),
    ("What do you call a computer superhero?", "A screen saver!"),
    ("Why did the computer go to therapy?", "It had too many bytes of emotional baggage!"),
    ("What did one computer say to another in a bar?", "0101011101100001011011000110110001101111!"),
    ("How do you know your computer is a music lover?", "It has a good byte!"),
    ("What did the computer say when it met its soulmate?", "You've got mail!"),
    ("Why did the computer go on a diet?", "It had too many cookies!"),
    ("What's a computer's favorite snack?", "Microchips!"),
    ("How do you catch a computer mouse?", "Use a webcam!"),
    ("What do computers do when they're cold?", "They boot up a Windows!"),
    ("Why did the computer take up gardening?", "It wanted to improve its root access!"),
    ("What's a computer virus's favorite game?", "Hide and seek!"),
    ("How do you organize a space party?", "You planet!"),
    ("What's a computer's favorite beat?", "An algo-rhythm!"),
    ("Why did the computer apply for a job?", "It wanted to be a website developer!"),
    ("What's a computer's favorite dance?", "The algorithm!"),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
    ("How do you comfort a JavaScript bug?", "You console it!"),
    ("What do you call a computer that can sing?", "Adele!"),
    ("What's the difference between a computer and a cat?", "You only have to tell the computer once!"),
    ("Why did the computer get in trouble with the law?", "It had too many bits!"),
    ("What do you call a computer with a messy desk?", "Cluttered memory!"),
    ("Why was the computer cold?", "It left its Windows open!"),
    ("What did the computer say at the job interview?", "I'm good at processing information, not emotions!"),
    ("How do you keep a computer from getting sick?", "Run an anti-virus program!"),
]


            
running = True  # Variable to control the main loop

while running:

    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not ai_path_revealed:
                # Click to reveal AI path
                ai_path_revealed = True
            elif event.type == pygame.MOUSEBUTTONDOWN and ai_path_revealed:
                # Click to hide AI path
                ai_path_revealed = False

        keys = pygame.key.get_pressed()
        current_time = time.time()

        # Add a delay between key presses to limit movement speed
        if current_time - last_key_press_time > 0.1 and not victory:
            if keys[pygame.K_UP] and user_row > 0 and maze[user_row - 1][user_col] in [0, YELLOW]:
                user_row -= 1
                user_moved = True
            elif keys[pygame.K_DOWN] and user_row < ROWS - 1 and maze[user_row + 1][user_col] in [0, YELLOW]:
                user_row += 1
                user_moved = True
            elif keys[pygame.K_LEFT] and user_col > 0 and maze[user_row][user_col - 1] in [0, YELLOW]:
                user_col -= 1
                user_moved = True
            elif keys[pygame.K_RIGHT] and user_col < COLS - 1 and maze[user_row][user_col + 1] in [0, YELLOW]:
                user_col += 1
                user_moved = True

            last_key_press_time = current_time

            # Check if the user reached the red square
            if user_row == ROWS - 1 and user_col == COLS - 1:
                victory = True

            # Check if the user reached a package (yellow square)
            if maze[user_row][user_col] == YELLOW:
                # Display a joke and answer on the screen
                joke, answer = random.choice(jokes_and_answers)
                joke_text = font.render(joke, True, RED)
                answer_text = font.render("Answer: " + answer, True, RED)

                # Set the display timers for joke and answer
                joke_display_timer = current_time + 2000  # 2 seconds
                answer_display_timer = joke_display_timer + 2000  # 2 seconds

                # Create a background rectangle behind the joke text
                background_rect = pygame.Rect(
                    WIDTH // 2 - joke_text.get_width() // 2 - 10,
                    HEIGHT // 2 - joke_text.get_height() // 2 - 10,
                    joke_text.get_width() + 20,
                    joke_text.get_height() + 20
                )
                pygame.draw.rect(screen, WHITE, background_rect)

                # Draw the joke text on top of the background rectangle
                joke_text_position = (WIDTH // 2 - joke_text.get_width() // 2, HEIGHT // 2 - joke_text.get_height() // 2)
                screen.blit(joke_text, joke_text_position)

                pygame.display.flip()  # Update the display to show the joke and background

                # Wait for the remaining time before displaying the answer
                remaining_time = joke_display_timer - current_time
                if remaining_time > 0:
                    pygame.time.wait(int(remaining_time))

                # Create a background rectangle behind the answer text
                answer_background_rect = pygame.Rect(
                    WIDTH // 2 - answer_text.get_width() // 2 - 10,
                    HEIGHT // 2 + joke_text.get_height() // 2 + 20,  # Move answer text farther down
                    answer_text.get_width() + 20,
                    answer_text.get_height() + 20
                )
                pygame.draw.rect(screen, WHITE, answer_background_rect)

                # Draw the answer text on top of the background rectangle
                answer_text_position = (WIDTH // 2 - answer_text.get_width() // 2, HEIGHT // 2 + joke_text.get_height() // 2 + 20)
                screen.blit(answer_text, answer_text_position)

                pygame.display.flip()  # Update the display to show the answer and background

                # Wait for the remaining time before removing the package from the maze
                remaining_time = answer_display_timer + 2000 - current_time
                if remaining_time > 0:
                    pygame.time.wait(int(remaining_time))

                # Remove the package from the maze
                maze[user_row][user_col] = 0

        screen.fill(WHITE)
        draw_maze(maze)

        # Draw the starting and end points
        pygame.draw.rect(screen, BLUE, (user_col * CELL_SIZE, user_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, ((COLS - 1) * CELL_SIZE, (ROWS - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if ai_path_revealed and (user_moved or current_time - last_key_press_time <= 0.2):
            draw_path(ai_path)

        # Display victory message
        if victory:
            font = pygame.font.Font(None, 35)
            message = "Congratulations! You reached the end!"
    
            # Create a background rectangle behind the victory message
            text_width, text_height = font.size(message)
            background_rect = pygame.Rect(
                WIDTH // 2 - text_width // 2 - 10,
                HEIGHT // 2 - text_height // 2 - 10,
                text_width + 20,
                text_height + 20
            )
            pygame.draw.rect(screen, WHITE, background_rect)

            # Draw the victory message text on top of the background rectangle
            text = font.render(message, True, RED)
            screen.blit(text, (WIDTH // 2 - text_width // 2, HEIGHT // 2 - text_height // 2))

            pygame.display.flip()

            pygame.time.wait(2000)
            running = False

        pygame.display.flip()

    except pygame.error as e:
        # Handle the "video system not initialized" error
        pass

pygame.quit()
sys.exit()
