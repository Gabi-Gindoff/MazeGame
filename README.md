# Maze Game
By: Adam Christopher & Gabriella Gindoff


# Table of Contents

1. [Project Goals](https://github.com/Gabi-Gindoff/MazeGame/blob/main/README.md#project-goals)
2. [Significance of the Project](https://github.com/Gabi-Gindoff/MazeGame/blob/main/README.md#significance-of-the-project)
3. [Installation and Usage Instructions](https://github.com/Gabi-Gindoff/MazeGame/blob/main/README.md#installation-and-usage-instructions)
4. [Code Structure](https://github.com/Gabi-Gindoff/MazeGame/blob/main/README.md#code-structure)
5. [List of Functionalities and Test Results](https://github.com/Gabi-Gindoff/MazeGame/blob/main/README.md#list-of-functionalities-and-test-results)
6. [Discussion and Conclusions](https://github.com/Gabi-Gindoff/MazeGame/blob/main/README.md#discussion-and-conclusions)


## Project Goals

The primary goal of the Maze Game project is to create an interactive and enjoyable gaming experience for users. Through maze navigation, package collection with jokes, and reaching the game's endpoint, users are immersed in a dynamic and challenging environment. A distinctive feature is the incorporation of packages, each revealing lighthearted jokes upon collection, with the aim of enhancing user happiness. This unique approach seeks to create a positive and uplifting atmosphere within the game, contributing to the creation of a safe space for players.

Furthermore, the project aims to showcase the practical application of techniques and concepts learned in class. Drawing on fundamental programming, algorithms and software design principles, Python serves as the primary language, while the Pygame library facilitates graphical user interface development. The project employs data structures, such as queues for Breadth-First Search, demonstrating the application of class-learned algorithms. 

In summary, the Maze Game project not only aims to provide entertainment but also serves as a tangible application of class-learned techniques and concepts in software development and algorithm analysis. Through this integration, the project seeks to reinforce programming principles and deliver an engaging and uplifting user experience.




## Significance of the Project

The Maze Game holds substantial significance within the context of Safe Space as it goes beyond being just a source of entertainment. By integrating features designed to elevate user happiness, the project aligns with the core values of creating a safe and positive environment for users. In addition to providing a lighthearted activity, the game serves as a tool for relaxation and stress relief, fostering mental well-being.

The incorporation of jokes within the game becomes a powerful mechanism to infuse humor into the user experience. Humor has proven therapeutic effects, offering a natural and accessible means to alleviate stress and elevate mood. Through the delivery of jokes upon collecting packages, the Maze Game becomes more than just a maze-navigating adventure; it transforms into a source of joy and amusement, creating a dynamic and emotionally uplifting interaction for the players.

Furthermore, the project's dual focus on user happiness and the practical application of class-learned techniques enhances its significance. By providing a tangible demonstration of programming, algorithms, and software development concepts, the Maze Game becomes not only a recreational activity but also an educational tool. Users engage with a product that not only entertains but also subtly educates, making it a valuable and holistic addition to the Safe Space platform.

In summary, the Maze Game contributes significantly to Safe Space by combining entertainment with mental well-being, offering users a delightful and educational experience. The integration of humor and the practical application of programming concepts enrich the overall impact of the project, aligning it with the goals of creating a positive and supportive space for users.






## Installation and Usage Instructions

### Installation:

1. **Install Visual Studio Code:**
   - If you haven't installed Visual Studio Code, download and install it from the [official website](https://code.visualstudio.com/).

2. **Open the Project in Visual Studio Code:**
   - Clone or download the Maze Game project from the [GitHub repository](https://github.com/Gabi-Gindoff/MazeGame).

3. **Open Visual Studio Code:**
   - Launch Visual Studio Code on your computer.

4. **Open the Project Folder:**
   - Click on "File" in the top-left corner of Visual Studio Code.
   - Select "Open Folder" and choose the folder where you cloned or downloaded the Maze Game project.


### Install Dependencies:

5. **Install Required Packages:**
   - Open a new terminal in Visual Studio Code (you can do this by clicking on `View` at the top of the screen and then selecting `Terminal`).
   - Run the following command in the terminal:
     ```
     pip install -r mazeRequirements.txt
     ```

   - Note: The entire application runs in Visual Studio / Visual Studio Code. It will **NOT** run in Google Collab or GitHub Codespaces due to pygame pop-ups not functioning correctly.

### Usage:

6. **Run the Game:**
   - In Visual Studio Code, make sure you have the `homePage.py` file open.

7. **Open a Terminal:**
   - If you don't have the terminal open, you can do this by clicking `View` at the top of the screen and then selecting `Terminal` from the drop-down menu.

8. **Run the `homePage.py` Script:**
    - In the terminal, run the following command:
      ```bash
      python homePage.py
      ```

9. **Navigate the Game:**
    - Follow the on-screen instructions.
    - Click on the "instructions" button for details on how to play.

10. **Enjoy the Maze Game:**
    - Play the game by collecting yellow squares (packages) and reaching the red square to complete the maze.
    - Press the space bar to reveal the shortest path.
    - Have fun exploring and navigating the maze!

11. **Exiting the Application:**
    - Press "Quit" in the game interface or reach the red square to exit the application.





## Code Structure

<img width="912" alt="image" src="https://github.com/Gabi-Gindoff/MazeGame/assets/144366612/a6585c82-95b8-4a36-8977-a54e2ba71c4f">



The Maze Game project is organized into a well-defined structure, comprising several key elements:

1. **`homePage.py:`** This script serves as the control center for the game's home page. It manages buttons for initiating gameplay, exiting the application, and accessing instructions, providing users with a seamless interface.
   - Import necessary libraries
   - Initialize Pygame
   - Define constants
   - Define functions:
     - `draw_home_page()`: Draw home page elements
     - `handle_events()`: Handle user input and events on the home page
   - Main loop:
     - Draw home page
     - Handle events
     - Update display
   - Clean up


2. **`maze.py:`** Responsible for the core functionalities, this script implements maze generation, the Breadth-First Search (BFS) pathfinding algorithm, and game logic governing the user's movement and interaction with packages. It forms the backbone of the gaming experience.
   - Import necessary libraries
   - Define constants
   - Define functions:
     - `generate_maze()`: Generate a maze
     - `draw_maze()`: Draw the maze
     - `bfs_pathfinding()`: Implement Breadth-First Search pathfinding algorithm
     - `handle_user_input()`: Handle user movement and interaction with packages
   - Main game loop:
     - Generate maze
     - Draw maze
     - Perform BFS pathfinding
     - Handle user input
     - Update display
   - Clean up

3. **`instructions.py:`** Dedicated to offering clear guidance, this script displays instructions on how to play the game. It ensures that users have a comprehensive understanding of the game mechanics and objectives.
   - Import necessary libraries
   - Define constants
   - Define functions:
     - `display_instructions()`: Display game instructions
     - `handle_events()`: Handle events to exit the instructions page
   - Main loop:
     - Display instructions
     - Handle events
     - Update display
   - Clean up


4. **`mazeRequirements.txt:`** This file consolidates all dependencies and installations required to run the application. It simplifies the setup process by providing a centralized list of prerequisites.

5. **`mazePic.jpeg:`** A visual element, this image serves as the background for the game, enhancing the overall aesthetic appeal and user experience.

6. **`README.md:`** The project report is a comprehensive document that acts as a guide and reference for users and collaborators.
   - Project goals
   - Significance of the project
   - Installation and usage instructions
   - Code structure
   - List of functionalities and test results
   - Discussion and conclusion





## List of Functionalities and Test Results

### Functionalities:

The Maze Game integrates various components to deliver a seamless and enjoyable user experience. The overall functionality encompasses the following aspects:

1. **User Interface:**
   - The home page provides clear navigation with buttons for playing, quitting, and accessing instructions.
   - Interactive buttons enhance the user experience, ensuring intuitive and straightforward navigation.

2. **Maze Generation and Navigation:**
   - The maze generation algorithm creates dynamic and challenging mazes.
   - Users can navigate through the maze using arrow keys, adding an element of strategy and skill to the game.

3. **Package Collection and Humor Integration:**
   - Yellow squares (packages) trigger jokes upon collection, enhancing user happiness and creating a lighthearted atmosphere.
   - The incorporation of humor adds a therapeutic and enjoyable dimension to the gaming experience.

4. **Shortest Path and Victory:**
   - Pressing the space bar reveals the shortest path, aiding users in completing the maze efficiently.
   - Victory conditions are met with a congratulatory message, providing a sense of accomplishment.

5. **Instructions Page:**
   - Clear and concise instructions ensure that users understand the game mechanics, contributing to a smooth and engaging experience.

6. **Dependency Management:**
   - The inclusion of the `mazeRequirements.txt` file simplifies the installation process, ensuring that the required dependencies are met.


### Test Results:

- **Functionality Testing:**
  - **Buttons:** Verified that the buttons work correctly and lead to the proper pages.

    <img width="300" alt="image" src="https://github.com/Gabi-Gindoff/MazeGame/assets/144366612/86f42c81-fee1-4396-b9d9-c100be3c2595">
  - **User Movement:** Verified arrow keys' responsiveness and accurate maze navigation.
    <img width="451" alt="image" src="https://github.com/Gabi-Gindoff/MazeGame/assets/144366612/7c6d13f9-20e4-4b97-b62c-e999cda27e76">
  - **Package Collection:** Ensured jokes triggered correctly upon collecting yellow squares.
    <img width="451" alt="image" src="https://github.com/Gabi-Gindoff/MazeGame/assets/144366612/1aaa066a-33d9-4a15-a63d-f9b8768e67b8">
  - **Shortest Path:** Confirmed the space bar correctly revealed the shortest path.
    <img width="454" alt="image" src="https://github.com/Gabi-Gindoff/MazeGame/assets/144366612/3eec4ba9-7c5c-4cbf-9712-2a3c943a5df6">


  - **Victory:** Checked congratulatory message appearance upon reaching the maze's end.
    <img width="452" alt="image" src="https://github.com/Gabi-Gindoff/MazeGame/assets/144366612/50922e21-db82-441f-b7e0-e44684c5105e">

- **Instructions Page Testing:**
  - **Clarity:** Verified instructions for clear and understandable guidance.
  - **Correctness:** Ensured that instructions accurately reflected game mechanics.

We performed various testing to guarantee the functionality of key features, the accuracy of provided instructions, and successful dependency management. All tests were successful, confirming a reliable and enjoyable user experience.




## Discussion and Conclusions

### Project Issues and Limitations:

- **Scoring System and Progress Tracking:**
  - The absence of a scoring system limits the game's ability to provide users with a quantitative measure of their performance.
  - Implementing a mechanism to track user progress beyond package collection could enhance engagement and motivation.

- **Maze Generation Optimization:**
  - While the current maze generation algorithm is functional, there is room for optimization to create more intricate and challenging mazes.
  - Exploring advanced algorithms or tweaking parameters could contribute to a more diverse and engaging gaming experience.

- **User Guidance:**
  - The game lacks a tutorial or additional guidance for first-time users, which may affect the initial learning curve.
  - Integrating a tutorial or hints system could improve the onboarding experience for new players.

### Application of Course Learnings:

- **BFS Algorithm:**
  - The Breadth-First Search (BFS) algorithm is a fundamental part of the Maze Game, used for finding the shortest path.
  - Applying BFS showcases its practical utility in solving real-world problems, emphasizing its versatility in different domains.

- **Problem Solving:**
  - The project required systematic problem-solving skills, from maze generation to user navigation and humor integration.
  - The iterative process of identifying issues, devising solutions, and refining the implementation mirrors real-world problem-solving scenarios.

- **Python Programming:**
  - The project extensively utilized Python for its simplicity, readability, and versatility.
  - Writing clear and efficient code in Python contributes to the overall success of the project, demonstrating proficiency in the language.

- **Logical and Critical Thinking:**
  - Designing the game logic, including maze navigation, package collection, and humor integration, demanded logical and critical thinking.
  - The ability to think critically and strategically is a valuable skill reinforced through the development process.


### Enhancing Happiness Through Gameplay:

- **Humor Integration:**
  - The incorporation of lighthearted jokes upon collecting packages adds a unique and joyful element to the Maze Game.
  - Research suggests that humor has therapeutic effects, offering a natural and accessible means to alleviate stress and elevate mood.

- **Challenging Gameplay:**
  - The maze's dynamic and challenging nature contributes to a sense of accomplishment upon completing levels.
  - Overcoming challenges in a game setting can trigger the release of endorphins, promoting a positive emotional experience for players.

In conclusion, the Maze Game project not only serves as a multifaceted learning experience by addressing both technical and problem-solving aspects, but also as a source of entertainment and happiness for users. The identified issues present opportunities for future enhancements, and the application of course learnings highlights the practical and versatile nature of programming skills developed throughout the course. The combination of humor, challenges, and thoughtful game design aligns with Safe Space's mission, providing an engaging and uplifting experience.


