
# Classic Snake Game

Welcome to the Classic Snake Game repository! This project features a classic Snake game implemented using Python's Turtle module. The game has been Dockerized to simplify deployment and ensure a consistent development environment.


## Features

- Classic Gameplay: Enjoy the traditional Snake game where you control the snake to eat food and grow longer, while avoiding collisions with the walls and itself.
- Turtle Graphics: Uses Python's Turtle module to create and manage the game graphics.
- Dockerized: The application is containerized using Docker, allowing for easy setup and consistent execution across different environments.
## Technologies Used
- Python (3.x): The primary programming language used to develop the game.
- Turtle Module: Utilized for rendering the game graphics and handling user input.
- Docker: Containerizes the application for consistent environments and easy deployment.
## Prerequisites

- Python (3.x): Ensure you have Python 3.x installed. You can download it from the official website.
- Docker: Install Docker from the official website. Docker will help you containerize and run the application easily.
## Installation

Clone the repository:
```bash
git clone https://github.com/MdEhtesham2004/Snake_Game.git
```
Build and Run with Docker:
Build the Docker Image:
```bash
docker build -t snake-game .
```
Run the Docker Container:
```bash
docker run -it --rm snake-game
```

## How to Play
- Use Arrow Keys: Control the direction of the snake using the arrow keys on your keyboard.
- Eat Food: Move the snake to eat the food items that appear on the screen. Each time the snake eats food, it grows longer.
- Avoid Collisions: Avoid hitting the walls or the snake’s own body to keep playing.
    
