import pygame

window_height = 500 # as we'll have square so height = width hence 1 param is fine

def redraw_window(window):
    window.fill((0,0,0)) # 0 0 0 is for black 
    pygame.display.update()

def main():
    window = pygame.display.set_mode(size=(window_height,window_height)) 
    clock = pygame.time.Clock()
    while(True):
        pygame.time.delay(50) # 50 ms delay so that app does not run too fast
        clock.tick(10) # 10 fps, snake moves 10 blocks per sec
        redraw_window(window)


main()