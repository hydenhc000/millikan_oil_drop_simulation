import pygame

def create_oil_drop(screen, state):

    width, height = screen.get_size()

    x = width // 2
    y = int(state["y"])

    pygame.draw.circle(screen, (240, 240, 80), (x, y), 20)