import pygame
import sqlite3
import random

# ------------------------- DATABASE SETUP -------------------------

# Initialize the database and create necessary tables if they don't exist
def init_db():
    conn = sqlite3.connect("snake_game.db")
    cur = conn.cursor()

    # Create a user table to store usernames
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')

    # Create a table to store user scores and levels
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            level INTEGER,
            score INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id)
        )
    ''')

    conn.commit()
    conn.close()

# Fetch user by username or create a new user entry if not exists
def get_or_create_user(username):
    conn = sqlite3.connect("snake_game.db")
    cur = conn.cursor()

    # Check if the user exists
    cur.execute("SELECT id FROM user WHERE username=?", (username,))
    user = cur.fetchone()

    # Get user_id if user exists, otherwise insert new user
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO user (username) VALUES (?)", (username,))
        conn.commit()
        user_id = cur.lastrowid

    # Fetch the highest level achieved by the user
    cur.execute("SELECT MAX(level) FROM user_score WHERE user_id=?", (user_id,))
    level = cur.fetchone()[0] or 1  # Default to level 1 if none found

    conn.close()
    return user_id, level

# Save the score and level for a user
def save_score(user_id, level, score):
    conn = sqlite3.connect("snake_game.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (?, ?, ?)",
                (user_id, level, score))
    conn.commit()
    conn.close()

# ------------------------- GAME LOGIC -------------------------

# Render text on the screen
def draw_text(screen, text, x, y, font):
    screen.blit(font.render(text, True, (255, 255, 255)), (x, y))

# Generate wall positions based on current level
def generate_walls(level, width, height, tile_size):
    walls = []
    for _ in range(level):  # One more wall for each level
        x = random.randint(1, width // tile_size - 2)
        y = random.randint(1, height // tile_size - 2)
        walls.append((x, y))
    return walls

# Display the start menu with the user's name and current level
def show_start_menu(screen, font, username, level):
    button_rect = pygame.Rect(250, 200, 100, 40)
    waiting = True

    while waiting:
        screen.fill((30, 30, 30))
        draw_text(screen, f"Welcome, {username}!", 200, 100, font)
        draw_text(screen, f"Current Level: {level}", 220, 140, font)

        # Draw the Start button
        pygame.draw.rect(screen, (70, 130, 180), button_rect)
        draw_text(screen, "Start", button_rect.x + 25, button_rect.y + 10, font)

        pygame.display.flip()

        # Wait for user to click the Start button or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False

# Update user's current level in the database
def update_user_level(user_id, new_level):
    conn = sqlite3.connect("snake_game.db")
    cur = conn.cursor()
    cur.execute("UPDATE user SET current_level = ? WHERE id = ?", (new_level, user_id))
    conn.commit()
    conn.close()

# Ensure the current_level column exists in the user table
def update_db_schema():
    conn = sqlite3.connect("snake_game.db")
    cur = conn.cursor()
    try:
        cur.execute("ALTER TABLE user ADD COLUMN current_level INTEGER DEFAULT 1")
        conn.commit()
    except sqlite3.OperationalError:
        pass  # If column already exists, ignore the error
    conn.close()

# ------------------------- MAIN GAME LOOP -------------------------
def main(username):
    WIDTH, HEIGHT = 600, 400
    TILE_SIZE = 20

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game with Levels")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    # Ensure DB schema is updated and get user data
    update_db_schema()
    user_id, level = get_or_create_user(username)

    # Show start menu
    show_start_menu(screen, font, username, level)

    # Short "get ready" message
    screen.fill((0, 0, 0))
    draw_text(screen, f"Welcome, {username}!", WIDTH // 2 - 80, HEIGHT // 2 - 30, font)
    draw_text(screen, f"Level {level} - Get Ready!", WIDTH // 2 - 100, HEIGHT // 2, font)
    pygame.display.flip()
    pygame.time.wait(1000)

    # Game variables
    score = 0
    speed = 8 + level * 4
    walls = generate_walls(level, WIDTH, HEIGHT, TILE_SIZE)
    snake = [(5, 5)]
    direction = (1, 0)  # Moving right
    food = (random.randint(0, WIDTH // TILE_SIZE - 1), random.randint(0, HEIGHT // TILE_SIZE - 1))

    paused = False
    running = True
    game_over = False

    # Display "Get Ready" before game starts
    screen.fill((0, 0, 0))
    draw_text(screen, f"Welcome, {username}!", WIDTH // 2 - 80, HEIGHT // 2 - 30, font)
    draw_text(screen, f"Level {level} - Get Ready!", WIDTH // 2 - 100, HEIGHT // 2, font)
    pygame.display.flip()
    pygame.time.wait(3000)

    # Main game loop
    try:
        while running:
            screen.fill((0, 0, 0))
            draw_text(screen, f"User: {username} | Level: {level} | Score: {score}", 10, 10, font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_score(user_id, level, score)
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Change direction
                    if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)
                    elif event.key == pygame.K_p:
                        paused = not paused
                        if paused:
                            save_score(user_id, level, score)
                            draw_text(screen, "Paused - Press P to resume", WIDTH//2 - 100, HEIGHT//2, font)
                            pygame.display.flip()
                            # Pause loop
                            while paused:
                                for e in pygame.event.get():
                                    if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                                        paused = False

            if not paused:
                # Move snake
                head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

                # Check collisions with self, wall or boundary
                if (head in snake or
                    head in walls or
                    not (0 <= head[0] < WIDTH // TILE_SIZE) or
                    not (0 <= head[1] < HEIGHT // TILE_SIZE)):
                    save_score(user_id, level, score)
                    game_over = True
                    running = False
                    continue

                # Update snake position
                snake.insert(0, head)

                if head != food:
                    snake.pop()  # Only grow when food is eaten

                else:
                    # Food eaten
                    score += 10
                    food = (random.randint(0, WIDTH // TILE_SIZE - 1), random.randint(0, HEIGHT // TILE_SIZE - 1))

                    # Level progression logic
                    if score >= 200 and level < 3:
                        level = 3
                        update_user_level(user_id, 3)
                    elif score >= 100 and level < 2:
                        level = 2
                        update_user_level(user_id, 2)

                # Draw snake
                for part in snake:
                    pygame.draw.rect(screen, (0, 255, 0), (*[x*TILE_SIZE for x in part], TILE_SIZE, TILE_SIZE))

                # Draw food
                pygame.draw.rect(screen, (255, 0, 0), (*[x*TILE_SIZE for x in food], TILE_SIZE, TILE_SIZE))

                # Draw walls
                for wall in walls:
                    pygame.draw.rect(screen, (100, 100, 100), (*[x*TILE_SIZE for x in wall], TILE_SIZE, TILE_SIZE))

            pygame.display.flip()
            clock.tick(speed)

    # Catch any unexpected error
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        input("Press Enter to close...")

    # Game over screen
    if game_over:
        waiting_for_restart = True
        while waiting_for_restart:
            screen.fill((0, 0, 0))
            draw_text(screen, f"Game Over! Final Score: {score}", WIDTH//2 - 120, HEIGHT//2 - 20, font)
            draw_text(screen, "Press R to Restart or Q to Quit", WIDTH//2 - 140, HEIGHT//2 + 20, font)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_restart = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart game with the same username
                        main(username)
                        return
                    elif event.key == pygame.K_q:
                        waiting_for_restart = False

    pygame.quit()
    input("Press Q to exit...")

# ------------------------- ENTRY POINT -------------------------
if __name__ == "__main__":
    init_db()  # Set up the database
    username = input("Enter your username: ")  # Prompt user for name
    main(username)  # Start the game