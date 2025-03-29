import pygame
import math

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GFG Paint")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# Задний фон (белый)
screen.fill(WHITE)

# Кнопки выбора цветов
COLOR_BUTTONS = [
    {"color": RED, "rect": pygame.Rect(10, 10, 50, 50)},
    {"color": YELLOW, "rect": pygame.Rect(70, 10, 50, 50)},
    {"color": GREEN, "rect": pygame.Rect(130, 10, 50, 50)},
    {"color": BLUE, "rect": pygame.Rect(190, 10, 50, 50)},
    {"color": PURPLE, "rect": pygame.Rect(250, 10, 50, 50)}
]

# Загрузка изображения ластика
eraser_img = pygame.image.load("C:\\Users\\HUAWEI\\Downloads\\Telegram Desktop\\Lab9\\Lab9\\Source\\eraser.png")
eraser_img = pygame.transform.scale(eraser_img, (50, 50))

# Кнопки выбора фигур
TOOLS = [
    {"name": "Линия", "rect": pygame.Rect(320, 10, 90, 40), "type": "pencil"},
    {"name": "Прямоугольник", "rect": pygame.Rect(420, 10, 150, 40), "type": "rectangle"},
    {"name": "Круг", "rect": pygame.Rect(580, 10, 90, 40), "type": "circle"},
    {"name": "Квадрат", "rect": pygame.Rect(680, 10, 90, 40), "type": "square"},
    {"name": "Пр. Треугольник", "rect": pygame.Rect(780, 10, 120, 40), "type": "right_triangle"},
    {"name": "Равн. Треугольник", "rect": pygame.Rect(320, 60, 150, 40), "type": "equilateral_triangle"},
    {"name": "Ромб", "rect": pygame.Rect(480, 60, 90, 40), "type": "rhombus"},
]

# Кнопка выбора ластика
eraser_button = pygame.Rect(580, 60, 50, 50)

# Текущие настройки
current_color = BLACK
current_tool = "pencil"
drawing = False
start_pos = None
last_pos = None

# Функции для рисования фигур
def draw_pencil(surface, color, start, end, width=3):
    pygame.draw.line(surface, color, start, end, width)

def draw_rectangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    pygame.draw.rect(surface, color, (min(x1, x2), min(y1, y2), width, height), 3)

def draw_circle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    pygame.draw.circle(surface, color, start, radius, 3)

def draw_square(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surface, color, (x1, y1, side, side), 3)

def draw_right_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surface, color, points, 3)

def draw_equilateral_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    side = abs(x2 - x1)
    height = int(math.sqrt(3) / 2 * side)
    points = [(x1, y1 + height), (x1 + side, y1 + height), (x1 + side // 2, y1)]
    pygame.draw.polygon(surface, color, points, 3)

def draw_rhombus(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    points = [(x1 + width // 2, y1), (x2, y1 + height // 2), (x1 + width // 2, y2), (x1, y1 + height // 2)]
    pygame.draw.polygon(surface, color, points, 3)

def erase_area(surface, position):
    pygame.draw.circle(surface, WHITE, position, 20)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Проверка кнопок инструментов
                for button in TOOLS:
                    if button["rect"].collidepoint(event.pos):
                        current_tool = button["type"]

                # Проверка кнопки ластика
                if eraser_button.collidepoint(event.pos):
                    current_tool = "eraser"

                # Проверка кнопок цветов
                for button in COLOR_BUTTONS:
                    if button["rect"].collidepoint(event.pos):
                        current_color = button["color"]

                start_pos = event.pos
                last_pos = event.pos
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos
                if start_pos and end_pos:
                    shapes = {
                        "rectangle": draw_rectangle,
                        "circle": draw_circle,
                        "square": draw_square,
                        "right_triangle": draw_right_triangle,
                        "equilateral_triangle": draw_equilateral_triangle,
                        "rhombus": draw_rhombus,
                    }
                    if current_tool in shapes:
                        shapes[current_tool](screen, current_color, start_pos, end_pos)
                        pygame.display.update()  # Обновление экрана после рисования

        # Движение мыши для рисования
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == "pencil":
                    draw_pencil(screen, current_color, last_pos, event.pos, 3)
                    last_pos = event.pos  # Обновление последней позиции
                elif current_tool == "eraser":
                    erase_area(screen, event.pos)

    # Рисуем кнопки цветов
    for button in COLOR_BUTTONS:
        pygame.draw.rect(screen, button["color"], button["rect"])

    # Рисуем кнопки инструментов
    for button in TOOLS:
        pygame.draw.rect(screen, BLACK, button["rect"], 2)
        font = pygame.font.Font(None, 24)
        text = font.render(button["name"], True, BLACK)
        screen.blit(text, (button["rect"].x + 5, button["rect"].y + 10))

    # Кнопка ластика
    pygame.draw.rect(screen, BLACK, eraser_button, 2)
    screen.blit(eraser_img, (eraser_button.x, eraser_button.y))

    pygame.display.flip()

pygame.quit()