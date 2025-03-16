import pygame
from pygame.locals import *

pygame.init()
tracks = ["C:\\Users\\HUAWEI\\Desktop\\All labs\\labs\\LAB7\\ajjrat_Nrtas_-_You_are_just_my_universe_62614752.mp3", 
          "C:\\Users\\HUAWEI\\Desktop\\All labs\\labs\\LAB7\\Qairat_Nurtas_-_Baiqa_63647570.mp3", 
]
current_track = 0
pygame.mixer.init()
pygame.mixer.music.load(tracks[current_track])

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

def draw_ui():
    screen.fill((30, 30, 30))
    text = font.render(f"Track {current_track + 1}", True, (255, 255, 255))
    screen.blit(text, (150, 50))
    labels = ["Stop", "Play", "Prev", "Next"]
    colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0)]
    for i, (label, color) in enumerate(zip(labels, colors)):
        pygame.draw.rect(screen, color, (50 + i * 90, 120, 80, 40))
        screen.blit(font.render(label, True, (255, 255, 255)), (65 + i * 90, 130))
    pygame.display.flip()

def control(action):
    global current_track
    if action == "play": pygame.mixer.music.unpause() if pygame.mixer.music.get_busy() else pygame.mixer.music.play()
    if action == "stop": pygame.mixer.music.stop()
    if action == "next": current_track = (current_track + 1) % len(tracks)
    if action == "prev": current_track = (current_track - 1) % len(tracks)
    if action in ["next", "prev"]: pygame.mixer.music.load(tracks[current_track]); pygame.mixer.music.play()

running = True
while running:
    draw_ui()
    for event in pygame.event.get():
        if event.type == QUIT: running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE: control("play")
            elif event.key == K_s: control("stop")
            elif event.key == K_RIGHT: control("next")
            elif event.key == K_LEFT: control("prev")
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, action in enumerate(["stop", "play", "prev", "next"]):
                if 50 + i * 90 <= x <= 130 + i * 90 and 120 <= y <= 160:
                    control(action)
pygame.quit()