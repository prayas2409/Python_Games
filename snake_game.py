import pygame

window_height = 500 # as we'll have square so height = width hence 1 param is fine
rows = 20
black_color = (0,0,0)
white_color = (255,255,255)

def draw_grids(max_width,num_of_rows,window):
    gap_between_boxes = max_width // rows # // to get int
    x = y = 0 # initialize x and y to 0
    for _ in range(rows):
        x = x + gap_between_boxes
        y = y + gap_between_boxes
        pygame.draw.line(window,white_color,(x,0), (x,max_width)) # drawing lines from x axis till max width
        pygame.draw.line(window,white_color,(0,y), (max_width,y))

def redraw_window(window):
    window.fill(black_color) # 0 0 0 is for black 
    draw_grids(window_height,rows,window)
    pygame.display.update()

def main():
    window = pygame.display.set_mode(size=(window_height,window_height)) 
    clock = pygame.time.Clock()
    while(True):
        pygame.time.delay(50) # 50 ms delay so that app does not run too fast
        clock.tick(10) # 10 fps, snake moves 10 blocks per sec
        redraw_window(window)
        pass


main()