# Maze Game
By: Adam Christopher & Gabriella Gindoff

## Project Goals

The primary goal of the Maze Game project is to create an interactive and enjoyable gaming experience for users. Through maze navigation, package collection, and reaching the game's endpoint, users are immersed in a dynamic and challenging environment. A distinctive feature is the incorporation of packages, each revealing lighthearted jokes upon collection, with the aim of enhancing user happiness. This unique approach seeks to create a positive and uplifting atmosphere within the game, contributing to the creation of a safe space for players.

Furthermore, the project aspires to showcase the practical application of techniques and concepts learned in class throughout the software development process. Drawing on fundamental programming and software design principles, Python serves as the primary language, while the Pygame library facilitates graphical user interface development. The project employs data structures, such as queues for Breadth-First Search, demonstrating the application of class-learned algorithms. The incorporation of interactive buttons on the home page reflects the utilization of event-driven programming concepts. Emphasis is placed on user experience design, integrating principles learned in class for intuitive and visually appealing interfaces.

In summary, the Maze Game project not only aims to provide entertainment but also serves as a tangible application of class-learned techniques and concepts in software development. Through this integration, the project seeks to reinforce programming principles and deliver an engaging and uplifting user experience.




## Significance of the Project

The Maze Game holds substantial significance within the context of Safe Space as it goes beyond being a mere source of entertainment. By integrating features designed to elevate user happiness, the project aligns with the core values of creating a safe and positive environment for users. In addition to providing a lighthearted activity, the game serves as a tool for relaxation and stress relief, fostering mental well-being.

The incorporation of jokes within the game becomes a powerful mechanism to infuse humor into the user experience. Humor has proven therapeutic effects, offering a natural and accessible means to alleviate stress and elevate mood. Through the delivery of jokes upon collecting packages, the Maze Game becomes more than just a maze-navigating adventure; it transforms into a source of joy and amusement, creating a dynamic and emotionally uplifting interaction for the players.

Furthermore, the project's dual focus on user happiness and the practical application of class-learned techniques enhances its significance. By providing a tangible demonstration of programming and software development concepts, the Maze Game becomes not only a recreational activity but also an educational tool. Users engage with a product that not only entertains but also subtly educates, making it a valuable and holistic addition to the Safe Space platform.

In summary, the Maze Game contributes significantly to Safe Space by combining entertainment with mental well-being, offering users a delightful and educational experience. The integration of humor and the practical application of programming concepts enrich the overall impact of the project, aligning it with the goals of creating a positive and supportive space for users.




## Installation and Usage Instructions
1. **Installation:**
   - The entire application runs in Visual Studio / Visual Studio Code
   - The application will **NOT** run in Google Codespaces or GitHub Codespaces due to pygame pop-ups not functioning correctly.
   - Install the required dependencies by running:
     ```
     pip install -r mazeRequirements.txt
     ```

3. **Usage:**
   - Run the `homePage.py` script to launch the starting menu for the game
      ```
      python homePage.py
      ```
   - For instructions on how to play, click on the "instructions" button after launching the menu
   - Press the "Play" button to start the game.
   - Collect yellow squares (packages) for jokes and navigate to the red square to complete the maze.
   - Press the space bar to reveal the shortest path.
   - Pressing "Quit" or reaching the red square will exit the application.

## Code Structure
The project consists of three main Python scripts:
1. **homePage.py:** Manages the game's home page, including buttons for playing, quitting, and accessing instructions.
2. **maze.py:** Implements the maze generation, BFS pathfinding algorithm, and game logic for the user's movement and interaction with packages.
3. **instructions.py:** Displays instructions on how to play the game.

The code is structured with clear sections for Pygame setup, constants, maze generation, user input handling, and game loop. Each script serves a specific purpose, contributing to the overall functionality of the Maze Game.

## List of Functionalities and Test Results
### Functionalities:
- **Home Page:**
  - Play Button: Initiates the game session.
  - Quit Button: Exits the application.
  - Instructions Button: Displays instructions.

- **Maze Game:**
  - Maze Generation: Randomly generates a maze with packages.
  - User Movement: Allows the user to navigate the maze using arrow keys.
  - Package Collection: Triggers jokes upon collecting yellow squares.
  - Shortest Path: Pressing the space bar reveals the shortest path.
  - Victory: Displays a congratulatory message upon reaching the end.

- **Instructions Page:**
  - Displays game instructions.
  - Exit on any key press.

### Test Results:
- The game has been tested for functionality, including user movement, package collection, victory conditions, and pathfinding.
- The instructions page has been tested for clarity and correctness.

## Discussion and Conclusions
### Project Issues and Limitations:
- The game currently lacks a scoring system or a mechanism to track user progress beyond package collection.
- The maze generation algorithm could be further optimized for more interesting and challenging mazes.

### Application of Course Learnings:
- The project incorporates principles of game development, including user input handling, maze generation, and pathfinding algorithms.
- Python, Pygame, and basic software design concepts were applied to create a functional and entertaining game.

Overall, the Maze Game provides a fun and interactive experience for users, contributing to Safe Space's mission of promoting mental well-being through engaging activities. The project also serves as a practical application of programming and game development concepts learned throughout the course.
