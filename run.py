import pygame

from display import create_screen, screen_fill, create_droplet, create_plates
from physics import initialize_state, apply_forces

def main():
    
    # activates the pygame libary 

    pygame.init()

    screen = create_screen()

    # turns the simulation on

    running = True

    clock = pygame.time.Clock()

    state = initialize_state()

    while running:

        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            # ^ if the event of closing the window occurs, stop the simulation

        screen_fill(screen)

        # ^ sets a backround color for window 

        apply_forces(state, dt)
        create_droplet(screen, state)
        create_plates(screen)

        pygame.display.flip()

        # ^ update the window

    pygame.quit()

    # ^ quit the window 

main()