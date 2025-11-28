import pygame

def create_screen():

    # sets the screen size

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    # window title

    pygame.display.set_caption("Millikan Oil Drop Simulation")

    return screen

def screen_fill(screen):
        
        screen.fill((0, 0, 0))

def create_droplet(screen, state):

    # import the screen size from run.py

    width, height = screen.get_size()

    # creating the droplets

    # pygame.draw.circle(surface, color, position, radius)

    surface = screen
    droplet_color = (240,240, 80)
    position = (state["x"], state["y"])
    radius = 10

    pygame.draw.circle(surface, droplet_color, position, radius)

def create_plates(screen):

    # import the screen size from run.py

    width, height = screen.get_size()

    # creating the plates

    # pygame.draw.line(surface, color, starting point, ending point, thickness)

    surface = screen
    plate_color = (255, 255, 255)  # pure white
    top_start_pt = (400, 450)
    top_end_pt = (700, 450)
    bottom_start_pt = (400, 150)
    bottom_end_pt = (700, 150)
    thickness = 4

    pygame.draw.line(surface, plate_color, top_start_pt, top_end_pt, thickness)
    pygame.draw.line(surface, plate_color, bottom_start_pt, bottom_end_pt, thickness)
