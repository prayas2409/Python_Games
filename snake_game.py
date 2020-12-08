import pygame

window_height = 500 # as we'll have square so height = width hence 1 param is fine
rows = 20
black_color = (0,0,0) # 0 0 0 is for black
white_color = (255,255,255) # 255 255 255 is for white

def draw_grids(max_width,num_of_rows,window):
    size_of_box = max_width // rows # // to get int
    x = y = 0 # initialize x and y to 0
    for _ in range(rows):
        # increasing the x & y axis co-ordinates by size of each cube
        x = x + size_of_box 
        y = y + size_of_box
        # drawing lines from x & y axis till max width to create grid /boxes
        pygame.draw.line(window,white_color,(x,0), (x,max_width)) 
        pygame.draw.line(window,white_color,(0,y), (max_width,y))

def redraw_window(window):
    window.fill(black_color)  
    draw_grids(window_height,rows,window)
    pygame.display.update()

def main():
    window = pygame.display.set_mode(size=(window_height,window_height)) 
    clock = pygame.time.Clock()
    while(True):
        pygame.time.delay(50) # 50 ms delay so that app does not run too fast
        clock.tick(10) # 10 fps, snake moves 10 blocks per sec
        redraw_window(window)

main()