import random
import time
import os

# Game settings
WIDTH = 30      # Width of the game area
HEIGHT = 10     # Height of the game area
PLAYER_CHAR = "A"  # Player character
OBSTACLE_CHAR = "#"  # Obstacle character
EMPTY_SPACE = " "  # Empty space character

# Player settings
player_x = WIDTH // 2
player_y = HEIGHT - 1
score = 0

# Initialize obstacle positions
obstacles = []

# Clear the screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Draw the game state
def draw_game():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if y == player_y and x == player_x:
                print(PLAYER_CHAR, end="")
            elif any(obstacle['x'] == x and obstacle['y'] == y for obstacle in obstacles):
                print(OBSTACLE_CHAR, end="")
            else:
                print(EMPTY_SPACE, end="")
        print()  # Newline at the end of each row
    print(f"Score: {score}")

# Update obstacles position and add new obstacles
def update_obstacles():
    global score
    # Move obstacles down
    for obstacle in obstacles:
        obstacle['y'] += 1
    
    # Remove obstacles that are out of bounds and increase score
    obstacles[:] = [ob for ob in obstacles if ob['y'] < HEIGHT]
    score += len(obstacles)  # Increase score for obstacles avoided

    # Add a new obstacle at a random position at the top
    if random.random() < 0.3:  # 30% chance to spawn a new obstacle each frame
        new_obstacle_x = random.randint(0, WIDTH - 1)
        obstacles.append({'x': new_obstacle_x, 'y': 0})

# Check for collision with obstacles
def check_collision():
    return any(obstacle['x'] == player_x and obstacle['y'] == player_y for obstacle in obstacles)

# Main game loop
def game_loop():
    global player_x
    while True:
        clear_screen()
        draw_game()
        
        # Move player based on input
        move = input("Move (a: left, d: right, q: quit): ").strip().lower()
        if move == 'a' and player_x > 0:
            player_x -= 1
        elif move == 'd' and player_x < WIDTH - 1:
            player_x += 1
        elif move == 'q':
            print("Game Over! Final Score:", score)
            break

        # Update obstacles
        update_obstacles()
        
        # Check for collisions
        if check_collision():
            print("Game Over! Final Score:", score)
            break
        
        # Add a small delay to make game playable
        time.sleep(0.1)

# Run the game
game_loop()
