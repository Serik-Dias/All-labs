import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Game settings
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coinscore = 0
COIN_SPEED = 5
COIN_THRESHOLD = 5  # Coins required to increase enemy speed
ENEMY_SPEED_INCREMENT = 1
COIN_SIZE = (60, 60)  # Standard coin size

# Load assets
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")
background = pygame.image.load(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\road (1).png")
coin_images = {
    1: pygame.transform.scale(pygame.image.load(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\coin1.png"), COIN_SIZE),
    2: pygame.transform.scale(pygame.image.load(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\coin2.jpg"), COIN_SIZE),
    3: pygame.transform.scale(pygame.image.load(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\coin3.jpg"), COIN_SIZE),
}

# Display setup
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\Enemy (1).png"), (55, 110))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\Player.png"), (60, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(7, 0)

# Coin class with different weights
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value = random.choice([1, 2, 3])  # Random coin value
        self.image = coin_images[self.value]  # Assign scaled image based on value
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31)

    def move(self):
        global coinscore, SPEED
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()
        elif self.rect.colliderect(P1.rect):
            coinscore += self.value  # Increase score by coin value
            if coinscore % COIN_THRESHOLD == 0:
                increase_enemy_speed()
            self.reset_position()

    def reset_position(self):
        self.value = random.choice([1, 2, 3])  # Assign new random value
        self.image = coin_images[self.value]  # Assign corresponding scaled image
        self.rect.top = -31
        self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31)

# Increase enemy speed function
def increase_enemy_speed():
    global SPEED
    SPEED += ENEMY_SPEED_INCREMENT

# Initialize objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)
coins = pygame.sprite.Group()
coins.add(C1)

# Background scrolling variables
bgy = 0
bgsound = pygame.mixer.Sound(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\background.wav")
bgsound.play(loops=-1)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Scroll background
    DISPLAYSURF.blit(background, (0, bgy))
    DISPLAYSURF.blit(background, (0, bgy-600))
    bgy = (bgy + 7) % 600
    
    # Display scores
    scores = font_small.render(str(SCORE), True, "BLACK")
    coinscores = font_small.render(str(coinscore), True, "BLACK")
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coinscores, (360, 10))
    
    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for coin in coins:
        DISPLAYSURF.blit(coin.image, coin.rect)
        coin.move()
    
    # Collision detection
    if pygame.sprite.spritecollideany(P1, enemies):
        bgsound.stop()
        pygame.mixer.Sound(r"C:\Users\HUAWEI\Downloads\Telegram Desktop\Lab9\Lab9\Source\crash.wav").play()
        time.sleep(0.5)
        DISPLAYSURF.fill("RED")
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)