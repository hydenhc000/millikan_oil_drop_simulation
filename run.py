import pygame

from display import create_oil_drop
from physics import initialize_state, apply_forces

def main():
    pygame.init()

    # activates the pygame libary

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    # ^ sets the screen size

    pygame.display.set_caption("Millikan Oil Drop Simulation")

    # ^ window title

    running = True

    # ^ turns the simulation on

    clock = pygame.time.Clock()

    state = initialize_state()

    while running:

        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            # ^ if the event of closing the window occurs, stop the simulation

        screen.fill((0, 0, 0))

        # ^ sets a backround color for window 

        apply_forces(state, dt)
        create_oil_drop(screen, state)

        pygame.display.flip()

        # ^ update the window

    pygame.quit()

    # ^ quit the window 

main()