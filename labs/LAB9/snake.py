import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна и сетки
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
DARK_RED = (139, 0, 0)

# Направления движения змейки
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Класс змейки
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.alive = True

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        if not self.alive:
            return
        
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)

        # Проверка столкновений
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            self.alive = False
            return

        if new_head in self.positions:
            self.alive = False
            return

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.__init__()

    def draw(self, surface):
        for segment in self.positions:
            pygame.draw.rect(surface, self.color, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, WHITE, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE), 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

# Класс еды с разными типами и таймером
class Food:
    def __init__(self):
        self.food_types = [
            {'color': RED, 'score': 1, 'time': 300},  # Обычная еда
            {'color': BLUE, 'score': 3, 'time': 200},  # Дает больше очков
            {'color': YELLOW, 'score': 5, 'time': 150}  # Дает много очков, но исчезает быстрее
        ]
        self.type = random.choice(self.food_types)
        self.position = (0, 0)
        self.timer = self.type['time']
        self.randomize_position([])

    def randomize_position(self, snake_positions):
        while True:
            new_position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
            if new_position not in snake_positions:
                self.position = new_position
                self.type = random.choice(self.food_types)  # Меняем тип еды при генерации
                self.timer = self.type['time']
                break

    def update(self):
        self.timer -= 1
        return self.timer > 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.type['color'], pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, WHITE, pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE), 1)

# Функции отрисовки текста и экрана смерти
def draw_text(surface, text, x, y, size=36, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def game_over_screen(score):
    screen.fill(DARK_RED)
    draw_text(screen, "ВЫ УМЕРЛИ!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 50, WHITE)
    draw_text(screen, f"Ваш счет: {score}", SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 40, WHITE)
    draw_text(screen, "Нажмите ПРОБЕЛ для рестарта или ESC для выхода", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 50, 30, WHITE)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Основной игровой цикл
def main():
    while True:
        snake = Snake()
        food = Food()
        score = 0
        level = 1
        clock = pygame.time.Clock()

        while snake.alive:
            screen.fill(BLACK)
            snake.handle_keys()
            snake.move()
            
            if snake.get_head_position() == food.position:
                snake.length += 1
                score += food.type['score']
                food.randomize_position(snake.positions)
                
                if score % 3 == 0:
                    level += 1
            
            if not food.update():
                food.randomize_position(snake.positions)
            
            if not snake.alive:
                game_over_screen(score)
                break
            
            snake.draw(screen)
            food.draw(screen)
            draw_text(screen, f"Score: {score}", 10, 10)
            draw_text(screen, f"Level: {level}", 10, 40)
            
            pygame.display.update()
            clock.tick(8 + level)

if __name__ == '__main__':
    main()